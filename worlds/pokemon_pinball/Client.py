
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

RECV_IDX = 0x00

class PokePinballClient(BizHawkClient):
    game = "Pokemon Pinball"
    system = "GBC"
    patch_suffix = ".apokepinball"
    local_checked_locations: Set[int]
    rom_slot_name: Optional[str]

    death_link: bool = False
    sending_death_link: bool = True
    pending_death_link: bool = False

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
        await ctx.send_death("A pinball was lost.")

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
                    (0x1400, 0x200, "WRAM"), # 0 Game RAM
                    (0x1962, 0x96, "WRAM"), # 1 Pokedex Data
                    (0x18F1, 0x1, "WRAM"), # 2 Game State
                    (RECV_IDX, 0x1, "RDRAM"), # 3 Recv Index
                ]
            )
            outbound_writes = []
            game_data = ram_data[0]
            pokedex_data = ram_data[1]
            game_state = ram_data[2][0]
            recv_index = ram_data[3][0]

            if self.death_link:
                await ctx.update_death_link(self.death_link)

            if self.pending_death_link:
                ## Handle deathlink
                self.pending_death_link = False
                self.sending_death_link = True

            locs_to_send = set()

            goalclear = False
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