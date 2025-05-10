import hashlib
import math
import os
import struct
import random

from settings import get_settings
import Utils
from worlds.Files import APProcedurePatch, APTokenMixin, APTokenTypes

from worlds.AutoWorld import World

MD5Hash = [
    "7daebae488795835f962e875ee1f75e8", # NES cartridge
    "c03db5359fe7f6a052916ac1e84576e2", # NES cartridge (Rev 1)
    "96311ba196bb5ba1f59a2bd23215e76f", # Legacy Collection
    "ddc9559fc7b1540e4dd3023a242748f7", # Virtual Console
]

ROM_DATA_FREESPACE = 0x63900
ROM_NAME_ADR = ROM_DATA_FREESPACE + 0x10
PLAYER_NAME_ADR = ROM_DATA_FREESPACE + 0x30
OPTION_ADR = ROM_DATA_FREESPACE

class MM4ProcedurePatch(APProcedurePatch, APTokenMixin):
    game = "Mega Man 4"
    hash = MD5Hash
    patch_file_ending = ".apmm4"
    result_file_ending = ".nes"

    @classmethod
    def get_source_data(cls) -> bytes:
        return get_base_rom_bytes()
    
def write_tokens(world:World, patch:MM4ProcedurePatch):
    for j, b in enumerate(world.romName):
        patch.write_token(APTokenTypes.WRITE, ROM_NAME_ADR + j, struct.pack("<B", b))
    for j, b in enumerate(world.playerName):
        patch.write_token(APTokenTypes.WRITE, PLAYER_NAME_ADR + j, struct.pack("<B", b))
    patch.write_token(APTokenTypes.WRITE, OPTION_ADR + 0x0, bytearray([world.options.game_goal.value]))
    patch.write_token(APTokenTypes.WRITE, OPTION_ADR + 0x1, bytearray([world.options.death_link.value]))
    
    if world.options.death_link:
        patch.write_token(APTokenTypes.WRITE, OPTION_ADR + 0x2, bytearray([0x01]))
 

    patch.write_file("token_data.bin", patch.get_token_binary())

def get_base_rom_bytes(file_name: str ="") -> bytes:
    base_rom_bytes = getattr(get_base_rom_bytes, "base_rom_bytes", None)
    if not base_rom_bytes:
        file_name = get_base_rom_path(file_name)
        base_rom_bytes = bytes(Utils.read_snes_rom(open(file_name, "rb")))

        basemd5 = hashlib.md5()
        basemd5.update(base_rom_bytes)
        md5hash = basemd5.hexdigest()
        if md5hash not in MD5Hash:
            raise Exception("Supplied Rom does not match known MD5 for Mega Man 4")
        get_base_rom_bytes.base_rom_bytes = base_rom_bytes
    return base_rom_bytes

def get_base_rom_path(file_name: str="")-> str:
    if not file_name:
        file_name = get_settings().mm4_settings.rom_file
    if not os.path.exists(file_name):
        file_name= Utils.user_path(file_name)
    return file_name