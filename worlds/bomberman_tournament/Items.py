from typing import Callable, Dict, NamedTuple, Optional, TYPE_CHECKING

from BaseClasses import Item, ItemClassification

if TYPE_CHECKING:
    from . import BomberTWorld

id_to_string = {
    0x1C278A: "Health",
    0x1C278B: "BombUp",
    0x1C278C: "FireUp",
    0x1C278D: "Progressive Boots",
    0x1C278E: "Progressive Armor",

    0x1C2785: "Balloon",
    0x1C2786: "RainDrop",
    0x1C2787: "Hammer",
    0x1C2790: "Transistor",
    0x1C2791: "Sensor",

    0x1C2792: "Radar",
    0x1C2793: "Comic 1",
    0x1C2794: "Camera",
    0x1C2795: "Louie Photo",
    0x1C2796: "Ring",
    0x1C2797: "Medal of Bravery",
    0x1C27A0: "Disinfectant",
    0x1C27A1: "Fish Hook",
    0x1C27A2: "Medal of Justice",
    0x1C27A3: "Egg",
    0x1C27A4: "Ice Flowers",
    0x1C27A5: "Medal of Love",
    0x1C27A6: "Teriyaki Beef",
    0x1C27A7: "Medal of Friendship",
    0x1C27B0: "Stepcounter",
    0x1C27B1: "Flour",
    0x1C27B2: "Bread",
    0x1C27B3: "Small Medicine",
    0x1C27B4: "Large Medicine",
    0x1C27B7: "Comic 2",
    0x1C27C0: "Comic 3",
    0x1C27C1: "Comic 4",
    0x1C2850: "Comic 5",

    0x1C27C2: "Magnet Crystal",
    0x1C27C3: "Pretty Crystal",
    0x1C27C4: "Plasma Crystal",
    0x1C27C5: "Golem Crystal",
    0x1C2812: "Fantasy Crystal",

    0x1C27D0: "Hold Bomb",
    0x1C27D1: "Aqua Bomb",
    0x1C27D2: "Power Bomb",
    0x1C27D3: "RC Bomb",
    0x1C27D4: "Landmine",
    

    0x1C2965: "Pommy",
    0x1C2980: "Ceedrun",
    0x1C2972: "Elifan",
    0x1C2994: "P Fangs",
    0x1C2990: "Sharkun",
    0x1C29A3: "Th Liger",
    0x1C29A5: "Kai-man",
    0x1C29B2: "TwinDrag",
    0x1C2987: "P Nucklz",
    0x1C2995: "P Sea",
    0x1C29C7: "ToughGuy",
    0x1C29C4: "P Beast",
    0x1C29D2: "Pteradon",
    0x1C29B7: "Dorako",
    0x1C2996: "P Dragon",
    0x1C29D0: "Youno",
    0x1C2A07: "Sibaloon",
    0x1C29D5: "P Animal",
    0x1C29E5: "Unagi",
    0x1C2A00: "Elekong",
    0x1C29F0: "Youni",
    0x1C2997: "SeaWing",
    0x1C29F1: "KameKing",
    0x1C29B1: "MarinGon",
    0x1C2973: "Firekong",

    0x1C2982: "Magnet Door Key",
    0x1C2985: "Boat Key",
    0x1C29D1: "Desert Key",
    0x1C298F: "Zone Key",

    0x1C2958: "50 Gold",
    0x1C29A8: "100 Gold",
}

kara_hints = [
    "Pommy",
    "Ceedrun",
    "Elifan",
    "P Fangs",
    "Sharkun",
    "Th Liger",
    "Kai-man",
    "TwinDrag",
    "P Nucklz",
    "P Sea",
    "ToughGuy",
    "P Beast",
    "Pteradon",
    "Dorako",
    "P Dragon",
    "Youno",
    "Sibaloon",
    "P Animal",
    "Unagi",
    "Elekong",
    "Youni",
    "SeaWing",
    "KameKing",
    "MarinGon",
    "Firekong",
]
medal_hints = [
    "Medal of Bravery",
    "Medal of Justice",
    "Medal of Love",
    "Medal of Friendship",
]
bomb_hints = [
    "Hold Bomb",
    "Aqua Bomb",
    "Power Bomb",
    "RC Bomb",
    "Landmine"
]
key_hints = [
    "Magnet Door Key",
    "Boat Key",
    "Desert Key"
]
item_hints = [
    "Balloon",
    "RainDrop",
    "Hammer",
    "Transistor",
    "Sensor",

    "Camera",
    "Ring",
    "Disinfectant",
    "Fish Hook",
    "Egg",
    "Medal of Love",
    "Teriyaki Beef",
    "Stepcounter",
]

class BomberTItem(Item):
    game = "Bomberman Tournament"


class BomberTItemData(NamedTuple):
    code: Optional[int] = None
    type: ItemClassification = ItemClassification.filler
    num_exist: int = 1
    address: Optional[int] = None
    mask: Optional[int] = None
    can_create: Callable[["BomberTWorld"], bool] = lambda world: True


item_data_table: Dict[str, BomberTItemData] = {
    "Health": BomberTItemData(
        code=0x1C278A,
        type=ItemClassification.useful,
        num_exist = 6,
        address= 0x35195
    ),
    "BombUp": BomberTItemData(
        code=0x1C278B,
        type=ItemClassification.useful,
        num_exist = 3,
        address= 0x35196
    ),
    "FireUp": BomberTItemData(
        code=0x1C278C,
        type=ItemClassification.progression,
        num_exist = 3,
        address= 0x35197
    ),
    "Progressive Boots": BomberTItemData(
        code=0x1C278D,
        type=ItemClassification.useful,
        num_exist=2,
        address= 0x35278
    ),
    "Progressive Armor": BomberTItemData(
        code=0x1C278E,
        type=ItemClassification.useful,
        num_exist=2,
        address= 0x35278
    ),
    "Balloon": BomberTItemData(
        code=0x1C2785,
        type=ItemClassification.progression,
        address= 0x35278,
        mask=0x20
    ),
    "RainDrop": BomberTItemData(
        code=0x1C2786,
        type=ItemClassification.progression,
        address= 0x35278,
        mask=0x40
    ),
    "Hammer": BomberTItemData(
        code=0x1C2787,
        type=ItemClassification.progression,
        address= 0x35278,
        mask=0x80
    ),
    "Transistor": BomberTItemData(
        code=0x1C2790,
        type=ItemClassification.progression,
        address= 0x35279,
        mask=0x1
    ),
    "Sensor": BomberTItemData(
        code=0x1C2791,
        type=ItemClassification.progression,
        address= 0x35279,
        mask=0x2
    ),
    "Radar": BomberTItemData(
        code=0x1C2792,
        type=ItemClassification.useful,
        address= 0x35279,
        mask=0x4
    ),
    "Comic 1": BomberTItemData(
        code=0x1C2793,
        type=ItemClassification.filler,
        address= 0x35279,
        mask=0x8
    ),
    "Camera": BomberTItemData(
        code=0x1C2794,
        type=ItemClassification.progression,
        address= 0x35279,
        mask=0x10
    ),
    #"Louie Photo": BomberTItemData(
    #    code=0x1C2795,
    #    type=ItemClassification.progression,
    #    address= 0x35279,
    #    mask=0x20
    #),
    "Ring": BomberTItemData(
        code=0x1C2796,
        type=ItemClassification.progression,
        address= 0x35279,
        mask=0x40
    ),
    "Medal of Bravery": BomberTItemData(
        code=0x1C2797,
        type=ItemClassification.progression,
        address= 0x35279,
        mask=0x80,
        num_exist=0
    ),
    "Disinfectant": BomberTItemData(
        code=0x1C27A0,
        type=ItemClassification.progression,
        address= 0x3527A,
        mask=0x1
    ),
    "Fish Hook": BomberTItemData(
        code=0x1C27A1,
        type=ItemClassification.progression,
        address= 0x3527A,
        mask=0x2
    ),
    "Medal of Justice": BomberTItemData(
        code=0x1C27A2,
        type=ItemClassification.progression,
        address= 0x3527A,
        mask=0x4,
        num_exist=0
    ),
    "Egg": BomberTItemData(
        code=0x1C27A3,
        type=ItemClassification.progression,
        address= 0x3527A,
        mask=0x8
    ),
    #"IceFlwrs": BomberTItemData(
    #    code=0x1C27A4,
    #    type=ItemClassification.progression,
    #    address= 0x3527A,
    #    mask=0x10
    #),
    "Medal of Love": BomberTItemData(
        code=0x1C27A5,
        type=ItemClassification.progression,
        address= 0x3527A,
        mask=0x20,
        num_exist=0
    ),
    "Teriyaki Beef": BomberTItemData(
        code=0x1C27A6,
        type=ItemClassification.progression,
        address= 0x3527A,
        mask=0x40,
    ),
    "Medal of Friendship": BomberTItemData(
        code=0x1C27A7,
        type=ItemClassification.progression,
        address= 0x3527A,
        mask=0x80,
        num_exist=0
    ),
    "Stepcounter": BomberTItemData(
        code=0x1C27B0,
        type=ItemClassification.progression,
        address= 0x3527B,
        mask=0x1
    ),
    #"Flour": BomberTItemData(
    #    code=0x1C27B1,
    #    type=ItemClassification.progression,
    #    address= 0x3527B,
    #    mask=0x2
    #),
    #"Bread": BomberTItemData(
    #    code=0x1C27B2,
    #    type=ItemClassification.progression,
    #    address= 0x3527B,
    #    mask=0x4
    #),
    "Small Medicine": BomberTItemData(
        code=0x1C27B3,
        type=ItemClassification.filler,
        address= 0x3527B,
        mask=0x8
    ),
    "Large Medicine": BomberTItemData(
        code=0x1C27B4,
        type=ItemClassification.filler,
        address= 0x3527B,
        mask=0x10
    ),
    "Comic 2": BomberTItemData(
        code=0x1C27B7,
        type=ItemClassification.filler,
        address= 0x3527B,
        mask=0x80
    ),
    "Comic 3": BomberTItemData(
        code=0x1C27C0,
        type=ItemClassification.filler,
        address= 0x3527C,
        mask=0x1
    ),
    "Comic 4": BomberTItemData(
        code=0x1C27C1,
        type=ItemClassification.filler,
        address= 0x3527C,
        mask=0x2
    ),
    "Comic 5": BomberTItemData(
        code=0x1C2850,
        type=ItemClassification.filler,
        address= 0x35285,
        mask=0x1
    ),
    "Magnet Crystal": BomberTItemData(
        code=0x1C27C2,
        type=ItemClassification.useful,
        address= 0x3527C,
        mask=0x4
    ),
    "Pretty Crystal": BomberTItemData(
        code=0x1C27C3,
        type=ItemClassification.useful,
        address= 0x3527C,
        mask=0x8
    ),
    "Plasma Crystal": BomberTItemData(
        code=0x1C27C4,
        type=ItemClassification.useful,
        address= 0x3527C,
        mask=0x10
    ),
    "Golem Crystal": BomberTItemData(
        code=0x1C27C5,
        type=ItemClassification.useful,
        address= 0x3527C,
        mask=0x20
    ),
    "Hold Bomb": BomberTItemData(
        code=0x1C27D0,
        type=ItemClassification.useful,
        address= 0x3527D,
        mask=0x1
    ),
    "Aqua Bomb": BomberTItemData(
        code=0x1C27D1,
        type=ItemClassification.progression,
        address= 0x3527D,
        mask=0x2
    ),
    "Power Bomb": BomberTItemData(
        code=0x1C27D2,
        type=ItemClassification.useful,
        address= 0x3527D,
        mask=0x4
    ),
    "RC Bomb": BomberTItemData(
        code=0x1C27D3,
        type=ItemClassification.progression,
        address= 0x3527D,
        mask=0x8
    ),
    "Landmine": BomberTItemData(
        code=0x1C27D4,
        type=ItemClassification.useful,
        address= 0x3527D,
        mask=0x10
    ),
    "Fantasy Crystal": BomberTItemData(
        code=0x1C2812,
        type=ItemClassification.useful,
        address= 0x35281,
        mask=0x4
    ),


    "Pommy": BomberTItemData(
        code=0x1C2965,
        type=ItemClassification.progression,
        address= 0x35296,
        mask=0x20,
        num_exist=0
    ),
    "Ceedrun": BomberTItemData(
        code=0x1C2980,
        type=ItemClassification.progression,
        address= 0x35298,
        mask=0x1
    ),
    "Elifan": BomberTItemData(
        code=0x1C2972,
        type=ItemClassification.progression,
        address= 0x35297,
        mask=0x4
    ),
    "P Fangs": BomberTItemData(
        code=0x1C2994,
        type=ItemClassification.progression,
        address= 0x35299,
        mask=0x10,
        num_exist=0
    ),
    "Sharkun": BomberTItemData(
        code=0x1C2991,
        type=ItemClassification.progression,
        address= 0x35299,
        mask=0x1
    ),
    "Th Liger": BomberTItemData(
        code=0x1C29A3,
        type=ItemClassification.useful,
        address= 0x3529A,
        mask=0x8
    ),
    "Kai-man": BomberTItemData(
        code=0x1C29A5,
        type=ItemClassification.progression,
        address= 0x3529A,
        mask=0x20
    ),
    "TwinDrag": BomberTItemData(
        code=0x1C29B2,
        type=ItemClassification.progression,
        address= 0x3529B,
        mask=0x4
    ),
    "P Nucklz": BomberTItemData(
        code=0x1C2987,
        type=ItemClassification.progression,
        address= 0x35298,
        mask=0x80
    ),
    "P Sea": BomberTItemData(
        code=0x1C2995,
        type=ItemClassification.progression,
        address= 0x35299,
        mask=0x20,
        num_exist=0
    ),
    "ToughGuy": BomberTItemData(
        code=0x1C29C7,
        type=ItemClassification.progression,
        address= 0x3529C,
        mask=0x80
    ),
    "P Beast": BomberTItemData(
        code=0x1C29C4,
        type=ItemClassification.progression,
        address= 0x3529C,
        mask=0x10
    ),
    "Pteradon": BomberTItemData(
        code=0x1C29D2,
        type=ItemClassification.useful,
        address= 0x3529D,
        mask=0x4
    ),
    "Dorako": BomberTItemData(
        code=0x1C29B7,
        type=ItemClassification.progression,
        address= 0x3529B,
        mask=0x80
    ),
    "P Dragon": BomberTItemData(
        code=0x1C2996,
        type=ItemClassification.progression,
        address= 0x35299,
        mask=0x40,
        num_exist=0
    ),
    "Youno": BomberTItemData(
        code=0x1C29D0,
        type=ItemClassification.progression,
        address= 0x3529D,
        mask=0x1
    ),
    "Sibaloon": BomberTItemData(
        code=0x1C2A07,
        type=ItemClassification.progression,
        address= 0x352A0,
        mask=0x80
    ),
    "P Animal": BomberTItemData(
        code=0x1C29D5,
        type=ItemClassification.progression,
        address= 0x3529D,
        mask=0x20
    ),
    "Unagi": BomberTItemData(
        code=0x1C29E5,
        type=ItemClassification.progression,
        address= 0x3529E,
        mask=0x20
    ),
    "Elekong": BomberTItemData(
        code=0x1C2A00,
        type=ItemClassification.useful,
        address= 0x352A0,
        mask=0x1
    ),
    "Youni": BomberTItemData(
        code=0x1C29F0,
        type=ItemClassification.progression,
        address= 0x3529F,
        mask=0x1
    ),
    "SeaWing": BomberTItemData(
        code=0x1C2997,
        type=ItemClassification.progression,
        address= 0x35299,
        mask=0x80,
        num_exist=0
    ),
    "KameKing": BomberTItemData(
        code=0x1C29F1,
        type=ItemClassification.progression,
        address= 0x3529F,
        mask=0x2
    ),
    "MarinGon": BomberTItemData(
        code=0x1C29B1,
        type=ItemClassification.useful,
        address= 0x3529B,
        mask=0x2
    ),
    "Firekong": BomberTItemData(
        code=0x1C2973,
        type=ItemClassification.useful,
        address= 0x35297,
        mask=0x8
    ),

    #Special items
    "Magnet Door Key": BomberTItemData(
        code=0x1C2982,
        type=ItemClassification.progression,
        address= 0x35298,
        mask=0x4,
        num_exist=0
    ),
    "Boat Key": BomberTItemData(
        code=0x1C2985,
        type=ItemClassification.progression,
        address= 0x35298,
        mask=0x20,
        num_exist=0
    ),
    "Desert Key": BomberTItemData(
        code=0x1C29D1,
        type=ItemClassification.progression,
        address= 0x3529D,
        mask=0x2,
        num_exist=0
    ),
    
    # Non flag
    "Zone Key": BomberTItemData(
        code=0x1C298F,
        type=ItemClassification.progression,
        address= 0x35298,
        mask=0x4,
        num_exist=0
    ),

    # Filler
    "50 Gold": BomberTItemData(
        code=0x1C2958,
        type=ItemClassification.useful,
        address= 0x3529D,
        mask=0x2,
        num_exist=0
    ),
    "100 Gold": BomberTItemData(
        code=0x1C29A8,
        type=ItemClassification.useful,
        address= 0x3529D,
        mask=0x2,
        num_exist=0
    ),

    # Teleports
    # DEbug only for now
    #"Beta Teleport": BomberTItemData(
    #    code=0x1C2A11,
    #    type=ItemClassification.progression,
    #    address= 0x352A1,
    #    mask=0x2,
    #    num_exist=0
    #),
    "Gamma Teleport": BomberTItemData(
        code=0x1C2A12,
        type=ItemClassification.progression,
        address= 0x352A1,
        mask=0x2,
        num_exist=0
    ),
    "Delta Teleport": BomberTItemData(
        code=0x1C2A13,
        type=ItemClassification.progression,
        address= 0x352A1,
        mask=0x2,
        num_exist=0
    ),
    "Epsilon Teleport": BomberTItemData(
        code=0x1C2A14,
        type=ItemClassification.progression,
        address= 0x352A1,
        mask=0x2,
        num_exist=0
    ),
    "Upsilon Teleport": BomberTItemData(
        code=0x1C2A15,
        type=ItemClassification.progression,
        address= 0x352A1,
        mask=0x2,
        num_exist=0
    ),
    #"Zeta Teleport": BomberTItemData(
    #    code=0x1C2A16,
    #    type=ItemClassification.progression,
    #    address= 0x352A1,
    #    mask=0x2,
    #    num_exist=0
    #),
    "Ita Teleport": BomberTItemData(
        code=0x1C2A17,
        type=ItemClassification.progression,
        address= 0x352A1,
        mask=0x2,
        num_exist=0
    ),


    "MAX": BomberTItemData(
        code=0x1C202F,
        type=ItemClassification.progression,
        num_exist= 0
    ),
}

item_table = {name: data.code for name, data in item_data_table.items() if data.code is not None}
#useful_items = {name: data for name, data in item_data_table.items() if data.type == ItemClassification.useful}