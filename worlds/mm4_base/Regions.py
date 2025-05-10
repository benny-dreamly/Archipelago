from typing import Dict, List, NamedTuple


class MM4RegionData(NamedTuple):
    connecting_regions: List[str] = []

region_data_table: Dict[str, MM4RegionData] = {
    "Menu": MM4RegionData(["Example Region"]),
    "Example Region": MM4RegionData(["Example Region 2"]),
    "Example Region 2": MM4RegionData(["Goal Region"]),
    "Goal Region": MM4RegionData([]),
}

def get_exit(region, exit_name):
    for exit in region.exits:
        if exit.connected_region.name == exit_name:
            return exit