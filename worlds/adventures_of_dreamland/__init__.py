from typing import Dict, List
from BaseClasses import Item, Location, Region, Entrance, Tutorial, ItemClassification
from Options import PerGameCommonOptions
from worlds.AutoWorld import World#, WebWorld
from .Constants import AOD_BASE_ID
from .Items import item_table
from .Locations import location_table
from .Rules import create_rules
from .data import LocationName

class AdventuresOfDreamlandWorld(World):
    """
    Adventures of Dreamland is an Adventure Game! Have fun.
    """
    game = "Adventures of Dreamland"
    options_dataclass = PerGameCommonOptions
    item_name_to_id = {name: data["id"] for name, data in item_table.items()}
    location_name_to_id = {name: data["id"] for name, data in location_table.items()}

    def create_item(self, name: str) -> "AODItem":
        item_id: int = self.item_name_to_id[name]
        classification = item_table[name]["classification"]

        return AODItem(name, classification, item_id, player=self.player)

    def create_items(self) -> None:
        itempool = [self.create_item(name) for name in item_table]

        # Ensure the item count matches the location count
        num_extra_items = len(location_table) - len(item_table)
        for _ in range(num_extra_items):
            filler_item = AODItem("Filler Item", ItemClassification.filler, None, player=self.player)
            itempool.append(filler_item)

        self.multiworld.itempool += itempool

    def create_region(self, name: str, locations=None, exits=None):
        ret = Region(name, self.player, self.multiworld)
        if locations:
            for location in locations:
                loc_id = self.location_name_to_id.get(location, None)
                location = AODLocation(self.player, location, loc_id, ret)
                ret.locations.append(location)
        if exits:
            for region_exit in exits:
                ret.exits.append(Entrance(self.player, region_exit, ret))
        return ret

    def create_regions(self):
        menu = self.create_region("Menu", locations=None, exits=None)

        for name, data in location_table.items():
            menu.locations.append(
                AODLocation(self.player, name, data["id"], menu)
            )

        self.multiworld.regions.append(menu)

    def set_rules(self) -> None:
        create_rules(self)

class AODItem(Item):
    game: str = "Adventures of Dreamland"

class AODLocation(Location):
    game = "Adventures of Dreamland"