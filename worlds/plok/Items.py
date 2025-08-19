from typing import Callable, Dict, NamedTuple, Optional

from BaseClasses import Item, ItemClassification, MultiWorld


class PlokItem(Item):
    game = "Plok"


class PlokItemData(NamedTuple):
    code: Optional[int] = None
    type: ItemClassification = ItemClassification.filler
    num_exist: int = 1
    can_create: Callable[[MultiWorld, int], bool] = lambda multiworld, player: True

item_data_table: Dict[str, PlokItemData] = {
    "Spin Jump": PlokItemData(
        code=0x1C0001,
        type=ItemClassification.progression
    ),
    "Amulet": PlokItemData(
        code=0x1C0002,
        type=ItemClassification.useful
    ),
    "Limb": PlokItemData(
        code=0x1C0003,
        type=ItemClassification.progression,
        num_exist=3
    ),

    "HealthUp": PlokItemData(
        code=0x1C0004,
        type=ItemClassification.progression,
        num_exist=5
    ),
    "Hornet Capacity": PlokItemData(
        code=0x1C0005,
        type=ItemClassification.useful,
        num_exist=4
    ),
    "Shell Capacity": PlokItemData(
        code=0x1C0006,
        type=ItemClassification.useful,
        num_exist=9
    ),

    "Plok Flag": PlokItemData(
        code=0x1C0007,
        type=ItemClassification.progression
    ),
    "Grandpappy journal": PlokItemData(
        code=0x1C0008,
        type=ItemClassification.progression
    ),
    "Flea Pit Rope": PlokItemData(
        code=0x1C0009,
        type=ItemClassification.progression
    ),
    "Flashlight": PlokItemData(
        code=0x1C000D,
        type=ItemClassification.progression
    ),

    "Shells": PlokItemData(
        code=0x1C000A,
        type=ItemClassification.filler,
        num_exist=0
    ),
    "Extra Plife": PlokItemData(
        code=0x1C000B,
        type=ItemClassification.filler,
        num_exist=0
    ),
    "Fruit": PlokItemData(
        code=0x1C000C,
        type=ItemClassification.filler,
        num_exist=0
    ),
    "Force Field": PlokItemData(
        code=0x1C000E,
        type=ItemClassification.filler,
        num_exist=0
    ),
    "Rage": PlokItemData(
        code=0x1C000F,
        type=ItemClassification.filler,
        num_exist=0
    ),
#    "Hornet": PlokItemData(
#        code=0x1C000B,
#        type=ItemClassification.filler
#    ),

    "Unicycle": PlokItemData(
        code=0x1C0011,
        type=ItemClassification.progression
    ),
    "Car": PlokItemData(
        code=0x1C0012,
        type=ItemClassification.progression
    ),
    "Jet Booster": PlokItemData(
        code=0x1C0013,
        type=ItemClassification.progression
    ),
    "Motorcycle": PlokItemData(
        code=0x1C0014,
        type=ItemClassification.progression
    ),
    "Helicopter": PlokItemData(
        code=0x1C0015,
        type=ItemClassification.progression
    ),
    "Tank": PlokItemData(
        code=0x1C0016,
        type=ItemClassification.progression
    ),
    "UFO": PlokItemData(
        code=0x1C0017,
        type=ItemClassification.progression
    ),
    "Springs": PlokItemData(
        code=0x1C0018,
        type=ItemClassification.progression
    ),

    "Plocky Costume": PlokItemData(
        code=0x1C0021,
        type=ItemClassification.useful
    ),
    "Rocketman Costume": PlokItemData(
        code=0x1C0023,
        type=ItemClassification.useful
    ),
    "Squire Costume": PlokItemData(
        code=0x1C0025,
        type=ItemClassification.useful
    ),
    "Fireman Costume": PlokItemData(
        code=0x1C0026,
        type=ItemClassification.progression
    ),
    "Cowboy Costume": PlokItemData(
        code=0x1C0027,
        type=ItemClassification.filler
    ),

    "Boxer Shorts": PlokItemData(
        code=0x1C0030,
        type=ItemClassification.progression
    ),
    "Scarf": PlokItemData(
        code=0x1C0031,
        type=ItemClassification.progression
    ),
    "Bang Flag": PlokItemData(
        code=0x1C0032,
        type=ItemClassification.progression
    ),
    "Torn Flag": PlokItemData(
        code=0x1C0033,
        type=ItemClassification.progression
    ),
    "Overalls": PlokItemData(
        code=0x1C0034,
        type=ItemClassification.progression
    ),
    "Sports Flag": PlokItemData(
        code=0x1C0035,
        type=ItemClassification.progression
    ),
    "Pirate Flag": PlokItemData(
        code=0x1C0036,
        type=ItemClassification.progression
    ),
    "Bone": PlokItemData(
        code=0x1C0037,
        type=ItemClassification.progression
    ),
    "Carrot": PlokItemData(
        code=0x1C0038,
        type=ItemClassification.progression
    ),
    "Anvil": PlokItemData(
        code=0x1C0039,
        type=ItemClassification.progression
    ),
    "Old Boot": PlokItemData(
        code=0x1C003A,
        type=ItemClassification.progression
    ),
    "Used String": PlokItemData(
        code=0x1C003B,
        type=ItemClassification.progression
    ),
    "Broken Vase": PlokItemData(
        code=0x1C003C,
        type=ItemClassification.progression
    ),

    "Unicycle Rental": PlokItemData(
        code=0x1C0040,
        type=ItemClassification.filler,
        num_exist=0
    ),
    "Car Rental": PlokItemData(
        code=0x1C0041,
        type=ItemClassification.filler,
        num_exist=0
    ),
    "Jet Rental": PlokItemData(
        code=0x1C0042,
        type=ItemClassification.filler,
        num_exist=0
    ),
    "Motorcycle Rental": PlokItemData(
        code=0x1C0043,
        type=ItemClassification.filler,
        num_exist=0
    ),
    "Helicopter Rental": PlokItemData(
        code=0x1C0044,
        type=ItemClassification.filler,
        num_exist=0
    ),
    "Tank Rental": PlokItemData(
        code=0x1C0045,
        type=ItemClassification.filler,
        num_exist=0
    ),
    "UFO Rental": PlokItemData(
        code=0x1C0046,
        type=ItemClassification.filler,
        num_exist=0
    ),
    "Springs Rental": PlokItemData(
        code=0x1C0047,
        type=ItemClassification.filler,
        num_exist=0
    ),

    "Boxing Glove Rental": PlokItemData(
        code=0x1C0048,
        type=ItemClassification.filler,
        num_exist=0
    ),
    "Rocket Rental": PlokItemData(
        code=0x1C0049,
        type=ItemClassification.filler,
        num_exist=0
    ),
    "Musket Rental": PlokItemData(
        code=0x1C004A,
        type=ItemClassification.filler,
        num_exist=0
    ),
    "Flamethrower Rental": PlokItemData(
        code=0x1C004B,
        type=ItemClassification.filler,
        num_exist=0
    ),
    "Sheriff Badge Rental": PlokItemData(
        code=0x1C004C,
        type=ItemClassification.filler,
        num_exist=0
    ),

    "Flea Queen Dead": PlokItemData(
        type=ItemClassification.progression,
        can_create= False
    ) 
}

item_table = {name: data.code for name, data in item_data_table.items() if data.code is not None}
