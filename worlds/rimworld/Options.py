import typing
from dataclasses import dataclass
from Options import Option, Choice, PerGameCommonOptions, Range

max_research_locations = 200

class BasicResearchLocationCount(Range):
	"""
	The number of basic research locations in the game. These will only require the basic research bench.
	"""
	display_name = "Basic Research Location Count"
	range_start = 0
	range_end = max_research_locations
	default = 35

class HiTechResearchLocationCount(Range):
	"""
	The number of hi-tech research locations in the game. These will only require the hi-tech research bench (which requires Microelectronics.)
	"""
	display_name = "Hi-Tech Research Location Count"
	range_start = 0
	range_end = max_research_locations
	default = 35

class MultiAnalyzerResearchLocationCount(Range):
	"""
	The number of multi-analyzer research locations in the game. These will only require the hi-tech research bench and the multi-analyzer (and the research for them.)
	"""
	display_name = "Multi-Analyzer Research Location Count"
	range_start = 0
	range_end = max_research_locations
	default = 35

class ResearchBaseCost(Range):
	"""
	The amount of research points required to research research locations.
	"""
	display_name = "Research Base Cost"
	range_start = 10
	range_end = 8000
	default = 500

class ResearchMaxPrerequisites(Range):
	"""
	The max number of prerequisites for the generated Archipelago research. The higher this is, the more restricted your selection of research will be.
	"""
	display_name = "Research Max Prerequisites"
	range_start = 0
	range_end = 3
	default = 3

class CraftLocationCount(Range):
	"""
	The number of craft locations in the game. These locations require crafting two random items together.
	"""
	display_name = "Craft Location Count"
	range_start = 0
	range_end = 500
	default = 51

class VictoryCondition(Choice):
	"""
	The way to win. Choosing "any" will ensure one of these is considered "in-logic." They also require a "basic" set of research that isn't strictly required to win, so royalty will consider pianos and noble apparel in logic, while anomaly will consider basic bioferrite research in logic.
	"""
	display_name = "Victory Condition"
	option_any = 0
	option_ship_launch = 1
	option_royalty = 2
	option_archonexus = 3
	option_anomaly = 4
	default = 1

class RoyaltyEnabled(Choice):
	"""
	Enable the Royalty DLC. If you disable any DLC in yaml and enable it in client, all research will be researchable and excluded from the generator.
	"""
	display_name = "Royalty Enabled"
	option_disabled = 0
	option_enabled = 1
	default = 1

class IdeologyEnabled(Choice):
	"""
	Enable the Ideology DLC. If you disable any DLC in yaml and enable it in client, all research will be researchable and excluded from the generator.
	"""
	display_name = "Ideology Enabled"
	option_disabled = 0
	option_enabled = 1
	default = 1

class BiotechEnabled(Choice):
	"""
	Enable the Biotech DLC. If you disable any DLC in yaml and enable it in client, all research will be researchable and excluded from the generator.
	"""
	display_name = "Biotech Enabled"
	option_disabled = 0
	option_enabled = 1
	default = 1

class AnomalyEnabled(Choice):
	"""
	Enable the Anomaly DLC. If you disable any DLC in yaml and enable it in client, all research will be researchable and excluded from the generator.
	"""
	display_name = "Anomoly Enabled"
	option_disabled = 0
	option_enabled = 1
	default = 1

class StartingResearchLevel(Choice):
	"""
	If "none" is selected, the player will have access to NO research, regardless of starting scenario. Tribal and Crashlanded will give the player those starting research (regardless of starting scenario.)
	"""
	display_name = "Starting Research Level"
	option_none = 0
	option_tribal = 1
	option_crashlanded = 2
	default = 0

class NeolithicItemWeight(Range):
	"""
	How likely it will be that low/no-tech items are chosen for crafting locations. Higher weights make this category more likely. 0 will exempt it from the list. Note that these categories are slightly different than the vanilla "Tech Level," to help account for how challenging they are to craft.
	"""
	display_name = "Neolithic Item Weight"
	range_start = 0
	range_end = 100
	default = 60

class MedievalItemWeight(Range):
	"""
	How likely it will be that low-tech items are chosen for crafting locations. Higher weights make this category more likely. 0 will exempt it from the list. Note that these categories are slightly different than the vanilla "Tech Level," to help account for how challenging they are to craft.
	"""
	display_name = "Medieval Item Weight"
	range_start = 0
	range_end = 100
	default = 60

class IndustrialItemWeight(Range):
	"""
	How likely it will be that mid-tech items are chosen for crafting locations. Higher weights make this category more likely. 0 will exempt it from the list. Note that these categories are slightly different than the vanilla "Tech Level," to help account for how challenging they are to craft.
	"""
	display_name = "Industrial Item Weight"
	range_start = 0
	range_end = 100
	default = 30

class SpacerItemWeight(Range):
	"""
	How likely it will be that high-tech items are chosen for crafting locations. Higher weights make this category more likely. 0 will exempt it from the list. Note that these categories are slightly different than the vanilla "Tech Level," to help account for how challenging they are to craft.
	"""
	display_name = "Spacer Item Weight"
	range_start = 0
	range_end = 100
	default = 10

class HardToMakeItemWeight(Range):
	"""
	How likely it will be that complicated items are chosen for crafting locations. These items usually require specific/unique investment, like multiple advanced components and the like. Higher weights make this category more likely. 0 will exempt it from the list. Note that these categories are slightly different than the vanilla "Tech Level," to help account for how challenging they are to craft.
	"""
	display_name = "Hard To Make Item Weight"
	range_start = 0
	range_end = 100
	default = 1

class AnomalyItemWeight(Range):
	"""
	How likely it will be that Anomaly-specific items are chosen for crafting locations. These items will often require bioferrite, and investment into the anomaly expansion to craft. Higher weights make this category more likely. 0 will exempt it from the list. Note that these categories are slightly different than the vanilla "Tech Level," to help account for how challenging they are to craft.
	"""
	display_name = "Anomaly Item Weight"
	range_start = 0
	range_end = 100
	default = 10

@dataclass
class RimworldOptions(PerGameCommonOptions):
    BasicResearchLocationCount: BasicResearchLocationCount
    HiTechResearchLocationCount: HiTechResearchLocationCount
    MultiAnalyzerResearchLocationCount: MultiAnalyzerResearchLocationCount
    ResearchBaseCost: ResearchBaseCost
    ResearchMaxPrerequisites: ResearchMaxPrerequisites
    CraftLocationCount: CraftLocationCount
    VictoryCondition: VictoryCondition
    RoyaltyEnabled: RoyaltyEnabled
    IdeologyEnabled: IdeologyEnabled
    BiotechEnabled: BiotechEnabled
    AnomalyEnabled: AnomalyEnabled
    StartingResearchLevel: StartingResearchLevel
    NeolithicItemWeight: NeolithicItemWeight
    MedievalItemWeight: MedievalItemWeight
    IndustrialItemWeight: IndustrialItemWeight
    SpacerItemWeight: SpacerItemWeight
    HardToMakeItemWeight: HardToMakeItemWeight
    AnomalyItemWeight: AnomalyItemWeight
    

rimworld_options: typing.Dict[str, type(Option)] = {
	**{
		option.__name__: option
		for option in {
			BasicResearchLocationCount, HiTechResearchLocationCount, MultiAnalyzerResearchLocationCount,
			ResearchBaseCost, ResearchMaxPrerequisites, CraftLocationCount, VictoryCondition,
			RoyaltyEnabled, IdeologyEnabled, BiotechEnabled, AnomalyEnabled, StartingResearchLevel
		}
	}
}