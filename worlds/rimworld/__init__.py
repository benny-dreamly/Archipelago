# world/rimworld/__init__.py

import logging
import pkgutil
import random
import settings
import typing
import xml.etree.ElementTree as ElementTree
from typing import Dict
from .Options import RimworldOptions, max_research_locations, rimworld_options
from .Items import RimworldItem
from .Locations import RimworldLocation, base_location_id, location_id_gap, generic_victory_requirements, ship_launch_victory_requirements, royalty_victory_requirements, archonexus_victory_requirements, anomaly_victory_requirements
from ..generic.Rules import set_rule, add_rule
from worlds.AutoWorld import World
from BaseClasses import LocationProgressType, Region, Location, Entrance, Item, ItemClassification
from Options import OptionError

logger = logging.getLogger("Rimworld")

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

    item_name_to_id = {}
    location_name_to_id = {}

    # Yes, yes, I know this series of dictionaries is bad. I'll probably fix it eventually.
    item_name_to_expansion = {}
    tribal_tech_items = []
    crashlanded_tech_items = []
    progression_locations = {}

    location_prerequisites = {}

    craftable_item_id_to_name = {}
    craftable_item_id_to_prereqs = {}
    craftable_item_tech_level = {}
    craft_location_recipes = {}

    location_counts = {}
    max_item_id = 0

    item_root = ElementTree.fromstring(pkgutil.get_data(__name__,"ArchipelagoItemDefs.xml"));

    for item in item_root:
        itemName = item.find("label").text
        itemId = item.find("Id").text
        if int(itemId) > max_item_id:
            max_item_id = int(itemId)
        defType = item.find("DefType").text
        expansion = item.find("RequiredExpansion").text
        if (defType == "ResearchProjectDef"):
            item_name_to_id[itemName] = int(itemId)
            item_name_to_expansion[itemName] = expansion
            researchTags = item.find("ResearchTags")
            if researchTags is not None:
                for techTag in researchTags:
                    if techTag.text == "TribalStart":
                        tribal_tech_items.append(itemName)
                    if techTag.text == "ClassicStart":
                        crashlanded_tech_items.append(itemName)
        elif (defType == "ThingDef"):
            craftable_item_id_to_prereqs[itemId] = []
            defName = item.find("defName").text
            defName = defName.replace("Thing", "")
            techLevel = item.find("TechLevel").text
            craftable_item_id_to_name[itemId] = defName
            item_name_to_expansion[defName] = expansion
            craftable_item_tech_level[itemId] = techLevel
            prerequisites = item.find("Prerequisites")
            if (prerequisites is not None):
                for prereq in prerequisites:
                    craftable_item_id_to_prereqs[itemId].append(prereq.text)

    item_name_to_id["Temp Filler"] = max_item_id + 1
    item_name_to_expansion["Temp Filler"] = "Filler"





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

    baseLocationId = baseLocationId + location_id_gap
    for i in range(max_research_locations):
        locationName = "Multi-Analyzer Research Location "+ str(i)
        locationId = i + baseLocationId
        location_name_to_id[locationName] = locationId

    baseLocationId = baseLocationId + location_id_gap
    for i in range(max_research_locations):
        locationName = "Craft Location " + str(i)
        locationId = i + baseLocationId
        location_name_to_id[locationName] = locationId


    baseLocationId = baseLocationId + location_id_gap
    locationName = "Space Victory"
    locationId = baseLocationId
    location_name_to_id[locationName] = locationId

    locationName = "Royalty Victory"
    locationId = baseLocationId + 1
    location_name_to_id[locationName] = locationId

    locationName = "Archonexus Victory"
    locationId = baseLocationId + 2
    location_name_to_id[locationName] = locationId

    locationName = "Anomaly Victory"
    locationId = baseLocationId + 3
    location_name_to_id[locationName] = locationId




    def generate_early(self):
        royalty_enabled = getattr(self.options, "RoyaltyEnabled")
        ideology_enabled = getattr(self.options, "IdeologyEnabled")
        anomaly_enabled = getattr(self.options, "AnomalyEnabled")
        victoryCondition = getattr(self.options, "VictoryCondition")
        if not royalty_enabled and victoryCondition == 2:
            raise OptionError("Win condition cannot be Royalty while Royalty is disabled!")
        if not ideology_enabled and victoryCondition == 3:
            raise OptionError("Win condition cannot be Archonexus while Ideology is disabled!")
        if not anomaly_enabled and victoryCondition == 4:
            raise OptionError("Win condition cannot be Anomaly while Anomaly is disabled!")

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
        location_pool: Dict[str, int] = {}
        self.location_counts[self.player] = 0
        self.location_prerequisites[self.player] = {}
        self.progression_locations[self.player] = set()
        
        main_region = Region("Main", self.player, self.multiworld)

        basicResearchLocationCount = getattr(self.options, "BasicResearchLocationCount").value
        for i in range(basicResearchLocationCount):
            locationName = "Basic Research Location " + str(i)
            location_pool[locationName] = self.location_name_to_id[locationName]

        hiTechResearchLocationCount = getattr(self.options, "HiTechResearchLocationCount").value
        for i in range(hiTechResearchLocationCount):
            locationName = "Hi-Tech Research Location " + str(i)
            location_pool[locationName] = self.location_name_to_id[locationName]
            self.location_prerequisites[self.player][locationName] = ["Microelectronics"]
            self.progression_locations[self.player].add("Microelectronics")

        multiAnalyzerResearchLocationCount = getattr(self.options, "MultiAnalyzerResearchLocationCount").value
        for i in range(multiAnalyzerResearchLocationCount):
            locationName = "Multi-Analyzer Research Location " + str(i)
            location_pool[locationName] = self.location_name_to_id[locationName]
            self.location_prerequisites[self.player][locationName] = ["Microelectronics", "Multi-Analyzer"]
            self.progression_locations[self.player].add("Microelectronics")
            self.progression_locations[self.player].add("Multi-Analyzer")

        craftLocationCount = getattr(self.options, "CraftLocationCount").value
        royalty_disabled = not getattr(self.options, "RoyaltyEnabled")
        ideology_disabled = not getattr(self.options, "IdeologyEnabled")
        biotech_disabled = not getattr(self.options, "BiotechEnabled")
        anomaly_disabled = not getattr(self.options, "AnomalyEnabled")
        possibleItems = {}
        for itemId, itemName in list(self.craftable_item_id_to_name.items()):
            if royalty_disabled and self.item_name_to_expansion[itemName] == "Ludeon.RimWorld.Royalty":
                continue
            if ideology_disabled and self.item_name_to_expansion[itemName] == "Ludeon.RimWorld.Ideology":
                continue
            if biotech_disabled and self.item_name_to_expansion[itemName] == "Ludeon.RimWorld.Biotech":
                continue
            if anomaly_disabled and self.item_name_to_expansion[itemName] == "Ludeon.RimWorld.Anomaly":
                continue
            possibleItems[itemId] = itemName

        item_weights = {}
        total_weight = 0
        neolithic_weight = getattr(self.options, "NeolithicItemWeight")
        medieval_weight = getattr(self.options, "MedievalItemWeight")
        industrial_weight = getattr(self.options, "IndustrialItemWeight")
        spacer_weight = getattr(self.options, "SpacerItemWeight")
        hardtomake_weight = getattr(self.options, "HardToMakeItemWeight")
        anomaly_weight = getattr(self.options, "AnomalyItemWeight")
        for itemId in possibleItems:
            if self.craftable_item_tech_level[itemId] == "Neolithic":
                item_weights[itemId] = neolithic_weight
            if self.craftable_item_tech_level[itemId] == "Medieval":
                item_weights[itemId] = medieval_weight
            if self.craftable_item_tech_level[itemId] == "Industrial":
                item_weights[itemId] = industrial_weight
            if self.craftable_item_tech_level[itemId] == "Spacer":
                item_weights[itemId] = spacer_weight
            if self.craftable_item_tech_level[itemId] == "HardToMake":
                item_weights[itemId] = hardtomake_weight
            if self.craftable_item_tech_level[itemId] == "Anomaly":
                item_weights[itemId] = anomaly_weight
            total_weight += item_weights[itemId]

        for i in range(craftLocationCount):
            locationName = "Craft Location " + str(i)
            locationId = self.location_name_to_id[locationName]

            randomWeight = random.randrange(total_weight)
            for itemId in item_weights:
                if randomWeight < item_weights[itemId]:
                    itemId1 = itemId
                    itemName1 = self.craftable_item_id_to_name[itemId]
                    break
                else:
                    randomWeight -= item_weights[itemId]

            # Allows duplicate items - maybe fix it? Maybe who cares?
            randomWeight = random.randrange(total_weight)
            for itemId in item_weights:
                if randomWeight < item_weights[itemId]:
                    itemId2 = itemId
                    itemName2 = self.craftable_item_id_to_name[itemId]
                    break
                else:
                    randomWeight -= item_weights[itemId]

            prerequisites = list(set(self.craftable_item_id_to_prereqs[itemId1]) | set(self.craftable_item_id_to_prereqs[itemId2]))
            for item in prerequisites:
                self.progression_locations[self.player].add(item)
            self.location_prerequisites[self.player][locationName] = prerequisites
            self.craft_location_recipes[locationId] = [itemName1, itemName2]
            # print(self.player_name + "'s " + locationName + ": " + itemName1 + " + " + itemName2 + "(" + str(prerequisites) + ")")
            location_pool[locationName] = locationId

        self.location_counts[self.player] += len(location_pool)
        main_region.add_locations(location_pool, RimworldLocation)
        for locationName in location_pool:
            self.multiworld.get_location(locationName, self.player).progress_type = LocationProgressType.DEFAULT

        victoryCondition = getattr(self.options, "VictoryCondition")
        for itemList in generic_victory_requirements:
            for item in itemList: 
                self.progression_locations[self.player].add(item)
        # Any or Ship Launch
        if (victoryCondition == 0 or victoryCondition == 1):
            for itemList in ship_launch_victory_requirements:
                for item in itemList: 
                    self.progression_locations[self.player].add(item)
            self.location_prerequisites[self.player]["Space Victory"] = []
            main_region.locations.append(RimworldLocation(self.player, "Space Victory", None, main_region))
        # Any or Royalty
        if ((victoryCondition == 0 and not royalty_disabled) or victoryCondition == 2):
            for itemList in royalty_victory_requirements:
                for item in itemList: 
                    self.progression_locations[self.player].add(item)
            self.location_prerequisites[self.player]["Royalty Victory"] = []
            main_region.locations.append(RimworldLocation(self.player, "Royalty Victory", None, main_region))
        # Since Archonexus has lower strict requirements, I want the generator to only consider the
        #   other 3 victory conditions if the player opts for "any". Nexus still counts as "any", but
        #   this will ensure both Nexus and another victory are in logic.
        if (victoryCondition == 3):
            for itemList in archonexus_victory_requirements:
                for item in itemList: 
                    self.progression_locations[self.player].add(item)
            self.location_prerequisites[self.player]["Archonexus Victory"] = []
            main_region.locations.append(RimworldLocation(self.player, "Archonexus Victory", None, main_region))
        # Any or Anomaly
        if ((victoryCondition == 0 and not anomaly_disabled) or victoryCondition == 4):
            for itemList in anomaly_victory_requirements:
                for item in itemList: 
                    self.progression_locations[self.player].add(item)
            self.location_prerequisites[self.player]["Anomaly Victory"] = []
            main_region.locations.append(RimworldLocation(self.player, "Anomaly Victory", None, main_region))

        self.multiworld.regions.append(main_region)

        menu_region.connect(main_region)

    def create_item(self, item: str, classification: ItemClassification) -> RimworldItem:
        return RimworldItem(item, classification, self.item_name_to_id[item], self.player)

    def create_event(self, event: str) -> RimworldItem:
        return RimworldItem(event, ItemClassification.progression, None, self.player)

    def create_items(self) -> None:
        itempool = []
        royalty_disabled = not getattr(self.options, "RoyaltyEnabled")
        ideology_disabled = not getattr(self.options, "IdeologyEnabled")
        biotech_disabled = not getattr(self.options, "BiotechEnabled")
        anomaly_disabled = not getattr(self.options, "AnomalyEnabled")
        starting_research_level = getattr(self.options, "StartingResearchLevel")
        item_count = 0
        for item in self.item_name_to_id:
            if royalty_disabled and self.item_name_to_expansion[item] == "Ludeon.RimWorld.Royalty":
                continue
            if ideology_disabled and self.item_name_to_expansion[item] == "Ludeon.RimWorld.Ideology":
                continue
            if biotech_disabled and self.item_name_to_expansion[item] == "Ludeon.RimWorld.Biotech":
                continue
            if anomaly_disabled and self.item_name_to_expansion[item] == "Ludeon.RimWorld.Anomaly":
                continue
            # Removing items you start with from the pool
            if starting_research_level == 1 and item in self.tribal_tech_items:
                if item in self.progression_locations[self.player]:
                    itemClassification = ItemClassification.progression
                else:
                    itemClassification = ItemClassification.useful
                self.push_precollected(self.create_item(item, itemClassification))
                continue
            if starting_research_level == 2 and item in self.crashlanded_tech_items:
                if item in self.progression_locations[self.player]:
                    itemClassification = ItemClassification.progression
                else:
                    itemClassification = ItemClassification.useful
                self.push_precollected(self.create_item(item, itemClassification))
                continue

            item_count += 1
            if item in self.progression_locations[self.player]:
                itemClassification = ItemClassification.progression
            else:
                itemClassification = ItemClassification.useful
            itempool.append(self.create_item(item, itemClassification))
        
        if item_count < self.location_counts[self.player]:
            logger.warning("Player " + self.player_name + " had " + str(item_count) + " items, but " + str(self.location_counts[self.player]) + " locations! Adding filler.")
            while item_count < self.location_counts[self.player]:
                item_count += 1
                itempool.append(self.create_item("Temp Filler", ItemClassification.filler))
        self.multiworld.itempool += itempool

    def set_rules(self) -> None:
        for location in self.multiworld.get_locations(self.player):
            locationName = location.name
            if locationName in self.location_prerequisites[self.player]:
                # print("prereqs: " + locationName + ": " + str(self.location_prerequisites[self.player][locationName]))
                set_rule(self.get_location(locationName),
                    lambda state, prereqs = self.location_prerequisites[self.player][locationName]: state.has_all(prereqs, self.player))

        royalty_disabled = not getattr(self.options, "RoyaltyEnabled")
        anomaly_disabled = not getattr(self.options, "AnomalyEnabled")
        self.multiworld.completion_condition[self.player] = lambda state: state.has("Victory", self.player)
        victoryCondition = getattr(self.options, "VictoryCondition")
        if (victoryCondition == 0 or victoryCondition == 1):
            victoryLocation = self.get_location("Space Victory")
            for victoryRequirement in generic_victory_requirements:
                add_rule(victoryLocation, lambda state, req = victoryRequirement: state.has_any(req, self.player), "and")
            for victoryRequirement in ship_launch_victory_requirements:
                add_rule(victoryLocation, lambda state, req = victoryRequirement: state.has_any(req, self.player), "and")
            victoryLocation.place_locked_item(self.create_event("Victory"))
        if ((victoryCondition == 0 and not royalty_disabled) or victoryCondition == 2):
            victoryLocation = self.get_location("Royalty Victory")
            for victoryRequirement in generic_victory_requirements:
                add_rule(victoryLocation, lambda state, req = victoryRequirement: state.has_any(req, self.player), "and")
            for victoryRequirement in royalty_victory_requirements:
                add_rule(victoryLocation, lambda state, req = victoryRequirement: state.has_any(req, self.player), "and")
            victoryLocation.place_locked_item(self.create_event("Victory"))
        if (victoryCondition == 3):
            victoryLocation = self.get_location("Archonexus Victory")
            for victoryRequirement in generic_victory_requirements:
                add_rule(victoryLocation, lambda state, req = victoryRequirement: state.has_any(req, self.player), "and")
            for victoryRequirement in archonexus_victory_requirements:
                add_rule(victoryLocation, lambda state, req = victoryRequirement: state.has_any(req, self.player), "and")
            victoryLocation.place_locked_item(self.create_event("Victory"))
        if ((victoryCondition == 0 and not anomaly_disabled) or victoryCondition == 4):
            victoryLocation = self.get_location("Anomaly Victory")
            for victoryRequirement in generic_victory_requirements:
                add_rule(victoryLocation, lambda state, req = victoryRequirement: state.has_any(req, self.player), "and")
            for victoryRequirement in anomaly_victory_requirements:
                add_rule(victoryLocation, lambda state, req = victoryRequirement: state.has_any(req, self.player), "and")
            victoryLocation.place_locked_item(self.create_event("Victory"))
