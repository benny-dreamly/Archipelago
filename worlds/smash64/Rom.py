import hashlib
import math
import os
import struct
import random

from settings import get_settings
import Utils
from worlds.Files import APProcedurePatch, APTokenMixin, APTokenTypes

from worlds.AutoWorld import World

from .Rom_routines import *

MD5Hash = [
    "f7c52568a31aadf26e14dc2b6416b2ed", # N64 cartridge
]

ROM_DATA_FREESPACE = 0xF60000
ROM_NAME_ADR = ROM_DATA_FREESPACE + 0x10
PLAYER_NAME_ADR = ROM_DATA_FREESPACE + 0x30
OPTION_ADR = ROM_DATA_FREESPACE

NOP = bytearray([0x00,0x00,0x00,0x00])

class Smash64ProcedurePatch(APProcedurePatch, APTokenMixin):
    game = "Smash 64"
    hash = MD5Hash
    patch_file_ending = ".apsmash64"
    result_file_ending = ".z64"

    @classmethod
    def get_source_data(cls) -> bytes:
        return get_base_rom_bytes()
    
def write_tokens(world:World, patch:Smash64ProcedurePatch):
    for j, b in enumerate(world.romName):
        patch.write_token(APTokenTypes.WRITE, ROM_NAME_ADR + j, struct.pack("<B", b))
    for j, b in enumerate(world.playerName):
        patch.write_token(APTokenTypes.WRITE, PLAYER_NAME_ADR + j, struct.pack("<B", b))
    patch.write_token(APTokenTypes.WRITE, OPTION_ADR + 0x0, bytearray([world.options.game_goal.value]))
    patch.write_token(APTokenTypes.WRITE, OPTION_ADR + 0x1, bytearray([world.options.death_link.value]))
    
    if world.options.death_link:
        patch.write_token(APTokenTypes.WRITE, OPTION_ADR + 0x2, bytearray([0x01]))

    # Bypass CIC
    patch.write_token(APTokenTypes.WRITE, 0x63C, bytearray([0x3C,0x1C,0x80,0x0A])) # LUI GP, 0x800A
    patch.write_token(APTokenTypes.WRITE, 0x648, NOP)

    # Locking Character Select
    patch.write_token(APTokenTypes.WRITE, 0x13A8C8, CHAR_SEL) # Classic Mode
    patch.write_token(APTokenTypes.WRITE, 0x1482EC, CHAR_SEL) # Bonus

    # Progressive Difficulty
    patch.write_token(APTokenTypes.WRITE, 0x13EA6C, bytearray([0x01,0xDC,0x08,0x2A])) # SLT	AT, T6, GP
    patch.write_token(APTokenTypes.WRITE, 0x13E8EC, bytearray([0x83,0x9C,0x00,0x40])) # LB	GP, 0x0040 (GP)

    # Lock Classic Continue
    patch.write_token(APTokenTypes.WRITE, 0x17A7E8, bytearray([0x10, 0x00, 0x00, 0x0C])) # B	0x80133DBC
    patch.write_token(APTokenTypes.WRITE, 0x17A3CC, bytearray([0x24,0x19,0x00,0x01])) # 8013396C    ADDIU	T9, R0, 0x0001
    patch.write_token(APTokenTypes.WRITE, 0x17A3D4, bytearray([0xAC,0x39,0x43,0x38])) # 80133974    SW	T9, 0x4338 (AT)

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
            raise Exception("Supplied Rom does not match known MD5 for Smash 64")
        get_base_rom_bytes.base_rom_bytes = base_rom_bytes
    return base_rom_bytes

def get_base_rom_path(file_name: str="")-> str:
    if not file_name:
        file_name = get_settings().smash64_settings.rom_file
    if not os.path.exists(file_name):
        file_name= Utils.user_path(file_name)
    return file_name