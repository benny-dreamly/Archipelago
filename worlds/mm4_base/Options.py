from dataclasses import dataclass
from Options import Choice, Range, Toggle, DefaultOnToggle, Removed, PerGameCommonOptions, OptionSet, StartInventoryPool, DeathLink

class Goal(Toggle):
    """Game's Goal"""
    display_name = "Goal"


@dataclass
class MM4Options(PerGameCommonOptions):
    game_goal: Goal
    death_link: DeathLink
    
