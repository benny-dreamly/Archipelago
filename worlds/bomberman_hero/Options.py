from dataclasses import dataclass
from Options import Choice, Range, Toggle, DefaultOnToggle, Removed, PerGameCommonOptions, StartInventoryPool, DeathLink

class Goal(Choice):
    """
    Required Goal to complete the seed
    Bagular - Clear the game by defeating the final boss, unlocked by collecting enough adok bombs
    Adok Bombs - Clear the game by getting enough Adok Bombs for shorter seeds
    Clears - Clear the game by beating a certain number of stages
    """
    #display_name = "Goal"
    option_bagular = 0
    option_adokbombs = 1
    option_clears = 2
    default = 0


class AdokBombs(Range):
    """Number of Adok Bombs required to access Garaden
    If Adok Bomb Goal is Selected then this determines the number of Cards 
    Needed to hit your goal"""
    display_name = "Required Adok Bombs"
    range_start = 10
    range_end = 64
    default = 24


class MaxAdokBobms(Range):
    """Total number of Adok Bombs in the pool"""
    display_name = "Total Adok Bombs"
    range_start = 10
    range_end = 64
    default = 28

class ClearScore(Range):
    """Required clear points to collect the clear score checks."""
    range_start = 2
    range_end = 5
    default = 5

class StageTotal(Range):
    """Total number of stages needed to beat the game with Clear Goal"""
    range_start = 30
    range_end = 67
    default = 67

class ItemPowerup(DefaultOnToggle):
    """Fireups and Bombups become permanent powerups but collecting the ones in the stages will do nothing, 
    when turned off reciveing these items will just act like the collectable."""
    display_name="Pool Item Powerups"
class ItemHeart(Toggle):
    """Adds permanent max health upgrades into the item pool.
    when turned off you increase your max health by collecting 200 gems."""
    display_name="Pool Max Health"
class GemChecks(Range):
    """Determines how many locations for gems are added to the location pool."""
    range_start = 4
    range_end = 10
    default = 5

class GemRequire(Range):
    """How many Gems are required for each Gem Check"""
    range_start = 50
    range_end = 250
    default = 200

class Radiosanity(Toggle):
    """Collecting radios will be included as checks"""

class SecondStage(Toggle):
    """Will unlock a random second stage at the start of the run"""

class RandomMusic(Toggle):
    """Randomizes the music table every time the client is loaded"""

class RandomSound(Toggle):
    """Randomizes the sound table every time the client is loaded"""

class RandomSkybox(Toggle):
    """Randomizes the skybox table every time the client is loaded"""

@dataclass
class BombHOptions(PerGameCommonOptions):
    #start_inventory_from_pool: StartInventoryPool
    #open_stages: OpenStages
    adok_bombs: AdokBombs
    game_goal: Goal
    stage_total: StageTotal
    two_stage: SecondStage
    max_adok: MaxAdokBobms
    random_sounds: RandomSound
    random_sky: RandomSkybox
    random_music: RandomMusic
    clear_points: ClearScore
    item_powerups: ItemPowerup
    item_health: ItemHeart
    gem_check_total: GemChecks
    needed_gem: GemRequire
    radio: Radiosanity
    #difficulty: HardMode
    death_link: DeathLink
