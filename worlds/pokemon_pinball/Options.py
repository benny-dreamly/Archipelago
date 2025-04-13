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

class MapMove(Choice):
    """Controls what button is needed to move between areas during gameplay"""
    option_a     = 0b00000001 # A Button
    option_b     = 0b00000010 # B Button
    option_sel   = 0b00000100 # Select Button
    option_start = 0b00001000 # Start Button
    option_right = 0b00010000 # Right Button
    option_left  = 0b00100000 # Left Button
    option_up    = 0b01000000 # Up Button
    option_down  = 0b10000000 # Down Button
    default      = 0b00010000 # Right

class BalanceEncounter(DefaultOnToggle):
    """If enabled, will rebalance the encounter tables to make encountering rarer pokemon more common"""
    display_name = "Balanced Encounters"

class BallSaver(Toggle):
    """If enabled, the game will make the ball saved permanent"""
    display_name = "Permanent Ball Saver"

class StrongShake(Toggle):
    """If enabled, increases the strength of tilting, this can produce some odd results so use at your own risk"""

class ColorRando(Toggle):
    """If enabled, the game will randomize the colors of the Pokemon"""
    display_name = "Randomize Pokemon Colors"

class MapColor(Toggle):
    """If enabled, the game will randomize the colors of the maps"""
    display_name = "Randomize Map Colors"

@dataclass
class PokePinballOptions(PerGameCommonOptions):
    goal_dex: DexGoal
    dex_needed: DexNeed
    map_btn: MapMove
    rebalance_encounters: BalanceEncounter
    permanent_ball_saver: BallSaver
    strong_tilt: StrongShake
    mon_colors: ColorRando
    map_colors: MapColor
    death_link: DeathLink
    
