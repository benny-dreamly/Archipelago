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
from .rom_data import *
from .com_ap_methods import shuffle_dict, ramdomize_table_with_exclude
from .text_rando import dialog_map

MD5Hash = [
    "9eecb3d524fe8bc2362b3f0b1045f4ab", # GBA cartridge
]

ROM_DATA_FREESPACE = 0xFE8000
GAME_NAME_ADR = 0xA0
ROM_NAME_ADR = ROM_DATA_FREESPACE + 0x10
PLAYER_NAME_ADR = ROM_DATA_FREESPACE + 0x30
OPTION_ADR = ROM_DATA_FREESPACE

NOP = bytearray([0x00, 0x00])  # LSL R0, R0 #00 (NOP)

class HamGamesProcedurePatch(APProcedurePatch, APTokenMixin):
    game = "Hamtaro Hamham Games"
    hash = MD5Hash
    patch_file_ending = ".aphamgames"
    result_file_ending = ".gba"

    @classmethod
    def get_source_data(cls) -> bytes:
        return get_base_rom_bytes()
    
def write_tokens(world:World, patch:HamGamesProcedurePatch):
    
    for j, b in enumerate(world.romName):
        patch.write_token(APTokenTypes.WRITE, ROM_NAME_ADR + j, struct.pack("<B", b))
    for j, b in enumerate(world.playerName):
        patch.write_token(APTokenTypes.WRITE, PLAYER_NAME_ADR + j, struct.pack("<B", b))
    patch.write_token(APTokenTypes.WRITE, OPTION_ADR + 0x0, bytearray([world.options.game_goal.value]))
    patch.write_token(APTokenTypes.WRITE, OPTION_ADR + 0x1, bytearray([world.options.death_link.value]))
    patch.write_token(APTokenTypes.WRITE, OPTION_ADR + 0x2, bytearray([world.options.seedsanity.value]))
    patch.write_token(APTokenTypes.WRITE, OPTION_ADR + 0x3, bytearray([world.options.needed_medals.value]))
    patch.write_token(APTokenTypes.WRITE, OPTION_ADR + 0x4, bytearray([world.options.needed_nomination.value]))
    patch.write_token(APTokenTypes.WRITE, OPTION_ADR + 0x5, bytearray([world.options.costumesanity.value]))

    if world.options.random_text:
        shuffled_dialog = shuffle_dict(dialog_map)
        for rom_adr, talk_data_bytes in shuffled_dialog.items():
            patch.write_token(APTokenTypes.WRITE, (rom_adr - 0x8000000), talk_data_bytes.to_bytes(4, byteorder='little'))
            
 
    # Don't advance time
    #patch.write_token(APTokenTypes.WRITE, 0xD07F8, bytearray([0x50,0xD0,0x0F,0x08])) # Sleep Day Time ADvance Pointer
    #patch.write_token(APTokenTypes.WRITE, 0xFD050, bytearray([0x1E,0xFF,0x2F,0xE1])) # BX LR
    patch.write_token(APTokenTypes.WRITE, 0x3292, NOP) # Don't advance day on sleep
    patch.write_token(APTokenTypes.WRITE, 0x3322, NOP) # Bypass check for change in day
    
    # Shedule Routine
    patch.write_token(APTokenTypes.WRITE, 0x23126, bytearray([0xD9,0xF0,0xCB,0xFF])) # bl $0x80FD0C0
    patch.write_token(APTokenTypes.WRITE, 0xFD0C0, CLEAR_FIELD_FLAGS)
    patch.write_token(APTokenTypes.WRITE, 0xFD000, TIME_SELECT)
    
    # Disable Boss flag
    patch.write_token(APTokenTypes.WRITE, 0xF1D660, bytearray([0xF0, 0x03]))
    patch.write_token(APTokenTypes.WRITE, 0xE7A164, bytearray([0xF0, 0x03]))

    # Speed up text
    patch.write_token(APTokenTypes.WRITE, 0x1116A, NOP)
    patch.write_token(APTokenTypes.WRITE, 0x1115A, NOP)

    # Lock Map Movement By Default
    patch.write_token(APTokenTypes.WRITE, 0xCCE5A4, bytearray([
        0x40,0x00,0x0A,0x0A, 0x10,0x00,0x0A,0x0A, 0x80,0x00,0x0A,0x0A, 0x10,0x00,0x0B,0x0B,
        0x80,0x00,0x0B,0x0B, 0x20,0x00,0x0B,0x0B, 0x40,0x00,0x0C,0x0C, 0x80,0x00,0x0C,0x0C,
        0x20,0x00,0x0C,0x0C, 0x10,0x00,0x0C,0x0C, 0x80,0x00,0x0D,0x0D, 0x20,0x00,0x0D,0x0D,
        0x10,0x00,0x0D,0x0D, 0x80,0x00,0x0E,0x0E, 0x20,0x00,0x0E,0x0E, 0x40,0x00,0x0F,0x0F,
        0x80,0x00,0x0F,0x0F, 0x20,0x00,0x0F,0x0F, 0x40,0x00,0x10,0x10, 0x20,0x00,0x10,0x10,
        0x10,0x00,0x10,0x10, 0x40,0x00,0x11,0x11, 0x20,0x00,0x11,0x11, 0x10,0x00,0x11,0x11,
    ]))

    # Fortune 
    fortune_bytes = [
        0xA5,0x03, 0xA5,0x03, 0xA7,0x03, 0xAA,0x03, 0xA9,0x03, 0xAA,0x03, 0x80,0x80, 0x06,0x00,
        0x00,0x00, 0x88,0x18, 0xAB,0x03, 0xAC,0x03, 0xAD,0x03, 0xAE,0x03, 0xAF,0x03, 0xB0,0x03,
        0xB1,0x03, 0xB2,0x03, 0xB3,0x03, 0xB4,0x03, 0xB5,0x03, 0xB6,0x03, 0xB7,0x03
    ]
    fortune_area = world.fortune_area
    for x in range(0x14,0x2D,2):
        fortune_bytes[x] = fortune_area
    patch.write_token(APTokenTypes.WRITE, 0xE79D58, bytearray(fortune_bytes))
    # Arcade Check
    #patch.write_token(APTokenTypes.WRITE, 0x2770, ARCADE_ADJUST) 
    #patch.write_token(APTokenTypes.WRITE, 0x27CA8, bytearray([0x08,0x80,0x00,0x02])) #EWRAM 8008
    
    # Normal Ending
    patch.write_token(APTokenTypes.WRITE, 0xE87B84, bytearray([0x78,0x02])) # Change ending flag check

    # 
    patch.write_token(APTokenTypes.WRITE, 0xEA00A4, bytearray([0x48,0x08])) # Change shop costume set flag


    # Record dialog address
    patch.write_token(APTokenTypes.WRITE, 0xF508, bytearray([0xED,0xF0,0xBA,0xFD])) # bl ap_recordDialogAddress
    patch.write_token(APTokenTypes.WRITE, 0x1049A, bytearray([0xEC,0xF0,0xF1,0xFD])) # bl ap_recordDialogAddress
    patch.write_token(APTokenTypes.WRITE, 0xFD080, RECORD_DIALOG_OFFSET)

    # Movement speed
    patch.write_token(APTokenTypes.WRITE, 0x146AE, world.options.move_speed.value.to_bytes(1, 'little'))
    
    # Randomize Sounds
    if world.options.random_sound:
        sound_random_table = SOUND_TBL
        sound_random_table =  ramdomize_table_with_exclude(sound_random_table,0x4,[0x00])
        patch.write_token(APTokenTypes.WRITE, 0xDEE00, sound_random_table)
    if world.options.random_sound:
        music_random_table = MUSIC_TBL
        music_random_table =  ramdomize_table_with_exclude(music_random_table,0x4,[0x00,0x07,0x09, 0x0B, 0x0C,0xD,0x0E,0x0F,0x2A])
        patch.write_token(APTokenTypes.WRITE, 0xDED20, music_random_table)

    # Write Patch Token data
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
            raise Exception("Supplied Rom does not match known MD5 for Hamtaro Hamham Games")
        get_base_rom_bytes.base_rom_bytes = base_rom_bytes
    return base_rom_bytes

def get_base_rom_path(file_name: str="")-> str:
    if not file_name:
        file_name = get_settings().hamgames_settings.rom_file
    if not os.path.exists(file_name):
        file_name= Utils.user_path(file_name)
    return file_name