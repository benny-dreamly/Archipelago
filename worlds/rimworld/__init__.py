# world/rimworld/__init__.py

import pkgutil
import random
import settings
import typing
import xml.etree.ElementTree as ElementTree
from typing import Dict
from .Options import RimworldOptions, max_research_locations, rimworld_options
from .Items import RimworldItem
from .Locations import RimworldLocation, base_location_id, location_id_gap
from ..generic.Rules import set_rule
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

    craftable_item_id_to_name = {}
    craftable_item_id_to_prereqs = {}
    location_prerequisites = {}
    craft_location_recipes = {}

    item_root = ElementTree.fromstring(pkgutil.get_data(__name__,"ArchipelagoItemDefs.xml"));

    for item in item_root:
        itemName = item.find("label").text
        itemId = item.find("Id").text
        defType = item.find("DefType").text
        if (defType == "ResearchProjectDef"):
            item_name_to_id[itemName] = int(itemId)
        elif (defType == "ThingDef"):
            craftable_item_id_to_prereqs[itemId] = []
            defName = item.find("defName").text
            defName = defName.replace("Thing", "")
            craftable_item_id_to_name[itemId] = defName
            prerequisites = item.find("Prerequisites")
            if (prerequisites is not None):
                for prereq in prerequisites:
                    craftable_item_id_to_prereqs[itemId].append(prereq.text)





    baseLocationId = base_location_id
    for i in range(max_research_locations):
        locationName = "Basic Research Location "+ str(i)
        locationId = i + baseLocationId
        location_name_to_id[locationName] = locationId

    baseLocationId = baseLocationId + location_id_gap
    for i in range(max_research_locations):
        locationName = "Hi-Tech Research Location "+ str(i)
        locationId = i + baseLocationId
        location_name_to_id[locationName] = locationId
        location_prerequisites[locationName] = ["Microelectronics"]

    baseLocationId = baseLocationId + location_id_gap
    for i in range(max_research_locations):
        locationName = "Multi-Analyzer Research Location "+ str(i)
        locationId = i + baseLocationId
        location_name_to_id[locationName] = locationId
        location_prerequisites[locationName] = ["Microelectronics", "Multi-Analyzer"]

    baseLocationId = baseLocationId + location_id_gap
    for i in range(max_research_locations):
        locationName = "Craft Location " + str(i)
        locationId = i + baseLocationId
        location_name_to_id[locationName] = locationId





    def fill_slot_data(self):
        slot_data = {}

        slot_data["seed"] = self.multiworld.seed_name
        options = slot_data["options"] = {}
        for option_name in rimworld_options:
            option = getattr(self.options, option_name)
            try:
                optionvalue = int(option.value)
                options[option_name] = optionvalue
            except TypeError:
                pass

        slot_data["craft_recipes"] = self.craft_location_recipes

        return slot_data

    def create_regions(self) -> None:
        menu_region = Region("Menu", self.player, self.multiworld)
        self.multiworld.regions.append(menu_region)
        
        main_region = Region("Main", self.player, self.multiworld)

        basicResearchLocationCount = getattr(self.options, "BasicResearchLocationCount").value
        baseLocationId = base_location_id
        for i in range(basicResearchLocationCount):
            locationName = "Basic Research Location " + str(i)
            locationId = i + baseLocationId
            self.location_pool[locationName] = locationId

        hiTechResearchLocationCount = getattr(self.options, "HiTechResearchLocationCount").value
        baseLocationId = baseLocationId + location_id_gap
        for i in range(hiTechResearchLocationCount):
            locationName = "Hi-Tech Research Location " + str(i)
            locationId = i + baseLocationId
            self.location_pool[locationName] = locationId

        multiAnalyzerResearchLocationCount = getattr(self.options, "MultiAnalyzerResearchLocationCount").value
        baseLocationId = baseLocationId + location_id_gap
        for i in range(multiAnalyzerResearchLocationCount):
            locationName = "Multi-Analyzer Research Location " + str(i)
            locationId = i + baseLocationId
            self.location_pool[locationName] = locationId

        craftLocationCount = getattr(self.options, "CraftLocationCount").value
        baseLocationId = baseLocationId + location_id_gap
        for i in range(craftLocationCount):
            locationName = "Craft Location " + str(i)
            locationId = i + baseLocationId
            itemId1, itemName1 = random.choice(list(self.craftable_item_id_to_name.items()))
            # Allows duplicate items - maybe fix it? Maybe who cares?
            itemId2, itemName2 = random.choice(list(self.craftable_item_id_to_name.items()))
            prerequisites = list(set(self.craftable_item_id_to_prereqs[itemId1]) | set(self.craftable_item_id_to_prereqs[itemId2]))
            self.location_prerequisites[locationName] = prerequisites
            self.craft_location_recipes[locationId] = [itemName1, itemName2]
            self.location_pool[locationName] = locationId

        main_region.add_locations(self.location_pool, RimworldLocation)
        for locationName in self.location_pool:
            self.multiworld.get_location(locationName, self.player).progress_type = LocationProgressType.DEFAULT

        self.multiworld.regions.append(main_region)

        menu_region.connect(main_region)

    def create_item(self, item: str) -> RimworldItem:
        return RimworldItem(item, ItemClassification.progression, self.item_name_to_id[item], self.player)

    def create_item_from_xml_node(self, item) -> RimworldItem:
        return RimworldItem(item[3].text, ItemClassification.progression, int(item[0].text), self.player)

    def create_items(self) -> None:
        itempool = []
        for item in self.item_name_to_id:
            itempool.append(self.create_item(item))
        
        self.multiworld.itempool += itempool

    def set_rules(self) -> None:
        for locationName in self.location_pool:
            if locationName in self.location_prerequisites:
                set_rule(self.multiworld.get_location(locationName, self.player),
                    lambda state: state.has_all(self.location_prerequisites[locationName], self.player))
            '''locationId = self.location_name_to_id[locationName]
            if locationId >= base_location_id + location_id_gap + location_id_gap:
                set_rule(self.multiworld.get_location(locationName, self.player),
                    lambda state: state.has("Microelectronics", self.player) and state.has("Multi-Analyzer", self.player))
            elif locationId >= base_location_id + location_id_gap:
                set_rule(self.multiworld.get_location(locationName, self.player),
                    lambda state: state.has("Microelectronics", self.player))'''


