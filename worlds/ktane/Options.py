from dataclasses import dataclass
from Options import Option, DeathLink, Range, Toggle, PerGameCommonOptions
from BaseClasses import MultiWorld
from typing import Dict, Union, List


class RuleSeed(Range):
    """Rule randomization for each module. Set to 1 to use vanilla rules."""
    display_name = "Rule Seed"
    range_start = 1
    range_end = 10000
    default = 1


@dataclass
class KTANEOptions(PerGameCommonOptions):
    rule_seed: RuleSeed


def get_option_value(world: MultiWorld, player: int, name: str) -> Union[int, Dict, List]:
    option = getattr(world, name, None)
    if option is None:
        return 0

    return option[player].value
