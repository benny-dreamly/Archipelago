from dataclasses import dataclass
from Options import Choice, Toggle, PerGameCommonOptions, Range, StartInventoryPool, DeathLink

class ZoneNaviation(Choice):
    """
    Determines how traversing regions should function
    Normal: Defeat the dastardly bomber in the base to progress to the next zone
    Key: Zone Keys will be added to the item pool to allow progression into the next region
    Open: Beach, Snow, and Desert Zones will all be open by default 
    Fantasy Region will always require the 4 medals to access
    """
    option_normal = 0
    option_key = 1
    option_open = 2
    default = 0

class PoolMedals(Toggle):
    """If enabled Adds the medals into the item pool
    Otherwise the 4 Medals will be earned by clearing dungeons"""
    display_name = "Pool Medals"

class Mapsanity(Toggle):
    """If enabled Every Room in a Dungeon will become seperate Locations"""
    display_name = "Mapsanity"

class Rocksanity(Toggle):
    """If enabled every hidden Elifan room will become a check"""
    display_name = "Rocksanity"

class KaraMultiply(Range):
    """Multiplies the amount of stats you gain from Karabon stat tiles"""
    auto_display_name = "Karabon Multiplier"
    range_start = 1
    range_end = 10
    default = 2

class BomberColor(Choice):
    """Determines Bomberman's Color Palette"""
    option_white = 0
    option_black = 1
    option_red = 2
    option_blue = 3
    default = 0

class BaseSpeed(Range):
    """Sets the base movement speed, the games vanilla base value is 2"""
    display_name = "Movement Speed"
    range_start = 2
    range_end = 8
    default = 4

class RandomEnemy(Toggle):
    """Randomizes Enemy objects in maps"""

class RandomMusic(Toggle):
    """Randomizes the music table every time the client is loaded"""
class RandomSound(Toggle):
    """Randomizes the Sound Effect table every time the client is loaded"""

class Autosave(Toggle):
    """If enabled will attempt to autosave between every map transition"""

class NPCSprite(Toggle):
    """If enabled NPCs will have a random sprite"""
    display_name = "Randomize NPC Sprites"

@dataclass
class BomberTOptions(PerGameCommonOptions):
    #color: ButtonColor
    #hard_mode: HardMode
    #start_inventory_from_pool: StartInventoryPool
    zone_navigation: ZoneNaviation
    pool_medals: PoolMedals
    mapsanity: Mapsanity
    rocksanity: Rocksanity
    random_enemy: RandomEnemy
    random_npc: NPCSprite
    move_speed: BaseSpeed
    kara_multiply: KaraMultiply
    bomber_color: BomberColor
    random_music: RandomMusic
    random_sound: RandomSound
    autosave: Autosave
    death_link: DeathLink
