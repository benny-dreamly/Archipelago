import typing
from dataclasses import dataclass
from Options import Option, Choice, PerGameCommonOptions, Range

class FakeOption(Choice):
    display_name = "Fake Option"
    option_vanilla = 0
    option_fake_option = 1
    default = 0

class ResearchLocationCount(Range):
	display_name = "Research Location Count"
	range_start = 50
	range_end = 155
	default = 69

@dataclass
class RimworldOptions(PerGameCommonOptions):
    fake_option: FakeOption
    ResearchLocationCount: ResearchLocationCount
    

rimworld_options: typing.Dict[str, type(Option)] = {
	**{
		option.__name__: option
		for option in {
			ResearchLocationCount
		}
	}
}