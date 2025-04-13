
from typing import TYPE_CHECKING, Set, Optional, Dict, Any
import logging
from NetUtils import ClientStatus
#Test comment
from base64 import b64encode
import worlds._bizhawk as bizhawk
from worlds._bizhawk.client import BizHawkClient

import time
import random

from .Items import item_recv_text
logger = logging.getLogger("Client")

if TYPE_CHECKING:
    from worlds._bizhawk.context import BizHawkClientContext

RECV_IDX = 0x2FFF

class PokePinballClient(BizHawkClient):
    game = "Pokemon Pinball"
    system = "GBC"
    patch_suffix = ".apkpinball"
    local_checked_locations: Set[int]
    rom_slot_name: Optional[str]

    death_link: bool = False
    sending_death_link: bool = True
    pending_death_link: bool = False

    dex_need = 151

    def __init__(self) -> None:
        super().__init__()
        self.local_checked_locations = set()
        self.rom_slot_name = None
        self.game_state = False

    async def validate_rom(self, ctx: "BizHawkClientContext") -> bool:
        from CommonClient import logger
        from .Rom import ROM_NAME_ADR, PLAYER_NAME_ADR, OPTION_ADR
        rom_data = await bizhawk.read(
            ctx.bizhawk_ctx,
            [
            (0x134, 0xB, "ROM"), # 0 Rom Name
            (OPTION_ADR, 0x10, "ROM"), # 1 Options
            (PLAYER_NAME_ADR, 0x32, "ROM"), # 2 Player Name
            (ROM_NAME_ADR, 0x20, "ROM"), # 3 Slot Data
            ]
        )
        try:
            rom_name = rom_data[0].decode("ascii")
            if rom_name != "POKEPINBALL":
                return False
            try:
                slot_name_bytes = rom_data[2]
                self.rom_slot_name = bytes([byte for byte in slot_name_bytes if byte != 0]).decode("utf-8")
            except UnicodeDecodeError:
                logger.info("Could not read slot name from ROM. Are you sure this ROM matches this client version?")
                return False
        except bizhawk.RequestFailedError:
            return False  # Not able to get a response, say no for now
        
        gameoptions = rom_data[1]
        deathlink = gameoptions[2]
        if deathlink:
            self.death_link = True

        self.dex_need = gameoptions[0]
        ctx.game = self.game
        ctx.items_handling = 0b111
        self.player_name = rom_data[2].decode("ascii")
        ctx.slot = chr(rom_data[3][7])
        ctx.want_slot_data = True

        return True
    
    def on_package(self, ctx: "BizHawkClientContext", cmd: str, args: Dict[str, Any]) -> None:
        if cmd == "Bounced":
            if "tags" in args:
                assert ctx.slot is not None
                if "DeathLink" in args["tags"] and args["data"]["source"] != ctx.slot_info[ctx.slot].name:
                    self.on_deathlink(ctx)

    async def send_deathlink(self, ctx: "BizHawkClientContext") -> None:
        self.sending_death_link = True
        ctx.last_death_link = time.time()
        await ctx.send_death("Pinballs were lost.")

    def on_deathlink(self, ctx: "BizHawkClientContext") -> None:
        ctx.last_death_link = time.time()
        self.pending_death_link = True

    async def set_auth(self, ctx: "BizHawkClientContext") -> None:
        ctx.auth = self.rom_slot_name

    async def game_watcher(self, ctx: "BizHawkClientContext") -> None:
        from CommonClient import logger
        def send_banner_msg(text:str,writes:list):
                while len(text) < 0x20:
                    text += " "
                writes.append((0x500, text.encode("ascii") , "WRAM"))
                
                writes.append((0x15CA, bytearray([0x01,0x01,0x01,0x05,0x05,0x54,0x40,0x14]) , "WRAM"))
                return writes
        
        if ctx.slot is None:
            await ctx.send_connect(name=ctx.auth)

        try:
            ram_data = await bizhawk.read(
                ctx.bizhawk_ctx,
                [
                    (0x1400, 0x100, "WRAM"), # 0 Game RAM
                    (0x1962, 0x96, "WRAM"), # 1 Pokedex Data
                    (0x18F1, 0x1, "WRAM"), # 2 Game State
                    (RECV_IDX, 0x1, "WRAM"), # 3 Recv Index
                    (0x1616, 0x1, "WRAM"), # 4 Death State
                    (0x1AF0, 0x20, "WRAM"), # 5 AP RAM
                    (0x19FB, 0x01, "WRAM"), # 6 Pokeon Owned
                    #(0x154A, 0x1, "WRAM"), # 7 Current Map


                ]
            )
            outbound_writes = []
            game_data = ram_data[0]
            pokedex_data = ram_data[1]
            game_state = ram_data[2][0]
            recv_index = ram_data[3][0]
            mon_owned = ram_data[6][0]
            death_state = game_data[0xC9]
            game_over = ram_data[0x4][0]
            ap_ram = ram_data[5]
            bonus_clear = game_data[0x9A]
            stage_cur = game_data[0xAC]
            #meowth_score = ram_data[7][0]
            #seel_score = ram_data[0xA][0]
            #diglett_score = ram_data[8][0]
            #gastly_score = ram_data[9][0]
            #mewtwo_clears = ram_data[0xB][0]


            if game_state != 0x04:
                # Make sure you are in a pinball game
                return
            
            if self.death_link:
                await ctx.update_death_link(self.death_link)

            if self.pending_death_link:
                ## Handle deathlink
                outbound_writes.append((0x14B3, bytearray([0xF8, 0x44, 0x55, 0xA9]), "WRAM"))
                self.pending_death_link = False
                self.sending_death_link = True

            if "DeathLink" in ctx.tags  and ctx.last_death_link + 10 < time.time():
                if game_over == 0x01 and not self.sending_death_link:
                    await self.send_deathlink(ctx)
                else:
                    self.sending_death_link = False

            locs_to_send = set()
            # Handle Locations
                # Pokedex
            mon_idx = 0
            for val in pokedex_data:
                mon_idx += 1
                if val >= 3:
                    loc_id = 0x1C2000 + mon_idx
                    if loc_id not in self.local_checked_locations:
                        locs_to_send.add(loc_id)
                # Map Events
            if ap_ram[0x1] and 0x1C2098 not in self.local_checked_locations:
                locs_to_send.add(0x1C2098)
            if ap_ram[0x2] and 0x1C2099 not in self.local_checked_locations:
                locs_to_send.add(0x1C2099)

            if bonus_clear == 0x1:
                if stage_cur == 0xD and 0x1C209A not in self.local_checked_locations:
                    locs_to_send.add(0x1C209A)
                if stage_cur == 0xB and 0x1C209B not in self.local_checked_locations:
                    locs_to_send.add(0x1C209B)
                if stage_cur == 0x7 and 0x1C209C not in self.local_checked_locations:
                    locs_to_send.add(0x1C209C)
                if stage_cur == 0xF and 0x1C209D not in self.local_checked_locations:
                    locs_to_send.add(0x1C209D)
                if stage_cur == 0x9 and 0x1C209E not in self.local_checked_locations:
                    locs_to_send.add(0x1C209E)
                #outbound_writes.append((0x149A,bytearray([0x00]), "WRAM"))

                # Score
            match game_data[0x6D]:
                case 0x02:
                    if 0x1C20A0 not in self.local_checked_locations:
                        locs_to_send.add(0x1C20A0)
                case 0x05:
                    if 0x1C20A1 not in self.local_checked_locations:
                        locs_to_send.add(0x1C20A1)
                case 0x10:
                    if 0x1C20A2 not in self.local_checked_locations:
                        locs_to_send.add(0x1C20A2)
                case 0x25:
                    if 0x1C20A3 not in self.local_checked_locations:
                        locs_to_send.add(0x1C20A3)
                case 0x50:
                    if 0x1C20A4 not in self.local_checked_locations:
                        locs_to_send.add(0x1C20A4)
            
            if locs_to_send != self.local_checked_locations:
                self.local_checked_locations = locs_to_send
                if locs_to_send is not None:
                    await ctx.send_msgs([{"cmd": "LocationChecks", "locations": list(locs_to_send)}])

            # Handle Items
                # Permanent Items
            pokeball_level = 0
            red_stages = [0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,
                         0x00,0x00]
            blue_stages = [0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,
                         0x00,0x00]
            
            for item in range(len(ctx.items_received)):
                raw_item = ctx.items_received[item].item
                match raw_item:
                    case 0x1C2000:
                        pokeball_level += 1
                        if pokeball_level > 3:
                            pokeball_level = 3
                    case 0x1C2002: # Viridian Forest
                        red_stages[0x2] = 0x01
                        blue_stages[0x2] = 0x01
                    case 0x1C2003: # Pewter City
                        red_stages[0x3] = 0x01
                    case 0x1C2004: # Mt Moon
                        blue_stages[0x4] = 0x01
                    case 0x1C2005: # Cerulean City
                        red_stages[0x5] = 0x01
                        blue_stages[0x5] = 0x01
                    case 0x1C2006: # Vermilion City Seaside
                        red_stages[0x6] = 0x01
                    case 0x1C2007: # Vermilion City Streets
                        blue_stages[0x7] = 0x01
                    case 0x1C2008: # Rock Mountain
                        red_stages[0x8] = 0x01
                        blue_stages[0x8] = 0x01
                    case 0x1C2009: # Lavender Town
                        red_stages[0x9] = 0x01
                    case 0x1C200A: # Celadon City
                        blue_stages[0xA] = 0x01
                    case 0x1C200B: # Cycling Road
                        red_stages[0xB] = 0x01
                    case 0x1C200C: # Safari Zone
                        red_stages[0xC] = 0x01
                        blue_stages[0xC] = 0x01
                    case 0x1C200D: # Fuchsia City
                        blue_stages[0xD] = 0x01
                    case 0x1C200E: # Saffron City
                        blue_stages[0xE] = 0x01
                    case 0x1C200F: # Seafoam Islands
                        red_stages[0xF] = 0x01
                    case 0x1C2010: # Cinnabar Island
                        red_stages[0x10] = 0x01
                        blue_stages[0x10] = 0x01
                    case 0x1C2011: # Indigo Plateau
                        red_stages[0x11] = 0x01
                        blue_stages[0x11] = 0x01


            
            balltypes = [0x00, 0x02, 0x03, 0x05]
            outbound_writes.append((0x147E,bytearray(balltypes[pokeball_level]), "WRAM"))
            outbound_writes.append((0x1AB0,bytearray(red_stages), "WRAM"))
            outbound_writes.append((0x1AD0,bytearray(blue_stages), "WRAM"))

                # Temp Items
            if len(ctx.items_received) > recv_index:
                raw_item = ctx.items_received[recv_index].item
                #item_name = ctx.items_received[recv_index].player
                #logger.warning(f"{ctx.items_received[recv_index]}")
                match raw_item:
                    case 0x1C2030:   # Extra Ball
                        lives_cur = game_data[0x9B]
                        if lives_cur == 9:
                            lives = 9
                        else:
                            lives = lives_cur + 1
                        outbound_writes.append((0x149B, bytearray([lives]), "WRAM"))
                    case 0x1C2031:   # Pika Power
                        outbound_writes.append((0x151D, bytearray([0x01]), "WRAM"))
                    case 0x1C2032:   # Ball Saver
                        outbound_writes.append((0x14A4, bytearray([0x14]), "WRAM"))
                    case 0x1C2033:   # Slots
                        outbound_writes.append((0x1607, bytearray([0x01]), "WRAM"))
                        outbound_writes.append((0x1608, bytearray([0x01]), "WRAM"))
                if raw_item in item_recv_text:
                    #logger.warning(f"Billboard Msg: {item_recv_text[raw_item]}")
                    send_banner_msg(item_recv_text[raw_item].upper(), outbound_writes)
                outbound_writes.append((RECV_IDX, (recv_index +1).to_bytes(1, "little") , "WRAM"))

            # Handle Goal
            goalclear = False
            if mon_owned >= self.dex_need:
                goalclear = True
            if not ctx.finished_game:
                if goalclear:
                    await ctx.send_msgs([{
                        "cmd": "StatusUpdate",
                        "status": ClientStatus.CLIENT_GOAL
                    }])

            await bizhawk.write(ctx.bizhawk_ctx, outbound_writes)

        except bizhawk.RequestFailedError:
            # The connector didn't respond. Exit handler and return to main loop to reconnect
            pass