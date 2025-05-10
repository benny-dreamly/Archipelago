
from typing import TYPE_CHECKING, Set, Optional, Dict, Any
import logging
from NetUtils import ClientStatus
#Test comment
from base64 import b64encode
import worlds._bizhawk as bizhawk
from worlds._bizhawk.client import BizHawkClient

import time
import random

logger = logging.getLogger("Client")

if TYPE_CHECKING:
    from worlds._bizhawk.context import BizHawkClientContext

RECV_IDX = 0x1000
RECV_PORT = 0x1AF0

class MM4Client(BizHawkClient):
    game = "Mega Man 4"
    system = "NES"
    patch_suffix = ".apmm4"
    local_checked_locations: Set[int]
    rom_slot_name: Optional[str]

    death_link: bool = False
    game_goal = 0
    sending_death_link: bool = True
    pending_death_link: bool = False


    #needed_mons = b''

    def __init__(self) -> None:
        super().__init__()
        self.local_checked_locations = set()
        self.rom_slot_name = None
        self.game_state = False
        self.research_command = None

    async def validate_rom(self, ctx: "BizHawkClientContext") -> bool:
        from CommonClient import logger
        from .Rom import ROM_NAME_ADR, PLAYER_NAME_ADR, OPTION_ADR
        rom_data = await bizhawk.read(
            ctx.bizhawk_ctx,
            [
            (ROM_NAME_ADR-0x10, 0x3, "PRG ROM"), # 0 Rom Name
            (OPTION_ADR-0x10, 0x10, "PRG ROM"), # 1 Options
            (PLAYER_NAME_ADR-0x10, 0x32, "PRG ROM"), # 2 Player Name
            (ROM_NAME_ADR-0x10, 0x20, "PRG ROM"), # 3 Slot Data
            ]
        )
        try:
            rom_name = (rom_data[0]).decode("ascii")
            if rom_name != "MM4":
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
        await ctx.send_death("Megaman Died.")

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
                    (0x1400, 0x100, "RAM"), # 0 Game RAM
                    (RECV_IDX, 0x1, "WRAM"), # Recv Index
                    (0x1500, 0x100, "RAM"), # 2 Game Flags
                ]
            )
            outbound_writes = []
            game_data = ram_data[0]
            recv_index = ram_data[1][0]
            game_flags = ram_data[2]


            if game_data[0x10] == 0xF0:
                # Make sure you are in a pinball game
                return
            self.game_state = True
            if recv_index == 0xFF:
                outbound_writes.append((RECV_IDX, bytearray([0x00]), "WRAM"))
            
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

            for val in game_flags:
                flag_idx = 0
                if val != 0x00:
                    loc_id = 0x40001 + flag_idx
                    if loc_id not in self.local_checked_locations:
                        locs_to_send.add(loc_id)
                flag_idx += 1
                # Score

            if locs_to_send != self.local_checked_locations:
                self.local_checked_locations = locs_to_send
                if locs_to_send is not None:
                    await ctx.send_msgs([{"cmd": "LocationChecks", "locations": list(locs_to_send)}])

            # Handle Items
                # Permanent Items

            
            for item in range(len(ctx.items_received)):
                raw_item = ctx.items_received[item].item
                match raw_item:
                    case 0x40001: # Example Item 1
                        outbound_writes.append((0x1000, bytearray([0x01]), "WRAM"))


                # Temp Items
            if (len(ctx.items_received) > recv_index):
                raw_item = ctx.items_received[recv_index].item
                #item_name = ctx.items_received[recv_index].player
                #logger.warning(f"{ctx.items_received[recv_index]}")
                match raw_item:
                    case 0x40002:   # Example Item 2
                        outbound_writes.append((0x1001, bytearray([0x01]), "WRAM"))

                outbound_writes.append((RECV_IDX, (recv_index +1).to_bytes(1, "little") , "WRAM"))


            # Handle Goal
            goalclear = False
            #all_needed_mons = False
            #score_clear = False
            if not ctx.finished_game and goalclear == True:

                await ctx.send_msgs([{
                    "cmd": "StatusUpdate",
                    "status": ClientStatus.CLIENT_GOAL
                }])

            await bizhawk.write(ctx.bizhawk_ctx, outbound_writes)

        except bizhawk.RequestFailedError:
            # The connector didn't respond. Exit handler and return to main loop to reconnect
            pass
