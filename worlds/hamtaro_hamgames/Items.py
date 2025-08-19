from typing import Callable, Dict, NamedTuple, Optional, TYPE_CHECKING

from BaseClasses import Item, ItemClassification

if TYPE_CHECKING:
    from . import HamGamesWorld
    

class HamGamesItem(Item):
    game = "Hamtaro Hamham Games"

class HamGamesItemData(NamedTuple):
    code: Optional[int] = None
    type: ItemClassification = ItemClassification.filler
    num_exist: int = 1
    can_create: Callable[["HamGamesWorld"], bool] = lambda world: True
    fillweight: Optional[float] = None

item_data_table: Dict[str, HamGamesItemData] = {
    
    "Studio Pass": HamGamesItemData(
        code=0x1C2200,
        type=ItemClassification.progression,
    ),
    "Beach Pass": HamGamesItemData(
        code=0x1C2201,
        type=ItemClassification.progression,
    ),
    "Tennis Pass": HamGamesItemData(
        code=0x1C2202,
        type=ItemClassification.progression,
    ),
    "Village Pass": HamGamesItemData(
        code=0x1C2203,
        type=ItemClassification.progression,
    ),
    "Pool Pass": HamGamesItemData(
        code=0x1C2204,
        type=ItemClassification.progression,
    ),
    "Stadium Pass": HamGamesItemData(
        code=0x1C2205,
        type=ItemClassification.progression,
        num_exist=0 # One is already precollected
    ),
    "Lawn Pass": HamGamesItemData(
        code=0x1C2206,
        type=ItemClassification.progression,
    ),

    "Day 2": HamGamesItemData(
        code=0x1C2208,
        type=ItemClassification.progression,
    ),
    "Day 3": HamGamesItemData(
        code=0x1C2209,
        type=ItemClassification.progression,
    ),
    "Day 4": HamGamesItemData(
        code=0x1C220A,
        type=ItemClassification.progression,
    ),
    "Day 5": HamGamesItemData(
        code=0x1C220B,
        type=ItemClassification.progression,
    ),
    "Day 6": HamGamesItemData(
        code=0x1C220C,
        type=ItemClassification.progression,
    ),

    "Hamigo File": HamGamesItemData(
        code=0x1C220D,
        type=ItemClassification.progression,
    ),

    #"Energy Seed": HamGamesItemData(
     #   code=0x1C221A,
    #    type=ItemClassification.useful,
    #    num_exist= 2,
    #),
    "Hamham Games Trophy": HamGamesItemData(
        code=0x1C220E,
        type=ItemClassification.progression,
        num_exist=0
    ),
    "Marathon Nomination":  HamGamesItemData(
        code=0x1C220F,
        type=ItemClassification.progression,
        num_exist=0
    ),

    "Jukebox CD": HamGamesItemData(
        code=0x1C2210,
        type=ItemClassification.filler,
    ),
    "Game Cartridge": HamGamesItemData(
        code=0x1C2211,
        type=ItemClassification.filler,
    ),
    "Sunflower Seed": HamGamesItemData(
        code=0x1C2220,
        type=ItemClassification.filler,
        num_exist= 0,
        fillweight= 0.3,
    ),
    "5 Seeds": HamGamesItemData(
        code=0x1C2221,
        type=ItemClassification.filler,
        num_exist= 0,
        fillweight= 0.75,
    ),
    "10 Seeds": HamGamesItemData(
        code=0x1C2222,
        type=ItemClassification.filler,
        num_exist= 0,
        fillweight= 0.25,
    ),
    "25 Seeds": HamGamesItemData(
        code=0x1C2223,
        type=ItemClassification.filler,
        num_exist= 0,
        fillweight= 0.1,
    ),


}

item_table = {name: data.code for name, data in item_data_table.items() if data.code is not None}
item_id_to_name = {data.code: name for name, data in item_data_table.items() if data.code is not None}
item_filler = [name for name, data in item_data_table.items() if data.type == ItemClassification.filler and data.fillweight is not None]
item_filler_weight = [data.fillweight for name, data in item_data_table.items() if data.type == ItemClassification.filler and data.fillweight is not None]