from typing import Callable, Dict, NamedTuple, Optional, TYPE_CHECKING

from BaseClasses import Item, ItemClassification

if TYPE_CHECKING:
    from . import Smash64World
    

class Smash64Item(Item):
    game = "Smash 64"

class Smash64ItemData(NamedTuple):
    code: Optional[int] = None
    type: ItemClassification = ItemClassification.filler
    num_exist: int = 1
    can_create: Callable[["Smash64World"], bool] = lambda world: True
    fillweight: Optional[float] = None

item_data_table: Dict[str, Smash64ItemData] = {
    

    "Mario": Smash64ItemData(
        code=0x1C2100,
        type=ItemClassification.progression,
    ),
    "Fox": Smash64ItemData(
        code=0x1C2101,
        type=ItemClassification.progression,
    ),
    "Donkey Kong": Smash64ItemData(
        code=0x1C2102,
        type=ItemClassification.progression,
    ),
    "Samus": Smash64ItemData(
        code=0x1C2103,
        type=ItemClassification.progression,
    ),
    "Luigi": Smash64ItemData(
        code=0x1C2104,
        type=ItemClassification.progression,
    ),
    "Link": Smash64ItemData(
        code=0x1C2105,
        type=ItemClassification.progression,
    ),
    "Yoshi": Smash64ItemData(
        code=0x1C2106,
        type=ItemClassification.progression,
    ),
    "Captain Falcon": Smash64ItemData(
        code=0x1C2107,
        type=ItemClassification.progression,
    ),
    "Kirby": Smash64ItemData(
        code=0x1C2108,
        type=ItemClassification.progression,
    ),
    "Pikachu": Smash64ItemData(
        code=0x1C2109,
        type=ItemClassification.progression,
    ),
    "Jigglypuff": Smash64ItemData(
        code=0x1C210A,
        type=ItemClassification.progression,
    ),
    "Ness": Smash64ItemData(
        code=0x1C210B,
        type=ItemClassification.progression,
    ),
    "Progressive Classic Difficulty": Smash64ItemData(
        code=0x1C210C,
        type=ItemClassification.progression,
        num_exist= 4
    ),
    "Progressive Stocks": Smash64ItemData(
        code=0x1C210D,
        type=ItemClassification.progression,
        num_exist= 4
    ),

    "Example Item 2": Smash64ItemData(
        code=0x1C2102,
        type=ItemClassification.filler,
        num_exist= 2,
        fillweight= 0.5,
    ),


}

item_table = {name: data.code for name, data in item_data_table.items() if data.code is not None}
item_id_to_name = {data.code: name for name, data in item_data_table.items() if data.code is not None}
item_filler = [name for name, data in item_data_table.items() if data.type == ItemClassification.filler and data.fillweight is not None]
item_filler_weight = [data.fillweight for name, data in item_data_table.items() if data.type == ItemClassification.filler and data.fillweight is not None]