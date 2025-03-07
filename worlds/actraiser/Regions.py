from typing import NamedTuple, Callable, List, Dict
from BaseClasses import CollectionState


class ActraiserRegionData(NamedTuple):
    connecting_regions: List[str] = []

region_data_table: Dict[str, ActraiserRegionData] = {
    "Menu": ActraiserRegionData(["Sky"]),
    "Sky": ActraiserRegionData(["Fillmore Forest", "Bloodpool Bridge","Kasandora Desert","Aitos Mountain","Marahna Swamp","Northwall Cave","Death Heim"]),

    "Fillmore Forest":ActraiserRegionData(["Fillmore"]),
    "Fillmore": ActraiserRegionData(["Fillmore Chasm"]),
    "Fillmore Chasm": ActraiserRegionData([]),

    "Bloodpool Bridge": ActraiserRegionData(["Bloodpool"]),
    "Bloodpool": ActraiserRegionData(["Bloodpool Castle"]),
    "Bloodpool Castle": ActraiserRegionData([]),

    "Kasandora Desert": ActraiserRegionData(["Kasandora"]),
    "Kasandora": ActraiserRegionData(["Kasandora Pyramid"]),
    "Kasandora Pyramid": ActraiserRegionData([]),

    "Aitos Mountain": ActraiserRegionData(["Aitos"]),
    "Aitos": ActraiserRegionData(["Aitos Volcano"]),
    "Aitos Volcano": ActraiserRegionData([]),
    
    "Marahna Swamp": ActraiserRegionData(["Marahna"]),
    "Marahna": ActraiserRegionData(["Marahna Temple"]),
    "Marahna Temple": ActraiserRegionData([]),

    "Northwall Cave": ActraiserRegionData(["Northwall" ]),
    "Northwall": ActraiserRegionData(["Northwall Tree"]),
    "Northwall Tree": ActraiserRegionData([]),

    "Death Heim":ActraiserRegionData([])
}


def get_exit(region, exit_name):
    for exit in region.exits:
        if exit.connected_region.name == exit_name:
            return exit
