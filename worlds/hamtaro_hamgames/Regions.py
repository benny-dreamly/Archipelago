from typing import Dict, List, NamedTuple


class HamGamesRegionData(NamedTuple):
    connecting_regions: List[str] = []

region_data_table: Dict[str, HamGamesRegionData] = {
    "Menu": HamGamesRegionData(["Day 1","Day 2","Day 3","Day 4","Day 5","Day 6","Day 7","Hamigo","TV Shop","Fortune Teller"]),
    "Day 1": HamGamesRegionData(["Day 1 - Clubhouse","Day 1 - Studio","Day 1 - Beach","Day 1 - Tennis","Day 1 - Village","Day 1 - Pool","Day 1 - Stadium","Day 1 - Lawn"]),
    "Day 2": HamGamesRegionData(["Day 2 - Clubhouse","Day 2 - Studio","Day 2 - Beach","Day 2 - Tennis","Day 2 - Village","Day 2 - Pool","Day 2 - Stadium","Day 2 - Lawn"]),
    "Day 3": HamGamesRegionData(["Day 3 - Clubhouse","Day 3 - Studio","Day 3 - Beach","Day 3 - Tennis","Day 3 - Village","Day 3 - Pool","Day 3 - Stadium","Day 3 - Lawn"]),
    "Day 4": HamGamesRegionData(["Day 4 - Clubhouse","Day 4 - Studio","Day 4 - Beach","Day 4 - Tennis","Day 4 - Village","Day 4 - Pool","Day 4 - Stadium","Day 4 - Lawn"]),
    "Day 5": HamGamesRegionData(["Day 5 - Clubhouse","Day 5 - Studio","Day 5 - Beach","Day 5 - Tennis","Day 5 - Village","Day 5 - Pool","Day 5 - Stadium","Day 5 - Lawn"]),
    "Day 6": HamGamesRegionData(["Day 6 - Clubhouse","Day 6 - Studio","Day 6 - Beach","Day 6 - Tennis","Day 6 - Village","Day 6 - Pool","Day 6 - Stadium","Day 6 - Lawn"]),
    "Day 7": HamGamesRegionData(["Day 7 - Clubhouse","Day 7 - Studio","Day 7 - Beach","Day 7 - Tennis","Day 7 - Village","Day 7 - Pool","Day 7 - Stadium","Day 7 - Lawn"]),
    "Hamigo": HamGamesRegionData(),
    "TV Shop": HamGamesRegionData(["TV Shop Latenight"]),
    "TV Shop Latenight": HamGamesRegionData(),
    "Fortune Teller": HamGamesRegionData(),

    "Day 1 - Clubhouse": HamGamesRegionData(),
    "Day 1 - Studio": HamGamesRegionData(),
    "Day 1 - Beach": HamGamesRegionData(),
    "Day 1 - Tennis": HamGamesRegionData(),
    "Day 1 - Village": HamGamesRegionData(),
    "Day 1 - Pool": HamGamesRegionData(),
    "Day 1 - Stadium": HamGamesRegionData(),
    "Day 1 - Lawn": HamGamesRegionData(),

    "Day 2 - Clubhouse": HamGamesRegionData(),
    "Day 2 - Studio": HamGamesRegionData(),
    "Day 2 - Beach": HamGamesRegionData(),
    "Day 2 - Tennis": HamGamesRegionData(),
    "Day 2 - Village": HamGamesRegionData(),
    "Day 2 - Pool": HamGamesRegionData(),
    "Day 2 - Stadium": HamGamesRegionData(),
    "Day 2 - Lawn": HamGamesRegionData(),

    "Day 3 - Clubhouse": HamGamesRegionData(),
    "Day 3 - Studio": HamGamesRegionData(),
    "Day 3 - Beach": HamGamesRegionData(),
    "Day 3 - Tennis": HamGamesRegionData(),
    "Day 3 - Village": HamGamesRegionData(),
    "Day 3 - Pool": HamGamesRegionData(),
    "Day 3 - Stadium": HamGamesRegionData(),
    "Day 3 - Lawn": HamGamesRegionData(),

    "Day 4 - Clubhouse": HamGamesRegionData(),
    "Day 4 - Studio": HamGamesRegionData(),
    "Day 4 - Beach": HamGamesRegionData(),
    "Day 4 - Tennis": HamGamesRegionData(),
    "Day 4 - Village": HamGamesRegionData(),
    "Day 4 - Pool": HamGamesRegionData(),
    "Day 4 - Stadium": HamGamesRegionData(),
    "Day 4 - Lawn": HamGamesRegionData(),

    "Day 5 - Clubhouse": HamGamesRegionData(),
    "Day 5 - Studio": HamGamesRegionData(),
    "Day 5 - Beach": HamGamesRegionData(),
    "Day 5 - Tennis": HamGamesRegionData(),
    "Day 5 - Village": HamGamesRegionData(),
    "Day 5 - Pool": HamGamesRegionData(),
    "Day 5 - Stadium": HamGamesRegionData(),
    "Day 5 - Lawn": HamGamesRegionData(),

    "Day 6 - Clubhouse": HamGamesRegionData(),
    "Day 6 - Studio": HamGamesRegionData(),
    "Day 6 - Beach": HamGamesRegionData(),
    "Day 6 - Tennis": HamGamesRegionData(),
    "Day 6 - Village": HamGamesRegionData(),
    "Day 6 - Pool": HamGamesRegionData(),
    "Day 6 - Stadium": HamGamesRegionData(),
    "Day 6 - Lawn": HamGamesRegionData(),

    "Day 7 - Clubhouse": HamGamesRegionData(),
    "Day 7 - Studio": HamGamesRegionData(),
    "Day 7 - Beach": HamGamesRegionData(),
    "Day 7 - Tennis": HamGamesRegionData(),
    "Day 7 - Village": HamGamesRegionData(),
    "Day 7 - Pool": HamGamesRegionData(),
    "Day 7 - Stadium": HamGamesRegionData(),
    "Day 7 - Lawn": HamGamesRegionData(),
}

def get_exit(region, exit_name):
    for exit in region.exits:
        if exit.connected_region.name == exit_name:
            return exit