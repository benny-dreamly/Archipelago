import hashlib
import math
import os
import struct
import random

from settings import get_settings
import Utils
from worlds.Files import APProcedurePatch, APTokenMixin, APTokenTypes

from worlds.AutoWorld import World

NOP = bytearray([0x00,0x00,0x00,0x00])
MD5Hash = "ef2453bff7ad0c4bfa9ab0bd6324ebf3"

LEVEL_PATCH = [
    0x00,0x07,0x0E,0x00, 0x15,0x1C,0x23,0x00, 0x2A,0x31,0x38,0x00, 0x3F,0x46,0x4D,0x00,
    0x54,0x00,0x00,0x00, 0x05,0x07,0x04,0x00, 0x05,0x06,0x04,0x00, 0x05,0x07,0x05,0x00,
    0x04,0x05,0x05,0x00, 0x07,0x00,0x00,0x00, 0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00,
    0x3C,0x1C,0x80,0x13, 0x93,0x8E,0x48,0x01, 0x93,0x98,0x48,0x02, 0x3C,0x1C,0x80,0x05,
    0x23,0x9C,0xCC,0xD0, 0x00,0x0E,0x70,0x80, 0x03,0x8E,0xE0,0x20, 0x03,0x98,0xE0,0x20,
    0x93,0x98,0x00,0x00, 0x93,0x8E,0x00,0x14, 0x03,0x80,0xE0,0x24, 0x3C,0x1C,0x80,0x13,
    0x23,0x9C,0x48,0x08, 0x03,0x98,0xE0,0x20, 0x03,0x00,0xC0,0x24, 0x00,0x00,0x00,0x00,
    0x93,0x88,0x00,0x00, 0x21,0xCE,0xFF,0xFF, 0x1D,0x00,0x00,0x08, 0x00,0x00,0x00,0x00,
    0x11,0xC0,0x00,0x0F, 0x00,0x00,0x00,0x00, 0x23,0x18,0x00,0x01, 0x23,0x9C,0x00,0x01,
    0x10,0x00,0xFF,0xF7, 0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00, 0x03,0x80,0xE0,0x24,
    0x3C,0x1C,0x80,0x13, 0x23,0x9C,0x48,0x03, 0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00,
    0xA3,0x98,0x00,0x00, 0x03,0x80,0xE0,0x24, 0x08,0x0C,0xD5,0x2C, 0x00,0x00,0x00,0x00,
    0x03,0x00,0xC0,0x24, 0x03,0x80,0xE0,0x24, 0x3C,0x1C,0x80,0x13, 0x23,0x9C,0x48,0x00,
    0xA3,0x80,0x00,0x01, 0xA3,0x80,0x00,0x02, 0xA3,0x80,0x00,0x03, 0x03,0x80,0xE0,0x24,
    0x08,0x0C,0xD5,0x2C
]

STG_SEL_OVLAY_PATCH = [
    0x03,0x19,0x38,0x21, # ADDU	A3, T8, T9
    0x00,0x00,0x28,0x25, # OR	A1, R0, R0
    0x29,0x09,0x00,0x06, # SLTI	T1, T0, 0x0006
    0x1D,0x20,0x00,0x03, # BGTZ	T1, 0x8004CDEC
    0x00,0x00,0x00,0x00, # NOP
    0x3C,0x07,0x80,0x32, # LUI	A3, 0x8032
    0x24,0xE7,0x29,0x80, # ADDIU	A3, A3, 0x2980
    0x08,0x0C,0xCF,0x31, # J	0x80333CC4
]

GEM_CHECK_PATCH =[
    0x3C,0x18,0x80,0x41, # LUI	T8, 0x8041
    0x83,0x0D,0x00,0x00, # LB	T5, 0x0000 (T8)
    0x3C,0x01,0x80,0x05, # LUI	AT, 0x8005
    0x25,0xAE,0x00,0x01, # ADDIU	T6, T5, 0x0001
    0xA3,0x0E,0x00,0x00, # SB	T6, 0x7499 (T8)
]

class BombHProcedurePatch(APProcedurePatch, APTokenMixin):
    game = "Bomberman Hero"
    hash = MD5Hash
    patch_file_ending = ".apbombh"
    result_file_ending = ".z64"
    #name: str = ""

    @classmethod
    def get_source_data(cls) -> bytes:
        return get_base_rom_bytes()
    
def write_tokens(world:World, patch:BombHProcedurePatch):
    # Write Rom name
    for j, b in enumerate(world.romName):
        patch.write_token(APTokenTypes.WRITE, 0xB864E0 + j, struct.pack("<B", b))
    for j, b in enumerate(world.playerName):
        patch.write_token(APTokenTypes.WRITE, 0xB86500 + j, struct.pack("<B", b))

    item_powers = 0
    if world.options.item_powerups:
        item_powers += 1
    if world.options.item_health:
        item_powers += 2
        # Do not gain extra health
    #    patch.write_token(APTokenTypes.WRITE,0x239F4,NOP)
    # write game options
    patch.write_token(APTokenTypes.WRITE,0xB864D0,bytearray([world.options.adok_bombs.value]))
    patch.write_token(APTokenTypes.WRITE,0xB864D1,bytearray([world.options.game_goal.value]))
    if world.options.death_link:
        patch.write_token(APTokenTypes.WRITE,0xB864D2,bytearray([0x01]))
    if world.options.random_sounds:
        patch.write_token(APTokenTypes.WRITE,0xB864D3,bytearray([0x01]))
    if world.options.random_sky:
        patch.write_token(APTokenTypes.WRITE,0xB864D4,bytearray([0x01]))
    if world.options.random_music:
        patch.write_token(APTokenTypes.WRITE,0xB864D5,bytearray([0x01]))
    patch.write_token(APTokenTypes.WRITE,0xB864D6,bytearray([world.options.clear_points.value]))
    #if world.options.item_powerups:
    patch.write_token(APTokenTypes.WRITE,0xB864D7,bytearray([item_powers]))
    #if world.options.item_powerups:
    #    patch.write_token(APTokenTypes.WRITE,0xB864D7,bytearray([0x01]))
    if world.options.radio:
        patch.write_token(APTokenTypes.WRITE,0xB864D8,bytearray([0x01]))
    patch.write_token(APTokenTypes.WRITE,0xB864D9,bytearray([world.options.stage_total.value]))

    # Bypass CIC
    patch.write_token(APTokenTypes.WRITE, 0x66C, NOP)
    patch.write_token(APTokenTypes.WRITE, 0x678, NOP)
    
    # Do not unlock stages
    patch.write_token(APTokenTypes.WRITE, 0x5C87C, NOP)

    if world.options.item_powerups:
        # Do Gain Bomb up
        patch.write_token(APTokenTypes.WRITE, 0x23800, NOP)
        # Do Gain Fire up
        patch.write_token(APTokenTypes.WRITE, 0x2385C, NOP)
        # Do not get Bomb Vest
        patch.write_token(APTokenTypes.WRITE, 0x23E78,NOP)

    #Death Link
    patch.write_token(APTokenTypes.WRITE, 0x24978,bytearray([0x3C,0x1C,0x80,0x16])) # LUI	GP, 0x8016 {80023D78}
    patch.write_token(APTokenTypes.WRITE, 0x24984,bytearray([0xA3,0x80,0x52,0x44])) # SB	R0, 0x5244 (GP) [0x80165240]
    patch.write_token(APTokenTypes.WRITE, 0x2499C,bytearray([0x00,0x1C,0xE0,0x24])) # AND	GP, R0, GP

    # Do not reset stage progress to first stage
    patch.write_token(APTokenTypes.WRITE, 0x25F3C,NOP)

    # Move between worlds
    patch.write_token(APTokenTypes.WRITE, 0x5257C, bytearray([0x10,0x00,0x00,0x04])) # B 0x80060070
    patch.write_token(APTokenTypes.WRITE, 0x52594, bytearray([0x34,0x02]))
    
    
    # Do not Advance to next level
    patch.write_token(APTokenTypes.WRITE, 0x5C548, NOP)
    patch.write_token(APTokenTypes.WRITE, 0x5C560, NOP)

    patch.write_token(APTokenTypes.WRITE, 0x25F24, NOP)
    patch.write_token(APTokenTypes.WRITE, 0x5C530, NOP)
    patch.write_token(APTokenTypes.WRITE, 0x25F0C, NOP)

    # Change Adok Display
    patch.write_token(APTokenTypes.WRITE, 0x6261B, bytearray([world.options.adok_bombs.value]))
    patch.write_token(APTokenTypes.WRITE, 0x625C0, bytearray([0x80,0x64,0x03,0x24]))

    # Jump to Stage Code; J 0x8004CCD0, NOP; return to 0x803354B0
    patch.write_token(APTokenTypes.WRITE, 0x1519EC, bytearray([0x08,0x01,0x33,0x40, 0x00,0x00,0x00,0x00]))

    # Patch in Stage Code
    patch.write_token(APTokenTypes.WRITE, 0x4D8D0, bytearray(LEVEL_PATCH))

    # Patch in gem patch 0x00023A6C
    patch.write_token(APTokenTypes.WRITE, 0x239A7, bytearray([world.options.needed_gem.value])) # SLTI	AT, T3, 0x00XX
    patch.write_token(APTokenTypes.WRITE, 0x23A6C, bytearray([0xA0,0x20,0x52,0x41])) # SB	R0, 0x5241 (AT)
    patch.write_token(APTokenTypes.WRITE, 0x239E4, bytearray(GEM_CHECK_PATCH))
    

    # Jump to Stage Code; J 0x8004CDD0, NOP; return to 0x80333CC4
    patch.write_token(APTokenTypes.WRITE, 0x1501FC, bytearray([0x08,0x01,0x33,0x74, 0x00,0x00,0x00,0x00]))
    patch.write_token(APTokenTypes.WRITE, 0x14FF8B, bytearray([0x07])) # Do not change the clear point overlay to 0

    patch.write_token(APTokenTypes.WRITE, 0x4D9D0, bytearray(STG_SEL_OVLAY_PATCH))
    # Write patch file
    patch.write_file("token_data.bin", patch.get_token_binary())

def get_base_rom_bytes(file_name: str ="") -> bytes:
    base_rom_bytes = getattr(get_base_rom_bytes, "base_rom_bytes", None)
    if not base_rom_bytes:
        file_name = get_base_rom_path(file_name)
        base_rom_bytes = bytes(Utils.read_snes_rom(open(file_name, "rb")))

        basemd5 = hashlib.md5()
        basemd5.update(base_rom_bytes)
        md5hash = basemd5.hexdigest()
        if MD5Hash !=md5hash:
            raise Exception("Supplied Rom does not match known MD5 for Bobmerman Hero")
        get_base_rom_bytes.base_rom_bytes = base_rom_bytes
    return base_rom_bytes

def get_base_rom_path(file_name: str="")-> str:
    if not file_name:
        file_name = get_settings().bombermanhero_settings.rom_file
    if not os.path.exists(file_name):
        file_name= Utils.user_path(file_name)
    return file_name