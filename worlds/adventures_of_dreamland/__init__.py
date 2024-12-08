from typing import Dict, List

from BaseClasses import Item, Location, Region, Entrance, Tutorial, ItemClassification
from Options import PerGameCommonOptions
from worlds.AutoWorld import World#, WebWorld
from .Items import item_table
from .Locations import location_table

class AdventuresOfDreamlandWorld(World):
    """
    Adventures of Dreamland is an Adventure Game! Have fun.
    """
    game = "Adventures of Dreamland"
    options_dataclass = PerGameCommonOptions
    item_name_to_id = {item["name"]: item["id"] for item in item_table}

    def create_items(self) -> None:
        itempool = []
        for item in item_table:
            count = item["count"]

            if count <= 0:
                continue
            else:
                for i in range(count):
                    itempool.append(self.create_item(item["name"]))

        self.multiworld.itempool += itempool

class AODItem(Item):
    game: str = "Adventures of Dreamland"

class AODLocation(Location):
    game = "Adventures of Dreamland"