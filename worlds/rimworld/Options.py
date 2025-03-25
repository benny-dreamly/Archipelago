import typing
from dataclasses import dataclass
from Options import Option, Choice, PerGameCommonOptions, Range

max_research_locations = 200

class BasicResearchLocationCount(Range):
	display_name = "Basic Research Location Count"
	range_start = 0
	range_end = max_research_locations
	default = 35

class HiTechResearchLocationCount(Range):
	display_name = "Hi-Tech Research Location Count"
	range_start = 0
	range_end = max_research_locations
	default = 35

class MultiAnalyzerResearchLocationCount(Range):
	display_name = "Multi-Analyzer Research Location Count"
	range_start = 0
	range_end = max_research_locations
	default = 35

class ResearchBaseCost(Range):
	display_name = "Research Base Cost"
	range_start = 10
	range_end = 8000
	default = 500

class ResearchMaxPrerequisites(Range):
	display_name = "Research Max Prerequisites"
	range_start = 0
	range_end = 3
	default = 3

class CraftLocationCount(Range):
	display_name = "Craft Location Count"
	range_start = 0
	range_end = max_research_locations
	default = 50

@dataclass
class RimworldOptions(PerGameCommonOptions):
    BasicResearchLocationCount: BasicResearchLocationCount
    HiTechResearchLocationCount: HiTechResearchLocationCount
    MultiAnalyzerResearchLocationCount: MultiAnalyzerResearchLocationCount
    ResearchBaseCost: ResearchBaseCost
    ResearchMaxPrerequisites: ResearchMaxPrerequisites
    CraftLocationCount: CraftLocationCount
    

rimworld_options: typing.Dict[str, type(Option)] = {
	**{
		option.__name__: option
		for option in {
			BasicResearchLocationCount, HiTechResearchLocationCount, MultiAnalyzerResearchLocationCount,
			ResearchBaseCost, ResearchMaxPrerequisites, CraftLocationCount
		}
	}
}