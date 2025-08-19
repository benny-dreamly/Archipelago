import logging
import time
import asyncio

from NetUtils import ClientStatus, color
from worlds.AutoSNIClient import SNIClient

from .rom_data import level_clear_data, item_rom_data, warp_data, fruit_data, gift_data, letter_data

snes_logger = logging.getLogger("SNES")
ROM_START = 0x000000
WRAM_START = 0xF50000
WRAM_SIZE = 0x20000
SRAM_START = 0xE00000

DEATHLINK_ADR = 0xFCE62

PLOK_ROMNAME_START = 0x00FFC0
PLOK_ROMHASH_START = 0x7FC0
ROMNAME_SIZE = 0x15
ROMHASH_SIZE = 0x15

DEATH_FLAG = WRAM_START + 0x766
IN_STAGE = WRAM_START + 0x77A
MAX_HEALTH = WRAM_START + 0x7B0
MAX_SHELL = WRAM_START + 0x7B2
SPIN_HAVE = WRAM_START + 0x7B4
LEVEL_ADR = WRAM_START + 0x848  # Current level
FLEA_CNT = WRAM_START + 0x908
LAST_FLEA = WRAM_START + 0xEB4

PLOK_RECV_PROGRESS_ADDR = WRAM_START + 0x774

class PlokSNIClient(SNIClient):
    game = "Plok"
    patch_suffix = ".aplok"

    queen_item_cnt = 10
    fleasanity = False
    game_clear = False
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
        death_data = await snes_read(ctx, DEATHLINK_ADR, 1)
        death_link = death_data[0]
        queen_data = await snes_read(ctx, DEATHLINK_ADR+ 1, 1)
        self.queen_item_cnt = queen_data[0]
        flea_data = await snes_read(ctx, DEATHLINK_ADR+ 2, 1)
        self.fleasanity = flea_data[0]
        if death_link:
            #ctx.allow_collect = True
            await ctx.update_death_link(bool(death_link & 0b1))

        ctx.rom = rom_name

        return True
    
    async def game_watcher(self, ctx):
        from SNIClient import snes_buffered_write, snes_flush_writes, snes_read
        if ctx.server is None or ctx.slot is None:
            return
        rom = await snes_read(ctx, PLOK_ROMHASH_START, ROMHASH_SIZE)
        if rom != ctx.rom:
            ctx.rom = None
            # We have somehow loaded a different ROM
            return
        
        location_ram_data = await snes_read(ctx, WRAM_START + 0x780, 0x30)
        level_ram = await snes_read(ctx, LEVEL_ADR, 0x1)
        death_ram = await snes_read(ctx, DEATH_FLAG, 0x1)
        flea_cnt_ram  = await snes_read(ctx, FLEA_CNT, 0x1)
        recv_count = await snes_read(ctx, PLOK_RECV_PROGRESS_ADDR, 1)
        instage_raw = await snes_read(ctx, IN_STAGE, 1)
        last_flea_raw = await snes_read(ctx, LAST_FLEA, 1)

        current_level = level_ram[0]
        death_state = death_ram[0]
        flea_count = flea_cnt_ram[0]
        last_flea = last_flea_raw[0]
        last_warp = location_ram_data[0x6]
        fruit_grab = location_ram_data[0x8:0xE]
        gift_grab = location_ram_data[0xE:0x14]
        letter_grab = location_ram_data[0x14:0x1A]
        gamemode = instage_raw[0]

        
        if "DeathLink" in ctx.tags and death_state and ctx.last_death_link + 1 < time.time():
            currently_dead = death_state in {0x1}
            await ctx.handle_deathlink_state(currently_dead)

        new_checks = []
        # Level Clears
        for loc_id, loc_data in level_clear_data.items():
            if loc_id not in ctx.locations_checked:
                data = location_ram_data[loc_data[0] - 0x780]
                masked_data = data & (1 << loc_data[1])
                bit_set = (masked_data != 0)
                invert_bit = ((len(loc_data) >= 3) and loc_data[2])
                if bit_set != invert_bit:
                    if loc_id == 0x1C0027:
                        self.game_clear = True
                    else:
                        new_checks.append(loc_id)

        # Warps
        if last_warp != 0:
            for loc_id, loc_data in warp_data.items():
                if loc_id not in ctx.locations_checked:
                    if loc_data == last_warp:
                        new_checks.append(loc_id)
            snes_buffered_write(ctx, WRAM_START + 0x786, bytes([0x00]))
            await snes_flush_writes(ctx)

        # Fruits
        if fruit_grab[0] != 0:
            fruit_level = fruit_grab[0]
            fruit_xpos = int.from_bytes(fruit_grab[2:4], byteorder='little', signed = False)
            fruit_ypos = int.from_bytes(fruit_grab[4:6], byteorder='little', signed = False)
            for loc_id, loc_data in fruit_data.items():
                if loc_id not in ctx.locations_checked:
                    loc_level = loc_data[0]
                    loc_xpos = loc_data[1]
                    loc_ypos = loc_data[2]
                    if loc_level == fruit_level and loc_xpos == fruit_xpos and loc_ypos == fruit_ypos:
                        new_checks.append(loc_id)
            snes_buffered_write(ctx, WRAM_START + 0x788, bytes([0x00]))
            await snes_flush_writes(ctx)

        # Gifts
        if gift_grab[0] != 0:
            gift_level = gift_grab[0]
            gift_xpos = int.from_bytes(gift_grab[2:4], byteorder='little', signed = False)
            gift_ypos = int.from_bytes(gift_grab[4:6], byteorder='little', signed = False)
            for loc_id, loc_data in gift_data.items():
                if loc_id not in ctx.locations_checked:
                    loc_level = loc_data[0]
                    loc_xpos = loc_data[1]
                    loc_ypos = loc_data[2]
                    if loc_level == gift_level and loc_xpos == gift_xpos and loc_ypos == gift_ypos:
                        new_checks.append(loc_id)
            snes_buffered_write(ctx, WRAM_START + 0x78E, bytes([0x00]))
            await snes_flush_writes(ctx)

        # Letters
        if letter_grab[0] != 0:
            letter_level = letter_grab[0]
            letter_xpos = int.from_bytes(letter_grab[2:4], byteorder='little', signed = False)
            letter_ypos = int.from_bytes(letter_grab[4:6], byteorder='little', signed = False)
            for loc_id, loc_data in letter_data.items():
                if loc_id not in ctx.locations_checked:
                    loc_level = loc_data[0]
                    loc_xpos = loc_data[1]
                    loc_ypos = loc_data[2]
                    if loc_level == letter_level and loc_xpos == letter_xpos and loc_ypos == letter_ypos:
                        new_checks.append(loc_id)
            snes_buffered_write(ctx, WRAM_START + 0x794, bytes([0x00]))
            await snes_flush_writes(ctx)

        # Flea Kills
        if self.fleasanity and (gamemode == 1):
            flea_base_ID = {
                0x08: 0x1C0080, # Garlen Beach
                0x09: 0x1C0090, # Sleepy Dale
                0x13: 0x1C00A0, # Plok Town
                0x15: 0x1C00B0, # Venge Thicket
                0x16: 0x1C00C0, # Dreamy Cove
                0x17: 0x1C00D0, # Creepy Forest
                0x19: 0x1C00E0, # Creepy Crag
                0x1A: 0x1C00F0, # Gohome Cavern
                0x1B: 0x1C0100, # Crashing Rocks
            }
            flea_stage_cnt = {
                0x08: 14, # Garlen Beach
                0x09: 12, # Sleepy Dale
                0x13: 10, # Plok Town
                0x15: 10, # Venge Thicket
                0x16: 15, # Dreamy Cove
                0x17: 14, # Creepy Forest
                0x19: 11, # Creepy Crag
                0x1A: 14, # Gohome Cavern
                0x1B: 8, # Crashing Rocks
            }
            if (current_level in flea_base_ID) and (flea_count != 0 or last_flea != 0):
                base_loc_id = flea_base_ID[current_level]
                stage_fleas = flea_stage_cnt[current_level]
                cur_flea = stage_fleas * 8
                while cur_flea > flea_count:
                    flea_id = (stage_fleas - (cur_flea/8) + 1)
                    cur_flea -= 0x8
                    if flea_id <= stage_fleas:
                        loc_id = base_loc_id + flea_id
                        if loc_id in ctx.server_locations:
                            if loc_id not in ctx.locations_checked:
                                new_checks.append(loc_id)


                

        for new_check_id in new_checks:
            ctx.locations_checked.add(new_check_id)
            location = ctx.location_names.lookup_in_game(new_check_id)
            snes_logger.info(
                f'New Check: {location} ({len(ctx.locations_checked)}/{len(ctx.missing_locations) + len(ctx.checked_locations)})')
            await ctx.send_msgs([{"cmd": 'LocationChecks', "locations": [new_check_id]}])


        # Handle Items
        #0x7B0-0x7CF
        write_array = [0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00, 
                       0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00, ]
        max_hp = 0x30
        max_shell = 0x20
        max_hornet = 0x0
        vechile = 0x0000
        transform = 0x0000
        limb_count = 1
        queen_items = 0
        for item in range(len(ctx.items_received)):
            raw_item = ctx.items_received[item].item
            match raw_item:
                case 0x1C0001: # Spin Jump
                    write_array[4] = 0x12
                case 0x1C0002: # Amulet
                    write_array[6] = 0x28
                case 0x1C0003: # Limb
                    limb_count += 1
                    if limb_count > 4:
                        limb_count = 4
                case 0x1C0004: # Health
                    max_hp += 0x18
                case 0x1C0005: # Hornets
                    max_hornet += 1
                case 0x1C0006: # Shell Capacity
                    max_shell += 0x10
                case 0x1C0007: # Plok Flag
                    write_array[0x10] = 0x1
                case 0x1C0008: # Granpappy Journal
                    write_array[0x12] = 0x1
                case 0x1C0009: # Flea Pit Rope
                    write_array[0x14] = 0x1
                case 0x1C000D: # Flashlight
                    write_array[0x1A] = 0x1
                case 0x1C0011: # Unicycle
                    vechile = vechile | 0x02
                case 0x1C0012: # Car
                    vechile = vechile | 0x04
                case 0x1C0013: # Jet
                    vechile = vechile | 0x08
                case 0x1C0014: # Motorcycle
                    vechile = vechile | 0x10
                case 0x1C0015: # Helicopter
                    vechile = vechile | 0x20
                case 0x1C0016: # Tank
                    vechile = vechile | 0x40
                case 0x1C0017: # UFO
                    vechile = vechile | 0x80
                case 0x1C0018: # Springs
                    write_array[0x9] = 0x1
                case 0x1C0021: # Plocky Costume
                    transform = transform | 0x06
                case 0x1C0023: # Rocketman Costume
                    transform = transform | 0x18
                case 0x1C0025: # Squire Costume
                    transform = transform | 0x20
                case 0x1C0026: # Fireman Costume
                    transform = transform | 0x40
                case 0x1C0027: # Cowboy Costume
                    transform = transform | 0x80
                case _:
                    if raw_item >= 0x1C0030 and raw_item <= 0x1C003F:
                        queen_items += 1
        limb_state = [0x0C, 0x1C, 0x1E, 0x3E, 0x3F]
        write_array[0x0] = max_hp
        write_array[0x2] = max_shell
        write_array[0x8] = vechile
        write_array[0xA] = transform
        write_array[0x18] = limb_state[limb_count]
        write_array[0x1C] = max_hornet
        if queen_items >= self.queen_item_cnt:
            write_array[0x16] = 0x1 # Unlock flea queen
        snes_buffered_write(ctx, WRAM_START + 0x7B0, bytearray(write_array))
        await snes_flush_writes(ctx)

        recv_index = recv_count[0]
        if recv_index < len(ctx.items_received):
            raw_item = ctx.items_received[recv_index].item
            match raw_item:
                case 0x1C000A: # Shells
                    shell_data = await snes_read(ctx, WRAM_START + 0x8F2, 0x1)
                    shells = shell_data[0]
                    shells += 0x10
                    if shells >= max_shell:
                        shells = max_shell
                    snes_buffered_write(ctx, WRAM_START + 0x8F2, bytearray([shells]))
                    await snes_flush_writes(ctx)
                case 0x1C000B: # Extra Plok
                    lives_data = await snes_read(ctx, WRAM_START + 0x768, 0x1)
                    lives = lives_data[0]
                    lives += 1
                    if lives >= 9:
                        lives = 9
                    snes_buffered_write(ctx, WRAM_START + 0x768, bytearray([lives]))
                    await snes_flush_writes(ctx)
                    
                case 0x1C000C: # Fruit
                    snes_buffered_write(ctx, WRAM_START + 0x806, bytearray([max_hp]))
                    await snes_flush_writes(ctx)
                case 0x1C000E: # Force Field Gem
                    snes_buffered_write(ctx, WRAM_START + 0x83D, bytearray([0x1]))
                    await snes_flush_writes(ctx)
                case 0x1C000F: # Anger Saw
                    snes_buffered_write(ctx, WRAM_START + 0x951, bytearray([0x3]))
                    await snes_flush_writes(ctx)
                # Rentals
                case 0x1C0040: # Unicycle
                    snes_buffered_write(ctx, WRAM_START + 0x822, bytearray([0x3F]))
                    snes_buffered_write(ctx, WRAM_START + 0x7F7, bytearray([0x3]))
                    snes_buffered_write(ctx, WRAM_START + 0x81E, bytearray([0x1]))
                    await snes_flush_writes(ctx)
                case 0x1C0041: # Car
                    snes_buffered_write(ctx, WRAM_START + 0x822, bytearray([0x3F]))
                    snes_buffered_write(ctx, WRAM_START + 0x7F7, bytearray([0x3]))
                    snes_buffered_write(ctx, WRAM_START + 0x81E, bytearray([0x2]))
                    await snes_flush_writes(ctx)
                case 0x1C0042: # Jet
                    snes_buffered_write(ctx, WRAM_START + 0x822, bytearray([0x3F]))
                    snes_buffered_write(ctx, WRAM_START + 0x7F7, bytearray([0x3]))
                    snes_buffered_write(ctx, WRAM_START + 0x81E, bytearray([0x3]))
                    await snes_flush_writes(ctx)
                case 0x1C0043: # Motorcycle
                    snes_buffered_write(ctx, WRAM_START + 0x822, bytearray([0x3F]))
                    snes_buffered_write(ctx, WRAM_START + 0x7F7, bytearray([0x3]))
                    snes_buffered_write(ctx, WRAM_START + 0x81E, bytearray([0x4]))
                    await snes_flush_writes(ctx)
                case 0x1C0044: # Helicopter
                    snes_buffered_write(ctx, WRAM_START + 0x822, bytearray([0x3F]))
                    snes_buffered_write(ctx, WRAM_START + 0x7F7, bytearray([0x3]))
                    snes_buffered_write(ctx, WRAM_START + 0x81E, bytearray([0x5]))
                    await snes_flush_writes(ctx)
                case 0x1C0045: # Tank
                    snes_buffered_write(ctx, WRAM_START + 0x822, bytearray([0x3F]))
                    snes_buffered_write(ctx, WRAM_START + 0x7F7, bytearray([0x3]))
                    snes_buffered_write(ctx, WRAM_START + 0x81E, bytearray([0x6]))
                    await snes_flush_writes(ctx)
                case 0x1C0046: # UFO
                    snes_buffered_write(ctx, WRAM_START + 0x822, bytearray([0x3F]))
                    snes_buffered_write(ctx, WRAM_START + 0x7F7, bytearray([0x3]))
                    snes_buffered_write(ctx, WRAM_START + 0x81E, bytearray([0x7]))
                    await snes_flush_writes(ctx)
                case 0x1C0047: # Springs
                    snes_buffered_write(ctx, WRAM_START + 0x822, bytearray([0x3F]))
                    snes_buffered_write(ctx, WRAM_START + 0x7F7, bytearray([0x3]))
                    snes_buffered_write(ctx, WRAM_START + 0x81E, bytearray([0x8]))
                    await snes_flush_writes(ctx)
                case 0x1C0048: # Boxing Glove
                    snes_buffered_write(ctx, WRAM_START + 0x822, bytearray([0x3F]))
                    snes_buffered_write(ctx, WRAM_START + 0x7F7, bytearray([0x2]))
                    snes_buffered_write(ctx, WRAM_START + 0x7F4, bytearray([0x2]))
                    await snes_flush_writes(ctx)
                case 0x1C0049: # Rocket
                    snes_buffered_write(ctx, WRAM_START + 0x822, bytearray([0x3F]))
                    snes_buffered_write(ctx, WRAM_START + 0x7F7, bytearray([0x2]))
                    snes_buffered_write(ctx, WRAM_START + 0x7F4, bytearray([0x4]))
                    await snes_flush_writes(ctx)
                case 0x1C004A: # Musket
                    snes_buffered_write(ctx, WRAM_START + 0x822, bytearray([0x3F]))
                    snes_buffered_write(ctx, WRAM_START + 0x7F7, bytearray([0x2]))
                    snes_buffered_write(ctx, WRAM_START + 0x7F4, bytearray([0x5]))
                    await snes_flush_writes(ctx)
                case 0x1C004B: # Flamethrower
                    snes_buffered_write(ctx, WRAM_START + 0x822, bytearray([0x3F]))
                    snes_buffered_write(ctx, WRAM_START + 0x7F7, bytearray([0x2]))
                    snes_buffered_write(ctx, WRAM_START + 0x7F4, bytearray([0x6]))
                    await snes_flush_writes(ctx)
                case 0x1C004C: # Badge
                    snes_buffered_write(ctx, WRAM_START + 0x822, bytearray([0x3F]))
                    snes_buffered_write(ctx, WRAM_START + 0x7F7, bytearray([0x2]))
                    snes_buffered_write(ctx, WRAM_START + 0x7F4, bytearray([0x7]))
                    await snes_flush_writes(ctx)
            recv_index = len(ctx.items_received)
            #if recv_index > recv_count[0]:
            snes_buffered_write(ctx, PLOK_RECV_PROGRESS_ADDR, bytearray([recv_index]))
            await snes_flush_writes(ctx)

        # Handle game clear
        if not ctx.finished_game and self.game_clear == True:
            await ctx.send_msgs([{"cmd": "StatusUpdate", "status": ClientStatus.CLIENT_GOAL}])
            snes_buffered_write(ctx, WRAM_START + 0x848, bytearray([0x3A, 0x00, 0x3A, 0x00]))
            await snes_flush_writes(ctx)
            ctx.finished_game = True