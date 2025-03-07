from typing import Dict, List, NamedTuple


class BombHRegionData(NamedTuple):
    connecting_regions: List[str] = []


region_data_table: Dict[str, BombHRegionData] = {
    "Menu": BombHRegionData(["Planet Bomber","Primus","Kanatia","Mazone","Garaden"]),
    "Planet Bomber": BombHRegionData([
        "Battle Room",
        "Hyper Room",
        "Secret Room",
        "Heavy Room",
        "Sky Room",
        "Blue Cave",
        "Hole Lake",
        "Red Cave",
        "Big Cannon",
        "Dark Wood",
        "Dragon Road",
        "Vs Nitros Planet Bomber",
        "Clown Valley",
        "Great Rock",
        "Fog Route",
        "Vs Endol",
        ]),
    "Primus": BombHRegionData([
        "Groog Hills",
        "Bubble Hole",
        "Erars Lake",
        "Waterway",
        "Water Slider",
        "Rockn Road",
        "Water Pool",
        "Millian Road",
        "Warp Room",
        "Dark Prison",
        "Vs Nitros Primus",
        "Killer Gate",
        "Spiral Tower",
        "Snake Route",
        "Vs Baruda",
    ]),
    "Kanatia": BombHRegionData([
        "Hades Crater",
        "Magma Lake",
        "Magma Dam",
        "Crysta Hole",
        "Emerald Tube",
        "Death Temple",
        "Death Road",
        "Death Garden",
        "Float Zone",
        "Aqua Tank",
        "Aqua Way",
        "Vs Nitros Kanatia",
        "Hard Coaster",
        "Dark Maze",
        "Mad Coaster",
        "Move Stone",
        "Vs Bolban",
    ]),
    "Mazone": BombHRegionData([
        "Hopper Land",
        "Junfalls",
        "Freeze Lake",
        "Cool Cave",
        "Snowland",
        "Storm Valley",
        "Snow Circuit",
        "Heaven Sky",
        "Eye Snake",
        "Vs Nitros Mazone",
        "Air Room",
        "Zero G Room",
        "Mirror Room",
        "Vs Natia",
    ]),
    "Garaden": BombHRegionData([
        "Boss Room 1",
        "Boss Room 2",
        "Boss Room 3",
        "Boss Room 4",
        "Boss Room 5",
        "Boss Room 6",
        "Vs Bagular",
    ]),
    #"Gossick": BombHRegionData([
    #    "Outter Road",
    #    "Inner Road",
    #    "Vs Evil Bomber",
    #]),

    "Battle Room": BombHRegionData(),
    "Hyper Room": BombHRegionData(),
    "Secret Room": BombHRegionData(),
    "Heavy Room": BombHRegionData(),
    "Sky Room": BombHRegionData(),

    "Blue Cave": BombHRegionData(),
    "Hole Lake": BombHRegionData(),
    "Red Cave": BombHRegionData(),
    "Big Cannon": BombHRegionData(),
    "Dark Wood": BombHRegionData(),
    "Dragon Road": BombHRegionData(),
    "Vs Nitros Planet Bomber": BombHRegionData(),

    "Clown Valley": BombHRegionData(),
    "Great Rock": BombHRegionData(),
    "Fog Route": BombHRegionData(),
    "Vs Endol": BombHRegionData(),


    "Groog Hills": BombHRegionData(),
    "Bubble Hole": BombHRegionData(),
    "Erars Lake": BombHRegionData(),
    "Waterway": BombHRegionData(),
    "Water Slider": BombHRegionData(),

    "Rockn Road": BombHRegionData(),
    "Water Pool": BombHRegionData(),
    "Millian Road": BombHRegionData(),
    "Warp Room": BombHRegionData(),
    "Dark Prison": BombHRegionData(),
    "Vs Nitros Primus": BombHRegionData(),

    "Killer Gate": BombHRegionData(),
    "Spiral Tower": BombHRegionData(),
    "Snake Route": BombHRegionData(),
    "Vs Baruda": BombHRegionData(),


    "Hades Crater": BombHRegionData(),
    "Magma Lake": BombHRegionData(),
    "Magma Dam": BombHRegionData(),
    "Crysta Hole": BombHRegionData(),
    "Emerald Tube": BombHRegionData(),

    "Death Temple": BombHRegionData(),
    "Death Road": BombHRegionData(),
    "Death Garden": BombHRegionData(),
    "Float Zone": BombHRegionData(),
    "Aqua Tank": BombHRegionData(),
    "Aqua Way": BombHRegionData(),
    "Vs Nitros Kanatia": BombHRegionData(),

    "Hard Coaster": BombHRegionData(),
    "Dark Maze": BombHRegionData(),
    "Mad Coaster": BombHRegionData(),
    "Move Stone": BombHRegionData(),
    "Vs Bolban": BombHRegionData(),


    "Hopper Land": BombHRegionData(),
    "Junfalls": BombHRegionData(),
    "Freeze Lake": BombHRegionData(),
    "Cool Cave": BombHRegionData(),

    "Snowland": BombHRegionData(),
    "Storm Valley": BombHRegionData(),
    "Snow Circuit": BombHRegionData(),
    "Heaven Sky": BombHRegionData(),
    "Eye Snake": BombHRegionData(),

    "Vs Nitros Mazone": BombHRegionData(),
    "Air Room": BombHRegionData(),
    "Zero G Room": BombHRegionData(),
    "Mirror Room": BombHRegionData(),
    "Vs Natia": BombHRegionData(),

    "Boss Room 1": BombHRegionData(),
    "Boss Room 2": BombHRegionData(),
    "Boss Room 3": BombHRegionData(),
    "Boss Room 4": BombHRegionData(),
    "Boss Room 5": BombHRegionData(),
    "Boss Room 6": BombHRegionData(),
    "Vs Bagular": BombHRegionData(),

    #"Outter Road": BombHRegionData(),
    #"Inner Road": BombHRegionData(),
    #"Vs Evil Bomber": BombHRegionData(),

}

def get_exit(region, exit_name):
    for exit in region.exits:
        if exit.connected_region.name == exit_name:
            return exit