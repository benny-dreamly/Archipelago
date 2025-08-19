from typing import Dict, List, NamedTuple


class Smash64RegionData(NamedTuple):
    connecting_regions: List[str] = []

region_data_table: Dict[str, Smash64RegionData] = {
    "Menu": Smash64RegionData(["Example Region"]),
    "Example Region": Smash64RegionData(["Example Region 2"]),
    "Example Region 2": Smash64RegionData(["Goal Region"]),
    "Goal Region": Smash64RegionData([]),
}

def get_exit(region, exit_name):
    for exit in region.exits:
        if exit.connected_region.name == exit_name:
            return exit