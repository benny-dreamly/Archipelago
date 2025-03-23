import typing
from dataclasses import dataclass
from Options import Option, Choice, PerGameCommonOptions, Range

max_research_locations = 200

class BasicResearchLocationCount(Range):
	display_name = "Basic Research Location Count"
	range_start = 0
	range_end = max_research_locations
	default = 55

class HiTechResearchLocationCount(Range):
	display_name = "Hi-Tech Research Location Count"
	range_start = 0
	range_end = max_research_locations
	default = 50

class MultiAnalyzerResearchLocationCount(Range):
	display_name = "Multi-Analyzer Research Location Count"
	range_start = 0
	range_end = max_research_locations
	default = 50

class ResearchBaseCost(Range):
	display_name = "Research Base Cost"
	range_start = 10
	range_end = 8000
	default = 500

@dataclass
class RimworldOptions(PerGameCommonOptions):
    BasicResearchLocationCount: BasicResearchLocationCount
    HiTechResearchLocationCount: HiTechResearchLocationCount
    MultiAnalyzerResearchLocationCount: MultiAnalyzerResearchLocationCount
    ResearchBaseCost: ResearchBaseCost
    

rimworld_options: typing.Dict[str, type(Option)] = {
	**{
		option.__name__: option
		for option in {
			BasicResearchLocationCount, HiTechResearchLocationCount, MultiAnalyzerResearchLocationCount,
			ResearchBaseCost
		}
	}
}