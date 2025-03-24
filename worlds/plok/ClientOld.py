import logging
import time
import asyncio

from NetUtils import ClientStatus, color
from worlds.AutoSNIClient import SNIClient

snes_logger = logging.getLogger("SNES")

# FXPAK Pro protocol memory mapping used by SNI
ROM_START = 0x000000
WRAM_START = 0xF50000
WRAM_SIZE = 0x20000
SRAM_START = 0xE00000

PLOK_ROMNAME_START = 0x00FFC0
PLOK_ROMHASH_START = 0x7FC0
ROMNAME_SIZE = 0x15
ROMHASH_SIZE = 0x15

DEATH_FLAG = WRAM_START + 0x766
MAX_HEALTH = WRAM_START + 0x7B0
MAX_SHELL = WRAM_START + 0x7B2
SPIN_HAVE = WRAM_START + 0x7B4

PLOK_RECV_PROGRESS_ADDR = WRAM_START + 0x774
#PLOK_FILE_NAME_ADDR = WRAM_START + 0x5D9
#DEATH_LINK_ACTIVE_ADDR = PLOK_ROMNAME_START + 0x15     # DKC3_TODO: Find a permanent home for this


class PlokSNIClient(SNIClient):
    game = "Plok"
    patch_suffix = ".aplok"

    async def deathlink_kill_player(self, ctx):
        from SNIClient import DeathState, snes_buffered_write, snes_flush_writes
        
        snes_buffered_write(ctx, DEATH_FLAG , bytes([0x01]))
        await snes_flush_writes(ctx)
        ctx.death_state = DeathState.dead
        ctx.last_death_link = time.time()


    async def validate_rom(self, ctx):
        from SNIClient import snes_buffered_write, snes_flush_writes, snes_read

        rom_name = await snes_read(ctx, PLOK_ROMHASH_START, ROMHASH_SIZE)
        print(f"{rom_name}")
        if rom_name is None or rom_name == bytes([0] * ROMHASH_SIZE) or rom_name[:2] != b"PK":
            return False

        print(self.game)
        ctx.game = self.game
        ctx.items_handling = 0b111  # remote items

        ctx.rom = rom_name

        return True


    async def game_watcher(self, ctx):
        from SNIClient import snes_buffered_write, snes_flush_writes, snes_read
        max_health = await snes_read(ctx, MAX_HEALTH , 0x1)
        max_shells = await snes_read(ctx, MAX_SHELL , 0x1)
        death = await snes_read(ctx, DEATH_FLAG , 0x1)

        if ctx.server is None or ctx.slot is None:
            return
        
        if "DeathLink" in ctx.tags and death[0] > 0 and ctx.last_death_link + 1 < time.time():
            currently_dead = 1
            await ctx.handle_deathlink_state(currently_dead)

        new_checks = []
        from .Rom import location_rom_data, item_rom_data
        location_ram_data = await snes_read(ctx, WRAM_START + 0x780, 0x30)
        for loc_id, loc_data in location_rom_data.items():
            if loc_id not in ctx.locations_checked:
                data = location_ram_data[loc_data[0] - 0x780]
                masked_data = data & (1 << loc_data[1])
                bit_set = (masked_data != 0)
                invert_bit = ((len(loc_data) >= 3) and loc_data[2])
                if bit_set != invert_bit:
                    # DKC3_TODO: Handle non-included checks
                    new_checks.append(loc_id)

        rom = await snes_read(ctx, PLOK_ROMHASH_START, ROMHASH_SIZE)
        if rom != ctx.rom:
            ctx.rom = None
            # We have somehow loaded a different ROM
            return

        for new_check_id in new_checks:
            ctx.locations_checked.add(new_check_id)
            location = ctx.location_names.lookup_in_game(new_check_id)
            snes_logger.info(
                f'New Check: {location} ({len(ctx.locations_checked)}/{len(ctx.missing_locations) + len(ctx.checked_locations)})')
            await ctx.send_msgs([{"cmd": 'LocationChecks', "locations": [new_check_id]}])


        recv_count = await snes_read(ctx, PLOK_RECV_PROGRESS_ADDR, 1)
        recv_index = recv_count[0]

        if recv_index < len(ctx.items_received):
            item = ctx.items_received[recv_index]
            recv_index += 1
            logging.info('Received %s from %s (%s) (%d/%d in list)' % (
                color(ctx.item_names.lookup_in_game(item.item), 'red', 'bold'),
                color(ctx.player_names[item.player], 'yellow'),
                ctx.location_names.lookup_in_slot(item.location, item.player), recv_index, len(ctx.items_received)))

            snes_buffered_write(ctx, PLOK_RECV_PROGRESS_ADDR, bytes([recv_index]))
            
            if item.item in item_rom_data:
                #item_count = await snes_read(ctx, WRAM_START + item_rom_data[item.item][0], 0x1)
                #new_item_count = item_count[0] + 1
                if item.item == 0x1C0004:
                    snes_buffered_write(ctx,MAX_HEALTH,bytes([max_health[0] + 0x10]))
                elif item.item == 0x1C0001:
                    snes_buffered_write(ctx,SPIN_HAVE,bytes([0x12]))
                elif item.item == 0x1C0006:
                    snes_buffered_write(ctx,MAX_SHELL,bytes([max_shells[0] + 0x14]))

            else:
                if item.item == 0xDC3000:
                    # Handle Victory
                    if not ctx.finished_game:
                        await ctx.send_msgs([{"cmd": "StatusUpdate", "status": ClientStatus.CLIENT_GOAL}])
                        ctx.finished_game = True
                else:
                    print("Item Not Recognized: ", item.item)
                pass

            await snes_flush_writes(ctx)

        # Handle Collected Locations
        for loc_id in ctx.checked_locations:
            if loc_id not in ctx.locations_checked:
                loc_data = location_rom_data[loc_id]
                data = await snes_read(ctx, WRAM_START + loc_data[0], 1)
                invert_bit = ((len(loc_data) >= 3) and loc_data[2])
                if not invert_bit:
                    masked_data = data[0] | (1 << loc_data[1])
                    snes_buffered_write(ctx, WRAM_START + loc_data[0], bytes([masked_data]))

                    await snes_flush_writes(ctx)
                else:
                    masked_data = data[0] & ~(1 << loc_data[1])
                    snes_buffered_write(ctx, WRAM_START + loc_data[0], bytes([masked_data]))
                    await snes_flush_writes(ctx)
                ctx.locations_checked.add(loc_id)

        # Calculate Boomer Cost Text
