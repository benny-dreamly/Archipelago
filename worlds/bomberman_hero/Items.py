from typing import Callable, Dict, NamedTuple, Optional, TYPE_CHECKING

from BaseClasses import Item, ItemClassification

if TYPE_CHECKING:
    from . import BombHWorld


class BombHItem(Item):
    game = "Bomberman Hero"


class BombHItemData(NamedTuple):
    code: Optional[int] = None
    type: ItemClassification = ItemClassification.filler
    num_exist: int = 1
    can_create: Callable[["BombHWorld"], bool] = lambda world: True

stageid_to_name= {
    0x134808: "Battle Room",
    0x134809: "Hyper Room",
    0x13480A: "Secret Room",
    0x13480B: "Heavy Room",
    0x13480C: "Sky Room",
    0x13480F: "Blue Cave",
    0x134810: "Hole Lake",
    0x134811: "Red Cave",
    0x134812: "Big Cannon",
    0x134813: "Dark Wood",
    0x134814: "Dragon Road",
    0x134815: "Vs Nitros Planet Bomber",
    0x134816: "Clown Valley",
    0x134817: "Great Rock",
    0x134818: "Fog Route",
    0x134819: "Vs Endol",
    0x13481D: "Groog Hills",
    0x13481E: "Bubble Hole",
    0x13481F: "Erars Lake",
    0x134820: "Waterway",
    0x134821: "Water Slider",
    0x134824: "Rockn Road",
    0x134825: "Water Pool",
    0x134826: "Millian Road",
    0x134827: "Warp Room",
    0x134828: "Dark Prison",
    0x134829: "Vs Nitros Primus",
    0x13482B: "Killer Gate",
    0x13482C: "Spiral Tower",
    0x13482D: "Snake Route",
    0x13482E: "Vs Baruda",
    0x134832: "Hades Crater",
    0x134833: "Magma Lake",
    0x134834: "Magma Dam",
    0x134835: "Crysta Hole",
    0x134836: "Emerald Tube",
    0x134839: "Death Temple",
    0x13483A: "Death Road",
    0x13483B: "Death Garden",
    0x13483C: "Float Zone",
    0x13483D: "Aqua Tank",
    0x13483E: "Aqua Way",
    0x13483F: "Vs Nitros Kanatia",
    0x134840: "Hard Coaster",
    0x134841: "Dark Maze",
    0x134842: "Mad Coaster",
    0x134843: "Move Stone",
    0x134844: "Vs Bolban",
    0x134847: "Hopper Land",
    0x134848: "Junfalls",
    0x134849: "Freeze Lake",
    0x13484A: "Cool Cave",
    0x13484E: "Snowland",
    0x13484F: "Storm Valley",
    0x134850: "Snow Circuit",
    0x134851: "Heaven Sky",
    0x134852: "Eye Snake",
    0x134855: "Vs Nitros Mazone",
    0x134856: "Air Room",
    0x134857: "Zero G Room",
    0x134858: "Mirror Room",
    0x134859: "Vs Natia",
    0x13485C: "Boss Room 1",
    0x13485D: "Boss Room 2",
    0x13485E: "Boss Room 3",
    0x13485F: "Boss Room 4",
    0x134860: "Boss Room 5",
    0x134861: "Boss Room 6",
    0x134862: "Vs Bagular",
}

item_data_table: Dict[str, BombHItemData] = {
    "Bombup": BombHItemData(
        code=0x16523F,
        type=ItemClassification.progression,
        num_exist = 3
    ),
    "Fireup": BombHItemData(
        code=0x165240,
        type=ItemClassification.progression,
        num_exist = 3
    ),
    "Power Glove": BombHItemData(
        code=0x165268,
        type=ItemClassification.trap,
        num_exist=0
    ),
    "Vest": BombHItemData(
        code=0x165258,
        type=ItemClassification.useful,
    ),
    "Salt Bombs": BombHItemData(
        code= 0x165250,
        type=ItemClassification.trap,
        num_exist=0
    ),
    "Disabled HUD":BombHItemData(
        code= 0x1779F8,
        type=ItemClassification.trap,
        num_exist=0
    ),


    "Gold Heart": BombHItemData(
        code=0x165244,
        type=ItemClassification.filler,
        num_exist=0
    ),
    "Healthup": BombHItemData(
        code=0x165245,
        type=ItemClassification.progression,
        num_exist=0
    ),
    "1 UP": BombHItemData(
        code=0x165243,
        type=ItemClassification.filler,
        num_exist=0
    ),
    
    "Adok Bomb": BombHItemData(
        code=0x165248,
        type=ItemClassification.progression,
        num_exist = 0
    ),

    # STAGE UNLOCKS

    "Battle Room": BombHItemData(
        code=0x134808,
        type=ItemClassification.progression,
        num_exist=0,
    ),
    "Hyper Room": BombHItemData(
        code=0x134809,
        type=ItemClassification.progression,
    ),
    "Secret Room": BombHItemData(
        code=0x13480A,
        type=ItemClassification.progression,
    ),
    "Heavy Room": BombHItemData(
        code=0x13480B,
        type=ItemClassification.progression,
    ),
    "Sky Room": BombHItemData(
        code=0x13480C,
        type=ItemClassification.progression,
    ),

    "Blue Cave": BombHItemData(
        code=0x13480F,
        type=ItemClassification.progression,
    ),
    "Hole Lake": BombHItemData(
        code=0x134810,
        type=ItemClassification.progression,
    ),
    "Red Cave": BombHItemData(
        code=0x134811,
        type=ItemClassification.progression,
    ),
    "Big Cannon": BombHItemData(
        code=0x134812,
        type=ItemClassification.progression,
    ),
    "Dark Wood": BombHItemData(
        code=0x134813,
        type=ItemClassification.progression,
    ),
    "Dragon Road": BombHItemData(
        code=0x134814,
        type=ItemClassification.progression,
    ),
    "Vs Nitros Planet Bomber": BombHItemData(
        code=0x134815,
        type=ItemClassification.progression,
    ),

    "Clown Valley": BombHItemData(
        code=0x134816,
        type=ItemClassification.progression,
    ),
    "Great Rock": BombHItemData(
        code=0x134817,
        type=ItemClassification.progression,
    ),
    "Fog Route": BombHItemData(
        code=0x134818,
        type=ItemClassification.progression,
    ),
    "Vs Endol": BombHItemData(
        code=0x134819,
        type=ItemClassification.progression,
    ),

    # Primus
    "Groog Hills": BombHItemData(
        code=0x13481D,
        type=ItemClassification.progression,
    ),
    "Bubble Hole": BombHItemData(
        code=0x13481E,
        type=ItemClassification.progression,
    ),
    "Erars Lake": BombHItemData(
        code=0x13481F,
        type=ItemClassification.progression,
    ),
    "Waterway": BombHItemData(
        code=0x134820,
        type=ItemClassification.progression,
    ),
    "Water Slider": BombHItemData(
        code=0x134821,
        type=ItemClassification.progression,
    ),

    "Rockn Road": BombHItemData(
        code=0x134824,
        type=ItemClassification.progression,
    ),
    "Water Pool": BombHItemData(
        code=0x134825,
        type=ItemClassification.progression,
    ),
    "Millian Road": BombHItemData(
        code=0x134826,
        type=ItemClassification.progression,
    ),
    "Warp Room": BombHItemData(
        code=0x134827,
        type=ItemClassification.progression,
    ),
    "Dark Prison": BombHItemData(
        code=0x134828,
        type=ItemClassification.progression,
    ),
    "Vs Nitros Primus": BombHItemData(
        code=0x134829,
        type=ItemClassification.progression,
    ),

    "Killer Gate": BombHItemData(
        code=0x13482B,
        type=ItemClassification.progression,
    ),
    "Spiral Tower": BombHItemData(
        code=0x13482C,
        type=ItemClassification.progression,
    ),
    "Snake Route": BombHItemData(
        code=0x13482D,
        type=ItemClassification.progression,
    ),
    "Vs Baruda": BombHItemData(
        code=0x13482E,
        type=ItemClassification.progression,
    ),

    # Kanatia
    "Hades Crater": BombHItemData(
        code=0x134832,
        type=ItemClassification.progression,
    ),
    "Magma Lake": BombHItemData(
        code=0x134833,
        type=ItemClassification.progression,
    ),
    "Magma Dam": BombHItemData(
        code=0x134834,
        type=ItemClassification.progression,
    ),
    "Crysta Hole": BombHItemData(
        code=0x134835,
        type=ItemClassification.progression,
    ),
    "Emerald Tube": BombHItemData(
        code=0x134836,
        type=ItemClassification.progression,
    ),

    "Death Temple": BombHItemData(
        code=0x134839,
        type=ItemClassification.progression,
    ),
    "Death Road": BombHItemData(
        code=0x13483A,
        type=ItemClassification.progression,
    ),
    "Death Garden": BombHItemData(
        code=0x13483B,
        type=ItemClassification.progression,
    ),
    "Float Zone": BombHItemData(
        code=0x13483C,
        type=ItemClassification.progression,
    ),
    "Aqua Tank": BombHItemData(
        code=0x13483D,
        type=ItemClassification.progression,
    ),
    "Aqua Way": BombHItemData(
        code=0x13483E,
        type=ItemClassification.progression,
    ),
    "Vs Nitros Kanatia": BombHItemData(
        code=0x13483F,
        type=ItemClassification.progression,
    ),

    "Hard Coaster": BombHItemData(
        code=0x134840,
        type=ItemClassification.progression,
    ),
    "Dark Maze": BombHItemData(
        code=0x134841,
        type=ItemClassification.progression,
    ),
    "Mad Coaster": BombHItemData(
        code=0x134842,
        type=ItemClassification.progression,
    ),
    "Move Stone": BombHItemData(
        code=0x134843,
        type=ItemClassification.progression,
    ),
    "Vs Bolban": BombHItemData(
        code=0x134844,
        type=ItemClassification.progression,
    ),

    # Mazone
    "Hopper Land": BombHItemData(
        code=0x134847,
        type=ItemClassification.progression,
    ),
    "Junfalls": BombHItemData(
        code=0x134848,
        type=ItemClassification.progression,
    ),
    "Freeze Lake": BombHItemData(
        code=0x134849,
        type=ItemClassification.progression,
    ),
    "Cool Cave": BombHItemData(
        code=0x13484A,
        type=ItemClassification.progression,
    ),

    "Snowland": BombHItemData(
        code=0x13484E,
        type=ItemClassification.progression,
    ),
    "Storm Valley": BombHItemData(
        code=0x13484F,
        type=ItemClassification.progression,
    ),
    "Snow Circuit": BombHItemData(
        code=0x134850,
        type=ItemClassification.progression,
    ),
    "Heaven Sky": BombHItemData(
        code=0x134851,
        type=ItemClassification.progression,
    ),
    "Eye Snake": BombHItemData(
        code=0x134852,
        type=ItemClassification.progression,
    ),

    "Vs Nitros Mazone": BombHItemData(
        code=0x134855,
        type=ItemClassification.progression,
    ),
    "Air Room": BombHItemData(
        code=0x134856,
        type=ItemClassification.progression,
    ),
    "Zero G Room": BombHItemData(
        code=0x134857,
        type=ItemClassification.progression,
    ),
    "Mirror Room": BombHItemData(
        code=0x134858,
        type=ItemClassification.progression,
    ),
    "Vs Natia": BombHItemData(
        code=0x134859,
        type=ItemClassification.progression,
    ),
    "Boss Room 1": BombHItemData(
        code=0x13485C,
        type=ItemClassification.progression,
    ),
    "Boss Room 2": BombHItemData(
        code=0x13485D,
        type=ItemClassification.progression,
    ),
    "Boss Room 3": BombHItemData(
        code=0x13485E,
        type=ItemClassification.progression,
    ),
    "Boss Room 4": BombHItemData(
        code=0x13485F,
        type=ItemClassification.progression,
    ),
    "Boss Room 5": BombHItemData(
        code=0x134860,
        type=ItemClassification.progression,
    ),
    "Boss Room 6": BombHItemData(
        code=0x134861,
        type=ItemClassification.progression,
    ),
    
    #"Outter Road": BombHItemData(
    #    code=0x134871,
    #    type=ItemClassification.progression,
    #),
    #"Inner Road": BombHItemData(
    #    code=0x134872,
    #    type=ItemClassification.progression,
    #),
    #"Vs Evil Bomber": BombHItemData(
    #    code=0x134873,
    #    type=ItemClassification.progression,
    #),

    "Disk": BombHItemData(
        code=0x1779F9,
        type=ItemClassification.progression,
        num_exist=0
    ),
}

item_table = {name: data.code for name, data in item_data_table.items() if data.code is not None}
