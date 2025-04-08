from dataclasses import dataclass
from Options import Choice, Range, Toggle, DefaultOnToggle, PerGameCommonOptions, StartInventoryPool, DeathLink

class DexGoal(DefaultOnToggle):
    """If enabled will require you to catch a certain number of Pokemon to clear the game"""
    display_name = "Dex Completion Goal"

class DexNeed(Range):
    """Determines how many Pokemon you need to catch to complete the game"""
    display_name = "Dex Completion Requirement"
    range_start = 50
    range_end = 150
    default = 100

@dataclass
class PokePinballOptions(PerGameCommonOptions):
    goal_dex: DexGoal
    dex_needed: DexNeed
    death_link: DeathLink
