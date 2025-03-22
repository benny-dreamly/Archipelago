import typing
from dataclasses import dataclass
from Options import Option, Choice, PerGameCommonOptions, Range

max_research_locations = 250

class FakeOption(Choice):
    display_name = "Fake Option"
    option_vanilla = 0
    option_fake_option = 1
    default = 0

class ResearchLocationCount(Range):
	display_name = "Research Location Count"
	range_start = 50
	range_end = max_research_locations
	default = 155

class ResearchBaseCost(Range):
	display_name = "Research Base Cost"
	range_start = 10
	range_end = 8000
	default = 500

@dataclass
class RimworldOptions(PerGameCommonOptions):
    fake_option: FakeOption
    ResearchLocationCount: ResearchLocationCount
    ResearchBaseCost: ResearchBaseCost
    

rimworld_options: typing.Dict[str, type(Option)] = {
	**{
		option.__name__: option
		for option in {
			ResearchLocationCount, ResearchBaseCost
		}
	}
}