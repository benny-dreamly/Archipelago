# world/rimworld/__init__.py

import settings
import typing
import xml.etree.ElementTree as ElementTree
from typing import Dict
from .Options import rimworld_options, RimworldOptions
from .Items import RimworldItem
from .Locations import RimworldLocation
from worlds.AutoWorld import World
from BaseClasses import LocationProgressType, Region, Location, Entrance, Item, ItemClassification

class RimworldSettings(settings.Group):
    class RomFile(settings.SNESRomPath):
        """Insert help text for host.yaml here."""


class RimworldWorld(World):
    """Insert description of the world/game here."""
    game = "Rimworld"  # name of the game/world
    options_dataclass = RimworldOptions  # options the player can set
    options: RimworldOptions # typing hints for option results
    settings: typing.ClassVar[RimworldSettings]  # will be automatically assigned from type hint
    topology_present = True  # show path to required location checks in spoiler
    location_pool: Dict[str, int] = {}

    item_name_to_id = {}
    location_name_to_id = {}

    def fill_slot_data(self):
        slot_data = {}

        options = slot_data["options"] = {}
        for option_name in rimworld_options:
            option = getattr(self.options, option_name)
            try:
                optionvalue = int(option.value)
                options[option_name] = optionvalue
            except TypeError:
                pass

        return slot_data

    def create_regions(self) -> None:
        menu_region = Region("Menu", self.player, self.multiworld)
        self.multiworld.regions.append(menu_region)
        
        main_region = Region("Main", self.player, self.multiworld)

        researchLocationCount = getattr(self.options, "ResearchLocationCount").value

        for i in range(researchLocationCount):
            locationName = "Research Location "+ str(i)
            locationId = i + 5197648000
            self.location_pool[locationName] = locationId
            self.location_name_to_id[locationName] = locationId
            # print("Loc: " + locationName + " id " + str(locationId))

        main_region.add_locations(self.location_pool, RimworldLocation)
        for i in range(researchLocationCount):
            self.multiworld.get_location("Research Location " + str(i), self.player).progress_type = LocationProgressType.DEFAULT
        self.multiworld.regions.append(main_region)

        menu_region.connect(main_region)

    def create_item(self, item: str) -> RimworldItem:
        return RimworldItem(item, ItemClassification.progression_skip_balancing, self.item_name_to_id[item], self.player)

    def create_item_from_xml_node(self, item) -> RimworldItem:
        return RimworldItem(item[3].text, ItemClassification.progression_skip_balancing, int(item[0].text), self.player)

    def create_items(self) -> None:
        tree = ElementTree.parse('worlds/rimworld/ArchipelagoItemDefs.xml');
        root = tree.getroot()

        itempool = []
        for item in root:
            itempool.append(self.create_item_from_xml_node(item))
            self.item_name_to_id[item[3].text] = int(item[0].text)
        
        self.multiworld.itempool += itempool