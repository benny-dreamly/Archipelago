from dataclasses import dataclass
from Options import Option, Range, DefaultOnToggle, PerGameCommonOptions
from BaseClasses import MultiWorld
from typing import Dict, Union, List


class UseRandomRuleSeed(DefaultOnToggle):
    """Use random puzzle solutions for the modules."""
    display_name = "Use Random Rule Seed"


class RuleSeed(Range):
    """If "Use Random Rule Seed" is set to false, define the custom rule seed used to solve the modules.
    Set to 1 to use vanilla rules."""
    display_name = "Rule Seed Number"
    range_start = 1
    range_end = 10000
    default = 1


@dataclass
class KTANEOptions(PerGameCommonOptions):
    random_rule_seed: UseRandomRuleSeed
    rule_seed: RuleSeed


def get_option_value(world: MultiWorld, player: int, name: str) -> Union[int, Dict, List]:
    option = getattr(world, name, None)
    if option is None:
        return 0

    return option[player].value
