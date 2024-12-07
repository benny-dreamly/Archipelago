from __future__ import annotations
from pathlib import Path
import os
import json
import platform
import logging
import Utils
from NetUtils import NetworkItem, ClientStatus
from CommonClient import gui_enabled, logger, get_base_parser, ClientCommandProcessor, \
    CommonContext, server_loop

import ModuleUpdate
ModuleUpdate.update()

logger = logging.getLogger("Client")

if __name__ == "__main__":
    Utils.init_logging("AODClient", exception_logger="Client")


class AODClientCommandProcessor(ClientCommandProcessor):
    def __init__(self, ctx):
        super().__init__(ctx)

class AODContext(CommonContext):
    command_processor: int = AODClientCommandProcessor
    game = "Adventures of Dreamland"
    items_handling = 0b111 # full remote

    def __init__(self, server_address, password):
        super(AODContext, self).__init__(server_address, password)
        self.send_index: int = 0
        self.syncing = False
        self.awaiting_bridge = False
        # self.game_save_file_path: AOD's save file path
        system = platform.system
        if system == "Windows":
            self.game_save_file_path = Path(os.getenv('LOCALAPPDATA')) / "adventuresofdreamland" / "saves"
        else:
            self.game_save_file_path = Path.home() / ".local" / "share" / "adventuresofdreamland" / "saves"

    async def server_auth(self, password_requested: bool = False):
        if password_requested and not self.password:
            await super(AODContext, self).server_auth(password_requested)
        await self.get_username()
        await self.send_connect()
