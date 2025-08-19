from .Locations import HamGamesLocationData
from typing import Dict

loc_talk_data_table: Dict[str, HamGamesLocationData] = {
    "Day 1 Clubhouse - Dexter": HamGamesLocationData(
        region="Day 1 - Clubhouse",
        address=0x1C2400,
        rom_offset= 0x08E94BD8
    ),
}

talk_location_table = {name: data.address for name, data in loc_talk_data_table.items() if data.address is not None}
talk_location_data = {data.rom_offset: data.address for name, data in loc_talk_data_table.items() if data.rom_offset is not None}