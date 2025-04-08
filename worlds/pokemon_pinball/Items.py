from typing import Callable, Dict, NamedTuple, Optional, TYPE_CHECKING

from BaseClasses import Item, ItemClassification
# Testing 2
if TYPE_CHECKING:
    from . import PokePinballWorld

class PokePinballItem(Item):
    game = "Pokemon Pinball"

class PokePinballItemData(NamedTuple):
    code: Optional[int] = None
    type: ItemClassification = ItemClassification.filler
    num_exist: int = 1
    can_create: Callable[["PokePinballWorld"], bool] = lambda world: True

item_data_table: Dict[str, PokePinballItemData] = {
    "Ball Upgrade": PokePinballItemData(
        code=0x1C2000,
        type=ItemClassification.progression,
        num_exist = 3
    ),
    "Viridian City": PokePinballItemData(
        code=0x1C2001,
        type=ItemClassification.progression,
    ),
    "Viridian Forest": PokePinballItemData(
        code=0x1C2002,
        type=ItemClassification.progression,
    ),
    "Pewter City": PokePinballItemData(
        code=0x1C2003,
        type=ItemClassification.progression,
    ),
    "Mt Moon": PokePinballItemData(
        code=0x1C2004,
        type=ItemClassification.progression,
    ),
    "Cerulean City": PokePinballItemData(
        code=0x1C2005,
        type=ItemClassification.progression,
    ),
    "Vermilion City Seaside": PokePinballItemData(
        code=0x1C2006,
        type=ItemClassification.progression,
    ),
    "Vermilion City Streets": PokePinballItemData(
        code=0x1C2007,
        type=ItemClassification.progression,
    ),
    "Rock Mountain": PokePinballItemData(
        code=0x1C2008,
        type=ItemClassification.progression,
    ),
    "Lavender Town": PokePinballItemData(
        code=0x1C2009,
        type=ItemClassification.progression,
    ),
    "Celadon City": PokePinballItemData(
        code=0x1C200A,
        type=ItemClassification.progression,
    ),
    "Cycling Road": PokePinballItemData(
        code=0x1C200B,
        type=ItemClassification.progression,
    ),
    "Fuchsia City": PokePinballItemData(
        code=0x1C200C,
        type=ItemClassification.progression,
    ),
    "Safari Zone": PokePinballItemData(
        code=0x1C200D,
        type=ItemClassification.progression,
    ),
    "Saffron City": PokePinballItemData(
        code=0x1C200E,
        type=ItemClassification.progression,
    ),
    "Seafoam Island": PokePinballItemData(
        code=0x1C200F,
        type=ItemClassification.progression,
    ),
    "Cinnabar Island": PokePinballItemData(
        code=0x1C2010,
        type=ItemClassification.progression,
    ),
    "Indigo Plateau": PokePinballItemData(
        code=0x1C2011,
        type=ItemClassification.progression,
    ),
    "Red Table": PokePinballItemData(
        code=0x1C2012,
        type=ItemClassification.progression,
    ),
    "Blue Table": PokePinballItemData(
        code=0x1C2013,
        type=ItemClassification.progression,
    ),

    "Extra Ball": PokePinballItemData(
        code=0x1C2030,
        type=ItemClassification.filler,
    ),
    "Pika Power": PokePinballItemData(
        code=0x1C2031,
        type=ItemClassification.filler,
    ),
    "Ball Saver": PokePinballItemData(
        code=0x1C2032,
        type=ItemClassification.filler,
    ),
    "Victory": PokePinballItemData(
        code=0x1C203F,
        type=ItemClassification.progression,
        num_exist=0
    ),

}

item_table = {name: data.code for name, data in item_data_table.items() if data.code is not None}
