
from typing import TYPE_CHECKING, Set, Optional, Dict, Any
import logging
from NetUtils import ClientStatus
#Test comment
from base64 import b64encode
import worlds._bizhawk as bizhawk
from worlds._bizhawk.client import BizHawkClient

from .Locations import hamigo_flag_data
from .seedsanity import seed_flag_data
from .cliRoutines import get_area_move, recalculateMedals
#from .talksanity import talk_location_data
from .costumesanity import costume_flag_data

import time
import random

logger = logging.getLogger("Client")

if TYPE_CHECKING:
    from worlds._bizhawk.context import BizHawkClientContext

RECV_IDX = 0x8020
RECV_PORT = 0x1AF0
HAMTARO_PAL = 0x4DF1D0

class HamGamesClient(BizHawkClient):
    game = "Hamtaro Hamham Games"
    system = "GBA"
    patch_suffix = ".aphamgames"
    local_checked_locations: Set[int]
    rom_slot_name: Optional[str]

    death_link: bool = False
    game_goal = 0
    sending_death_link: bool = True
    pending_death_link: bool = False

    seedsanity: bool = False
    costumesanity:bool = False
    medals_needed: int = 14
    nomination_needed: int = 50

    #needed_mons = b''

    def __init__(self) -> None:
        super().__init__()
        self.local_checked_locations = set()
        self.rom_slot_name = None
        self.game_state = False
        self.research_command = None

    async def validate_rom(self, ctx: "BizHawkClientContext") -> bool:
        from CommonClient import logger
        from .Rom import GAME_NAME_ADR, ROM_NAME_ADR, PLAYER_NAME_ADR, OPTION_ADR
        rom_data = await bizhawk.read(
            ctx.bizhawk_ctx,
            [
            (GAME_NAME_ADR, 0x9, "ROM"), # 0 Rom Name
            (OPTION_ADR, 0x10, "ROM"), # 1 Options
            (PLAYER_NAME_ADR, 0x32, "ROM"), # 2 Player Name
            (ROM_NAME_ADR, 0x20, "ROM"), # 3 Slot Data
            #(0xCEE8, 0x1, "EWRAM"), # 4 Boss flag
            ]
        )
        try:
            rom_name = (rom_data[0]).decode("ascii")
            if rom_name != "HAMSPORTS":
                logger.info(f"Wrong Name {rom_name} for this client")
                return False
            try:
                slot_name_bytes = rom_data[2]
                self.rom_slot_name = bytes([byte for byte in slot_name_bytes if byte != 0]).decode("utf-8")
            except UnicodeDecodeError:
                logger.info("Could not read slot name from ROM. Are you sure this ROM matches this client version?")
                return False
        except bizhawk.RequestFailedError:
            logger.info(f"Request Failed")
            return False  # Not able to get a response, say no for now
        
        gameoptions = rom_data[1]
        self.game_goal = gameoptions[0]
        deathlink = gameoptions[1]
        self.seedsanity = gameoptions[2]
        self.costumesanity = gameoptions[5]
        self.medals_needed = gameoptions[3]
        self.nomination_needed = gameoptions[4]
        #boss_flag = rom_data[4][0] & 0xBF # Clear Boss Waiting Flag
       # await bizhawk.write(ctx.bizhawk_ctx, [(0xCEE8, bytearray([boss_flag]), "EWRAM")])

        if deathlink:
            self.death_link = True
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
        await ctx.send_death("Hamtaro Lost.")

    def on_deathlink(self, ctx: "BizHawkClientContext") -> None:
        ctx.last_death_link = time.time()
        self.pending_death_link = True

    async def set_auth(self, ctx: "BizHawkClientContext") -> None:
        ctx.auth = self.rom_slot_name

    async def game_watcher(self, ctx: "BizHawkClientContext") -> None:
        from CommonClient import logger
        
        if ctx.slot is None:
            await ctx.send_connect(name=ctx.auth)

        try:
            ram_data = await bizhawk.read(
                ctx.bizhawk_ctx,
                [
                    (0xCEE0, 0x20, "EWRAM"), # 0 Hamigo flag/ Prelim flags
                    (RECV_IDX, 0x1, "EWRAM"), # 1 Recv Index
                    (0xCF00,0x100, "EWRAM"), # 2 Flags
                    (0xC70, 0x20, "EWRAM"), # 3 Game Stats 1
                    (0xE70, 0x100, "EWRAM"), # 4 Event Stats
                    (0xF64, 0x01, "EWRAM"), # 5 medal Count
                    (0x8008, 0x20, "EWRAM"), # 6 AP ports
                    #(0xCEFA, 0x01, "EWRAM"), # 7 Tennis Prelim flag
                    
                ]
            )
            outbound_writes = []
            #game_data = ram_data[0]
            recv_index = ram_data[1][0]
            
            

            run_counter = ram_data[3][0xB]
            day_counter = ram_data[3][0xC]
            time_counter = ram_data[3][0xD]
            medal_count = ram_data[5][0]
            arcade_score = ram_data[6][0]
            flag_data = ram_data[2]
            ingame = flag_data[0xA4] & 0x08

            

            tennis_prelim_flag = ram_data[0][0x1A]
            tennis_finals_place = ram_data[4][1]
            volleyball_prelim_flag = ram_data[0][0x1C]
            volleyball_finals_place = ram_data[4][0x21]
            hamdash_place = ram_data[4][0x51]
            hurdles_place = ram_data[4][0x59]
            marathon_place = ram_data[4][0x61]
            sailing_place = ram_data[4][0x69]
            swim_place = ram_data[4][0x71]
            hammer_place = ram_data[4][0x7D]
            polevault_place = ram_data[4][0x85]
            triple_jump_place = ram_data[4][0x8D]
            diving_place = ram_data[4][0x95]
            carrot_place = ram_data[4][0x9D]
            archery_place = ram_data[4][0xA5]
            birdback_place = ram_data[4][0xAD]
            sync_swim_place = ram_data[4][0xB5]

            

            seeds = int.from_bytes(ram_data[3][0x10:0x11], byteorder='little', signed = False)
            last_dialog  = int.from_bytes(ram_data[6][0x8:0xC], byteorder='little', signed = False)


            if not ingame:
                # Make sure you are in a game
                return
            self.game_state = True
            #if recv_index == 0xFF:
            #    outbound_writes.append((RECV_IDX, bytearray([0x00]), "EWRAM"))
            
            if self.death_link:
                await ctx.update_death_link(self.death_link)

            if self.pending_death_link:
                ## Handle deathlink
                # Code to kill the player
                #outbound_writes.append((0x14B3, bytearray([0xF8, 0x44, 0x55, 0xA9]), "WRAM"))
                self.pending_death_link = False
                self.sending_death_link = True

            if "DeathLink" in ctx.tags  and ctx.last_death_link + 10 < time.time():
                # Code to check if you are dead
                #if game_over == 0x01 and not self.sending_death_link:
                #    await self.send_deathlink(ctx)
                #else:
                    self.sending_death_link = False

            locs_to_send = set()
            # Handle Locations

            # Medals
            medal_map = {
                0x1C2200: hamdash_place,
                0x1C2206: hammer_place,
                0x1C2209: diving_place,
                0x1C220F: hurdles_place,
                0x1C2212: birdback_place,
                0x1C2215: polevault_place,
                0x1C2218: tennis_finals_place,
                0x1C221B: carrot_place,
                0x1C221E: swim_place,
                0x1C2221: archery_place,
                0x1C2224: sailing_place,
                0x1C2227: triple_jump_place,
                0x1C222A: sync_swim_place,
                0x1C222D: volleyball_finals_place
            }
            medal_have = 0
            for loc, event in medal_map.items():
                print(event)
                if event < 3:
                    locs_to_send.add(loc + 2)
                    if event < 2:
                        locs_to_send.add(loc + 1)
                        if event == 0:
                            medal_have += 1
                            locs_to_send.add(loc)

            if tennis_prelim_flag & 0x1:
                locs_to_send.add(0x1C2203) # Day 2 Tennis - Win Tennis Prelim
            if volleyball_prelim_flag & 0x08:
                locs_to_send.add(0x1C220C)

            #if arcade_score >= 25:
            #    locs_to_send.add(0x1C2240)
            
            if self.seedsanity:
                for loc, flags in seed_flag_data.items():
                    # [offset, mask]
                    flag_byte = flag_data[flags[0]-0x200CF00]
                    flag_mask = flags[1]
                    masked_flag = flag_byte & flag_mask
                    day = flags[2]
                    if (masked_flag != 0) and (day == day_counter):
                        # logger.warning(f"{hex(loc)}: {flag_byte} {flag_mask} {masked_flag} {day}/{day_counter}")
                        locs_to_send.add(loc)

            for loc, flags in hamigo_flag_data.items():
                flag_byte = flag_data[flags[0]-0x200CF00]
                flag_mask = flags[1]
                masked_flag = flag_byte & flag_mask
                if masked_flag:
                    locs_to_send.add(loc)

            if self.costumesanity:
                for loc, flags in costume_flag_data.items():
                    flag_byte = flag_data[flags[0]-0x200CF00]
                    flag_mask = flags[1]
                    masked_flag = flag_byte & flag_mask
                    if masked_flag:
                        locs_to_send.add(loc)
            #    if last_dialog in talk_location_data:
            #        locs_to_send.add(talk_location_data[last_dialog])




            #for val in game_flags:
            #    flag_idx = 0
            #    if val != 0x00:
            #        loc_id = 0x40001 + flag_idx
            #        if loc_id not in self.local_checked_locations:
            #            locs_to_send.add(loc_id)
            #    flag_idx += 1
                # Score

            if locs_to_send != self.local_checked_locations:
                self.local_checked_locations = locs_to_send
                if locs_to_send is not None:
                    await ctx.send_msgs([{"cmd": "LocationChecks", "locations": list(locs_to_send)}])

            # Handle Items
                # Permanent Items
            # Day 1 always available
            outbound_writes.append((0x8001, bytearray([0x01]), "EWRAM"))
            
            passes = [0x0F]
            nomination_have = 0
            for item in range(len(ctx.items_received)):
                raw_item = ctx.items_received[item].item

                match raw_item:
                    case 0x1C2200: # Studio Pass
                        passes.append(0x0A)
                    case 0x1C2201: # Beach Pass
                        passes.append(0x0B)
                    case 0x1C2202: # Tennis Pass
                        passes.append(0x0C)
                    case 0x1C2203: # Village Pass
                        passes.append(0x0D)
                    case 0x1C2204: # Pool Pass
                        passes.append(0x0E)
                    case 0x1C2205: # Stadium Pass
                        passes.append(0x11)
                    case 0x1C2206: # Lawn Pass
                        passes.append(0x10)
                    
                    case 0x1C2208: # Day 2
                        outbound_writes.append((0x8002, bytearray([0x01]), "EWRAM"))
                    case 0x1C2209: # Day 3
                        outbound_writes.append((0x8003, bytearray([0x01]), "EWRAM"))
                    case 0x1C220A: # Day 4
                        outbound_writes.append((0x8004, bytearray([0x01]), "EWRAM"))
                    case 0x1C220B: # Day 5
                        outbound_writes.append((0x8005, bytearray([0x01]), "EWRAM"))
                    case 0x1C220C: # Day 6
                        outbound_writes.append((0x8006, bytearray([0x01]), "EWRAM"))

                    case 0x1C220F: # Marathon Nomination
                        nomination_have += 1
                        

            #move_bytes = 
            if (medal_have >= self.medals_needed) and (nomination_have >= self.nomination_needed):
                outbound_writes.append((0x8007, bytearray([0x01]), "EWRAM"))

            outbound_writes.append((0xCCE5A4, get_area_move(passes), "ROM"))

                # Temp Items
            seeds_new = seeds
            if (len(ctx.items_received) > recv_index):
                raw_item = ctx.items_received[recv_index].item
                #item_name = ctx.items_received[recv_index].player
                #logger.warning(f"{ctx.items_received[recv_index]}")
                match raw_item:
                    case 0x1C220D: # Hamigo
                        hamigo_flag = ram_data[0][0XB]
                        if (hamigo_flag & 0x10) == 0x00:
                            new_hamigo = hamigo_flag | 0x10
                            outbound_writes.append((0xCEEB, bytearray([new_hamigo]), "EWRAM"))
                        #boss_flag = ram_data[0][0x08]
                        #if boss_flag & 0x40:
                        #    new_boss = boss_flag & 0xBF
                        #    outbound_writes.append((0xCEE8, bytearray([new_boss]), "EWRAM"))
                    case 0x1C2210: # CD
                        cdflag = flag_data[0x86]
                        newflag = cdflag | 0x40
                        outbound_writes.append((0xCF86, (newflag).to_bytes(1, "little") , "EWRAM"))
                    case 0x1C2211: # Cartridge
                        cartflag = flag_data[0x33]
                        newflag = cartflag | 0x02
                        outbound_writes.append((0xCF86, (newflag).to_bytes(1, "little") , "EWRAM"))
                    case 0x1C2220:   # 1 Seed
                        seeds_new = seeds + 1
                        outbound_writes.append((0xC80, (seeds_new).to_bytes(2, "little") , "EWRAM"))
                    case 0x1C2221:   # 5 Seeds
                        seeds_new = seeds + 5
                        outbound_writes.append((0xC80, (seeds_new).to_bytes(2, "little") , "EWRAM"))
                    case 0x1C2222:  # 10 Seeds
                        seeds_new = seeds + 10
                        outbound_writes.append((0xC80, (seeds_new).to_bytes(2, "little") , "EWRAM"))
                    case 0x1C2223:  # 25 Seeds
                        seeds_new = seeds + 25  
                        outbound_writes.append((0xC80, (seeds_new).to_bytes(2, "little") , "EWRAM"))
                        #outbound_writes.append((0x1001, bytearray([0x01]), "EWRAM"))

                
                outbound_writes.append((RECV_IDX, (recv_index +1).to_bytes(2, "little") , "EWRAM"))


            # Handle Goal
            goalclear = False
            if marathon_place < 4 and self.game_goal ==1:
                goalclear = True
            elif 0x1C2306 in self.local_checked_locations and self.game_goal ==2:
                goalclear = True

            if not ctx.finished_game and goalclear == True:

                await ctx.send_msgs([{
                    "cmd": "StatusUpdate",
                    "status": ClientStatus.CLIENT_GOAL
                }])

            medal_array = recalculateMedals({
                "tennisprelim":tennis_prelim_flag,
                "tennis finals":tennis_finals_place,
                "volleyballprelim":volleyball_prelim_flag,
                "volleyball finals": volleyball_finals_place,
                "100hmdash":hamdash_place,
                "hurdles":hurdles_place,
                "sailing":sailing_place,
                "swimming":swim_place,
                "hammer":hammer_place,
                "polevault":polevault_place,
                "triple jump":triple_jump_place,
                "diving":diving_place,
                "carrot":carrot_place,
                "archery":archery_place,
                "bird back":birdback_place,
                "sync swim":sync_swim_place,
            })
            outbound_writes.append((0xF64, bytearray(medal_array), "EWRAM"))

            await bizhawk.write(ctx.bizhawk_ctx, outbound_writes)

        except bizhawk.RequestFailedError:
            # The connector didn't respond. Exit handler and return to main loop to reconnect
            pass
