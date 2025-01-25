from typing import TYPE_CHECKING

from worlds.AutoWorld import LogicMixin
from worlds.sims4.Names import SkillNames, CareerNames, AspirationNames
from .Options import Sims4Options
from ..generic.Rules import set_rule

if TYPE_CHECKING:
    from . import Sims4World


class Sims4Logic(LogicMixin):
    def _sims4_rule(self, player: int):
        return True


def set_rules(sims4_world: "Sims4World"):
    world = sims4_world.multiworld
    player = sims4_world.player
    options: Sims4Options = sims4_world.options



    # Career Rules
    # Athlete
    set_rule(world.get_location(CareerNames.base_career_athlete_3, player),
             lambda state: state.has(SkillNames.base_skill_charisma, player, count=1)
                           and state.has(SkillNames.base_skill_fitness, player, count=1))
    set_rule(world.get_location(CareerNames.base_career_athlete_4, player),
             lambda state: state.has(SkillNames.base_skill_charisma, player, count=2)
                           and state.has(SkillNames.base_skill_fitness, player, count=2))
    set_rule(world.get_location(CareerNames.base_career_athlete_5A, player),
             lambda state: state.has(SkillNames.base_skill_charisma, player, count=3)
                           and state.has(SkillNames.base_skill_fitness, player, count=3))
    set_rule(world.get_location(CareerNames.base_career_athlete_5B, player),
             lambda state: state.has(SkillNames.base_skill_charisma, player, count=3)
                           and state.has(SkillNames.base_skill_fitness, player, count=3))
    set_rule(world.get_location(CareerNames.base_career_athlete_6A, player),
             lambda state: state.has(SkillNames.base_skill_charisma, player, count=3)
                           and state.has(SkillNames.base_skill_fitness, player, count=4))
    set_rule(world.get_location(CareerNames.base_career_athlete_7A, player),
             lambda state: state.has(SkillNames.base_skill_charisma, player, count=3)
                           and state.has(SkillNames.base_skill_fitness, player, count=5))
    set_rule(world.get_location(CareerNames.base_career_athlete_8A, player),
             lambda state: state.has(SkillNames.base_skill_charisma, player, count=4)
                           and state.has(SkillNames.base_skill_fitness, player, count=7))
    set_rule(world.get_location(CareerNames.base_career_athlete_9A, player),
             lambda state: state.has(SkillNames.base_skill_charisma, player, count=5)
                           and state.has(SkillNames.base_skill_fitness, player, count=8))
    set_rule(world.get_location(CareerNames.base_career_athlete_10A, player),
             lambda state: state.has(SkillNames.base_skill_charisma, player, count=7)
                           and state.has(SkillNames.base_skill_fitness, player, count=9))
    set_rule(world.get_location(CareerNames.base_career_athlete_6B, player),
             lambda state: state.has(SkillNames.base_skill_charisma, player, count=4)
                           and state.has(SkillNames.base_skill_fitness, player, count=7))
    set_rule(world.get_location(CareerNames.base_career_athlete_7B, player),
             lambda state: state.has(SkillNames.base_skill_charisma, player, count=4)
                           and state.has(SkillNames.base_skill_fitness, player, count=8))
    set_rule(world.get_location(CareerNames.base_career_athlete_8B, player),
             lambda state: state.has(SkillNames.base_skill_charisma, player, count=5)
                           and state.has(SkillNames.base_skill_fitness, player, count=9))
    set_rule(world.get_location(CareerNames.base_career_athlete_9B, player),
             lambda state: state.has(SkillNames.base_skill_charisma, player, count=6)
                           and state.has(SkillNames.base_skill_fitness, player, count=9))
    set_rule(world.get_location(CareerNames.base_career_athlete_10B, player),
             lambda state: state.has(SkillNames.base_skill_charisma, player, count=7)
                           and state.has(SkillNames.base_skill_fitness, player, count=9))
    # Astronaut
    set_rule(world.get_location(CareerNames.base_career_astronaut_3, player),
             lambda state: state.has(SkillNames.base_skill_logic, player, count=1))
    set_rule(world.get_location(CareerNames.base_career_astronaut_4, player),
             lambda state: state.has(SkillNames.base_skill_logic, player, count=2)
                           and state.has(SkillNames.base_skill_fitness, player, count=1))
    set_rule(world.get_location(CareerNames.base_career_astronaut_5, player),
             lambda state: state.has(SkillNames.base_skill_logic, player, count=3)
                           and state.has(SkillNames.base_skill_fitness, player, count=2))
    set_rule(world.get_location(CareerNames.base_career_astronaut_6, player),
             lambda state: state.has(SkillNames.base_skill_logic, player, count=4)
                           and state.has(SkillNames.base_skill_fitness, player, count=3))
    set_rule(world.get_location(CareerNames.base_career_astronaut_7, player),
             lambda state: state.has(SkillNames.base_skill_logic, player, count=4)
                           and state.has(SkillNames.base_skill_fitness, player, count=5))
    set_rule(world.get_location(CareerNames.base_career_astronaut_8A, player),
             lambda state: state.has(SkillNames.base_skill_logic, player, count=5)
                           and state.has(SkillNames.base_skill_fitness, player, count=6))
    set_rule(world.get_location(CareerNames.base_career_astronaut_8B, player),
             lambda state: state.has(SkillNames.base_skill_logic, player, count=5)
                           and state.has(SkillNames.base_skill_fitness, player, count=6))
    set_rule(world.get_location(CareerNames.base_career_astronaut_9A, player),
             lambda state: state.has(SkillNames.base_skill_rocket_science, player, count=1)
                           and state.has(SkillNames.base_skill_fitness, player, count=7))
    set_rule(world.get_location(CareerNames.base_career_astronaut_10A, player),
             lambda state: state.has(SkillNames.base_skill_rocket_science, player, count=3)
                           and state.has(SkillNames.base_skill_fitness, player, count=9))
    set_rule(world.get_location(CareerNames.base_career_astronaut_9B, player),
             lambda state: state.has(SkillNames.base_skill_rocket_science, player, count=1)
                           and state.has(SkillNames.base_skill_fitness, player, count=7))
    set_rule(world.get_location(CareerNames.base_career_astronaut_10B, player),
             lambda state: state.has(SkillNames.base_skill_rocket_science, player, count=3)
                           and state.has(SkillNames.base_skill_fitness, player, count=9))
    # Business
    set_rule(world.get_location(CareerNames.base_career_business_3, player),
             lambda state: state.has(SkillNames.base_skill_charisma, player, count=1))
    set_rule(world.get_location(CareerNames.base_career_business_4, player),
             lambda state: state.has(SkillNames.base_skill_charisma, player, count=1)
                           and state.has(SkillNames.base_skill_logic, player, count=1))
    set_rule(world.get_location(CareerNames.base_career_business_5, player),
             lambda state: state.has(SkillNames.base_skill_charisma, player, count=2)
                           and state.has(SkillNames.base_skill_logic, player, count=1))
    set_rule(world.get_location(CareerNames.base_career_business_6, player),
             lambda state: state.has(SkillNames.base_skill_charisma, player, count=3)
                           and state.has(SkillNames.base_skill_logic, player, count=1))
    set_rule(world.get_location(CareerNames.base_career_business_7A, player),
             lambda state: state.has(SkillNames.base_skill_charisma, player, count=3)
                           and state.has(SkillNames.base_skill_logic, player, count=3))
    set_rule(world.get_location(CareerNames.base_career_business_7B, player),
             lambda state: state.has(SkillNames.base_skill_charisma, player, count=3)
                           and state.has(SkillNames.base_skill_logic, player, count=3))
    set_rule(world.get_location(CareerNames.base_career_business_8A, player),
             lambda state: state.has(SkillNames.base_skill_charisma, player, count=5)
                           and state.has(SkillNames.base_skill_logic, player, count=4))
    set_rule(world.get_location(CareerNames.base_career_business_9A, player),
             lambda state: state.has(SkillNames.base_skill_charisma, player, count=7)
                           and state.has(SkillNames.base_skill_logic, player, count=5))
    set_rule(world.get_location(CareerNames.base_career_business_10A, player),
             lambda state: state.has(SkillNames.base_skill_charisma, player, count=9)
                           and state.has(SkillNames.base_skill_logic, player, count=7))
    set_rule(world.get_location(CareerNames.base_career_business_8B, player),
             lambda state: state.has(SkillNames.base_skill_charisma, player, count=4)
                           and state.has(SkillNames.base_skill_logic, player, count=5))
    set_rule(world.get_location(CareerNames.base_career_business_9B, player),
             lambda state: state.has(SkillNames.base_skill_charisma, player, count=5)
                           and state.has(SkillNames.base_skill_logic, player, count=7))
    set_rule(world.get_location(CareerNames.base_career_business_10B, player),
             lambda state: state.has(SkillNames.base_skill_charisma, player, count=7)
                           and state.has(SkillNames.base_skill_logic, player, count=9))
    # Criminal
    set_rule(world.get_location(CareerNames.base_career_criminal_3, player),
             lambda state: state.has(SkillNames.base_skill_mischief, player, count=1))
    set_rule(world.get_location(CareerNames.base_career_criminal_4, player),
             lambda state: state.has(SkillNames.base_skill_mischief, player, count=2))
    set_rule(world.get_location(CareerNames.base_career_criminal_5, player),
             lambda state: state.has(SkillNames.base_skill_mischief, player, count=4))
    set_rule(world.get_location(CareerNames.base_career_criminal_6A, player),
             lambda state: state.has(SkillNames.base_skill_mischief, player, count=5))
    set_rule(world.get_location(CareerNames.base_career_criminal_6B, player),
             lambda state: state.has(SkillNames.base_skill_mischief, player, count=5))
    set_rule(world.get_location(CareerNames.base_career_criminal_7A, player),
             lambda state: state.has(SkillNames.base_skill_mischief, player, count=6))
    set_rule(world.get_location(CareerNames.base_career_criminal_8A, player),
             lambda state: state.has(SkillNames.base_skill_mischief, player, count=7)
                           and state.has(SkillNames.base_skill_handiness, player, count=1))
    set_rule(world.get_location(CareerNames.base_career_criminal_9A, player),
             lambda state: state.has(SkillNames.base_skill_mischief, player, count=8)
                           and state.has(SkillNames.base_skill_handiness, player, count=3))
    set_rule(world.get_location(CareerNames.base_career_criminal_10A, player),
             lambda state: state.has(SkillNames.base_skill_mischief, player, count=9)
                           and state.has(SkillNames.base_skill_handiness, player, count=5))
    set_rule(world.get_location(CareerNames.base_career_criminal_7B, player),
             lambda state: state.has(SkillNames.base_skill_mischief, player, count=6)
                           and state.has(SkillNames.base_skill_programming, player, count=1))
    set_rule(world.get_location(CareerNames.base_career_criminal_8B, player),
             lambda state: state.has(SkillNames.base_skill_mischief, player, count=7)
                           and state.has(SkillNames.base_skill_programming, player, count=3))
    set_rule(world.get_location(CareerNames.base_career_criminal_9B, player),
             lambda state: state.has(SkillNames.base_skill_mischief, player, count=8)
                           and state.has(SkillNames.base_skill_programming, player, count=5))
    set_rule(world.get_location(CareerNames.base_career_criminal_10B, player),
             lambda state: state.has(SkillNames.base_skill_mischief, player, count=9)
                           and state.has(SkillNames.base_skill_programming, player, count=7))
    # Culinary
    set_rule(world.get_location(CareerNames.base_career_culinary_3, player),
             lambda state: state.has(SkillNames.base_skill_cooking, player, count=1))
    set_rule(world.get_location(CareerNames.base_career_culinary_4, player),
             lambda state: state.has(SkillNames.base_skill_cooking, player, count=1)
                           and state.has(SkillNames.base_skill_mixology, player, count=1))
    set_rule(world.get_location(CareerNames.base_career_culinary_5, player),
             lambda state: state.has(SkillNames.base_skill_cooking, player, count=2)
                           and state.has(SkillNames.base_skill_mixology, player, count=2))
    set_rule(world.get_location(CareerNames.base_career_culinary_6A, player),
             lambda state: state.has(SkillNames.base_skill_cooking, player, count=3)
                           and state.has(SkillNames.base_skill_mixology, player, count=3))
    set_rule(world.get_location(CareerNames.base_career_culinary_6B, player),
             lambda state: state.has(SkillNames.base_skill_cooking, player, count=3)
                           and state.has(SkillNames.base_skill_mixology, player, count=3))
    set_rule(world.get_location(CareerNames.base_career_culinary_7A, player),
             lambda state: state.has(SkillNames.base_skill_cooking, player, count=5)
                           and state.has(SkillNames.base_skill_gourmet, player, count=1))
    set_rule(world.get_location(CareerNames.base_career_culinary_8A, player),
             lambda state: state.has(SkillNames.base_skill_cooking, player, count=7)
                           and state.has(SkillNames.base_skill_gourmet, player, count=5))
    set_rule(world.get_location(CareerNames.base_career_culinary_9A, player),
             lambda state: state.has(SkillNames.base_skill_cooking, player, count=7)
                           and state.has(SkillNames.base_skill_gourmet, player, count=5))
    set_rule(world.get_location(CareerNames.base_career_culinary_10A, player),
             lambda state: state.has(SkillNames.base_skill_cooking, player, count=9)
                           and state.has(SkillNames.base_skill_gourmet, player, count=7))
    set_rule(world.get_location(CareerNames.base_career_culinary_7B, player),
             lambda state: state.has(SkillNames.base_skill_mixology, player, count=4)
                           and state.has(SkillNames.base_skill_charisma, player, count=1))
    set_rule(world.get_location(CareerNames.base_career_culinary_8B, player),
             lambda state: state.has(SkillNames.base_skill_mixology, player, count=6)
                           and state.has(SkillNames.base_skill_charisma, player, count=3))
    set_rule(world.get_location(CareerNames.base_career_culinary_9B, player),
             lambda state: state.has(SkillNames.base_skill_mixology, player, count=7)
                           and state.has(SkillNames.base_skill_charisma, player, count=5))
    set_rule(world.get_location(CareerNames.base_career_culinary_10B, player),
             lambda state: state.has(SkillNames.base_skill_mixology, player, count=9)
                           and state.has(SkillNames.base_skill_charisma, player, count=7))
    # Entertainer
    set_rule(world.get_location(CareerNames.base_career_entertainer_3, player),
             lambda state: state.has(SkillNames.base_skill_guitar, player, count=1)
                           or state.has(SkillNames.base_skill_violin, player, count=1))
    set_rule(world.get_location(CareerNames.base_career_entertainer_4, player),
             lambda state: (state.has(SkillNames.base_skill_guitar, player, count=1)
                            or state.has(SkillNames.base_skill_violin, player, count=1))
                           and state.has(SkillNames.base_skill_comedy, player, count=1))
    set_rule(world.get_location(CareerNames.base_career_entertainer_5A, player),
             lambda state: (state.has(SkillNames.base_skill_guitar, player, count=2)
                            or state.has(SkillNames.base_skill_violin, player, count=2))
                           and state.has(SkillNames.base_skill_comedy, player, count=2))
    set_rule(world.get_location(CareerNames.base_career_entertainer_5B, player),
             lambda state: (state.has(SkillNames.base_skill_guitar, player, count=2)
                            or state.has(SkillNames.base_skill_violin, player, count=2))
                           and state.has(SkillNames.base_skill_comedy, player, count=2))
    set_rule(world.get_location(CareerNames.base_career_entertainer_6A, player),
             lambda state: state.has(SkillNames.base_skill_violin, player, count=3)
                           and state.has(SkillNames.base_skill_piano, player, count=1))
    set_rule(world.get_location(CareerNames.base_career_entertainer_7A, player),
             lambda state: (state.has(SkillNames.base_skill_guitar, player, count=4)
                            or state.has(SkillNames.base_skill_violin, player, count=4))
                           and state.has(SkillNames.base_skill_piano, player, count=3))
    set_rule(world.get_location(CareerNames.base_career_entertainer_8A, player),
             lambda state: (state.has(SkillNames.base_skill_guitar, player, count=5)
                            or state.has(SkillNames.base_skill_violin, player, count=5))
                           and state.has(SkillNames.base_skill_piano, player, count=5))
    set_rule(world.get_location(CareerNames.base_career_entertainer_9A, player),
             lambda state: (state.has(SkillNames.base_skill_guitar, player, count=6)
                            or state.has(SkillNames.base_skill_violin, player, count=6))
                           and state.has(SkillNames.base_skill_piano, player, count=7))
    set_rule(world.get_location(CareerNames.base_career_entertainer_10A, player),
             lambda state: (state.has(SkillNames.base_skill_guitar, player, count=7)
                            or state.has(SkillNames.base_skill_violin, player, count=7))
                           and state.has(SkillNames.base_skill_piano, player, count=9))
    set_rule(world.get_location(CareerNames.base_career_entertainer_6B, player),
             lambda state: state.has(SkillNames.base_skill_comedy, player, count=5))
    set_rule(world.get_location(CareerNames.base_career_entertainer_7B, player),
             lambda state: state.has(SkillNames.base_skill_comedy, player, count=6)
                           and state.has(SkillNames.base_skill_charisma, player, count=1))
    set_rule(world.get_location(CareerNames.base_career_entertainer_8B, player),
             lambda state: state.has(SkillNames.base_skill_comedy, player, count=7)
                           and state.has(SkillNames.base_skill_charisma, player, count=3))
    set_rule(world.get_location(CareerNames.base_career_entertainer_9B, player),
             lambda state: state.has(SkillNames.base_skill_comedy, player, count=8)
                           and state.has(SkillNames.base_skill_charisma, player, count=5))
    set_rule(world.get_location(CareerNames.base_career_entertainer_10B, player),
             lambda state: state.has(SkillNames.base_skill_comedy, player, count=9)
                           and state.has(SkillNames.base_skill_charisma, player, count=7))
    # Painter
    set_rule(world.get_location(CareerNames.base_career_painter_3, player),
             lambda state: state.has(SkillNames.base_skill_painting, player, count=1))
    set_rule(world.get_location(CareerNames.base_career_painter_4, player),
             lambda state: state.has(SkillNames.base_skill_painting, player, count=3))
    set_rule(world.get_location(CareerNames.base_career_painter_5, player),
             lambda state: state.has(SkillNames.base_skill_painting, player, count=4))
    set_rule(world.get_location(CareerNames.base_career_painter_6, player),
             lambda state: state.has(SkillNames.base_skill_painting, player, count=5))
    set_rule(world.get_location(CareerNames.base_career_painter_7A, player),
             lambda state: state.has(SkillNames.base_skill_painting, player, count=6))
    set_rule(world.get_location(CareerNames.base_career_painter_7B, player),
             lambda state: state.has(SkillNames.base_skill_painting, player, count=6))
    set_rule(world.get_location(CareerNames.base_career_painter_8A, player),
             lambda state: state.has(SkillNames.base_skill_painting, player, count=7)
                           and state.has(SkillNames.base_skill_logic, player, count=1))
    set_rule(world.get_location(CareerNames.base_career_painter_9A, player),
             lambda state: state.has(SkillNames.base_skill_painting, player, count=8)
                           and state.has(SkillNames.base_skill_logic, player, count=3))
    set_rule(world.get_location(CareerNames.base_career_painter_10A, player),
             lambda state: state.has(SkillNames.base_skill_painting, player, count=9)
                           and state.has(SkillNames.base_skill_logic, player, count=5))
    set_rule(world.get_location(CareerNames.base_career_painter_8B, player),
             lambda state: state.has(SkillNames.base_skill_painting, player, count=7)
                           and state.has(SkillNames.base_skill_charisma, player, count=1))
    set_rule(world.get_location(CareerNames.base_career_painter_9B, player),
             lambda state: state.has(SkillNames.base_skill_painting, player, count=8)
                           and state.has(SkillNames.base_skill_charisma, player, count=3))
    set_rule(world.get_location(CareerNames.base_career_painter_10B, player),
             lambda state: state.has(SkillNames.base_skill_painting, player, count=9)
                           and state.has(SkillNames.base_skill_charisma, player, count=5))
    # Secret Agent
    set_rule(world.get_location(CareerNames.base_career_secret_agent_3, player),
             lambda state: state.has(SkillNames.base_skill_logic, player, count=1))
    set_rule(world.get_location(CareerNames.base_career_secret_agent_4, player),
             lambda state: state.has(SkillNames.base_skill_logic, player, count=2)
                           and state.has(SkillNames.base_skill_charisma, player, count=2))
    set_rule(world.get_location(CareerNames.base_career_secret_agent_5, player),
             lambda state: state.has(SkillNames.base_skill_logic, player, count=2)
                           and state.has(SkillNames.base_skill_charisma, player, count=2))
    set_rule(world.get_location(CareerNames.base_career_secret_agent_6, player),
             lambda state: state.has(SkillNames.base_skill_logic, player, count=4)
                           and state.has(SkillNames.base_skill_charisma, player, count=4))
    set_rule(world.get_location(CareerNames.base_career_secret_agent_7, player),
             lambda state: state.has(SkillNames.base_skill_logic, player, count=4)
                           and state.has(SkillNames.base_skill_charisma, player, count=4))
    set_rule(world.get_location(CareerNames.base_career_secret_agent_8A, player),
             lambda state: state.has(SkillNames.base_skill_logic, player, count=5)
                           and state.has(SkillNames.base_skill_charisma, player, count=5))
    set_rule(world.get_location(CareerNames.base_career_secret_agent_8B, player),
             lambda state: state.has(SkillNames.base_skill_logic, player, count=5)
                           and state.has(SkillNames.base_skill_charisma, player, count=5))
    set_rule(world.get_location(CareerNames.base_career_secret_agent_9A, player),
             lambda state: state.has(SkillNames.base_skill_logic, player, count=7)
                           and state.has(SkillNames.base_skill_charisma, player, count=6))
    set_rule(world.get_location(CareerNames.base_career_secret_agent_10A, player),
             lambda state: state.has(SkillNames.base_skill_logic, player, count=9)
                           and state.has(SkillNames.base_skill_charisma, player, count=7))
    set_rule(world.get_location(CareerNames.base_career_secret_agent_9B, player),
             lambda state: state.has(SkillNames.base_skill_logic, player, count=7)
                           and state.has(SkillNames.base_skill_mischief, player, count=1))
    set_rule(world.get_location(CareerNames.base_career_secret_agent_10B, player),
             lambda state: state.has(SkillNames.base_skill_logic, player, count=9)
                           and state.has(SkillNames.base_skill_mischief, player, count=3))
    set_rule(world.get_location(CareerNames.base_career_secret_agent_11B, player),
             lambda state: state.has(SkillNames.base_skill_logic, player, count=9)
                           and state.has(SkillNames.base_skill_mischief, player, count=5))
    # Style Influencer
    set_rule(world.get_location(CareerNames.base_career_style_influencer_3, player),
             lambda state: state.has(SkillNames.base_skill_writing, player, count=1))
    set_rule(world.get_location(CareerNames.base_career_style_influencer_4, player),
             lambda state: state.has(SkillNames.base_skill_writing, player, count=2)
                           and state.has(SkillNames.base_skill_charisma, player, count=1))
    set_rule(world.get_location(CareerNames.base_career_style_influencer_5, player),
             lambda state: state.has(SkillNames.base_skill_writing, player, count=3)
                           and state.has(SkillNames.base_skill_photography, player, count=1))
    set_rule(world.get_location(CareerNames.base_career_style_influencer_6A, player),
             lambda state: state.has(SkillNames.base_skill_writing, player, count=4)
                           and state.has(SkillNames.base_skill_charisma, player, count=2)
                           and state.has(SkillNames.base_skill_painting, player, count=2))
    set_rule(world.get_location(CareerNames.base_career_style_influencer_7A, player),
             lambda state: state.has(SkillNames.base_skill_writing, player, count=5)
                           and state.has(SkillNames.base_skill_charisma, player, count=4)
                           and state.has(SkillNames.base_skill_painting, player, count=3)
                           and state.has(SkillNames.base_skill_photography, player, count=2))
    set_rule(world.get_location(CareerNames.base_career_style_influencer_8A, player),
             lambda state: state.has(SkillNames.base_skill_writing, player, count=6)
                           and state.has(SkillNames.base_skill_charisma, player, count=5)
                           and state.has(SkillNames.base_skill_painting, player, count=4))
    set_rule(world.get_location(CareerNames.base_career_style_influencer_9A, player),
             lambda state: state.has(SkillNames.base_skill_writing, player, count=7)
                           and state.has(SkillNames.base_skill_charisma, player, count=6)
                           and state.has(SkillNames.base_skill_painting, player, count=7))
    set_rule(world.get_location(CareerNames.base_career_style_influencer_10A, player),
             lambda state: state.has(SkillNames.base_skill_writing, player, count=8)
                           and state.has(SkillNames.base_skill_charisma, player, count=7)
                           and state.has(SkillNames.base_skill_painting, player, count=6))
    set_rule(world.get_location(CareerNames.base_career_style_influencer_6B, player),
             lambda state: state.has(SkillNames.base_skill_writing, player, count=4)
                           and state.has(SkillNames.base_skill_charisma, player, count=2)
                           and state.has(SkillNames.base_skill_painting, player, count=2))
    set_rule(world.get_location(CareerNames.base_career_style_influencer_7B, player),
             lambda state: state.has(SkillNames.base_skill_writing, player, count=5)
                           and state.has(SkillNames.base_skill_charisma, player, count=4)
                           and state.has(SkillNames.base_skill_painting, player, count=3)
                           and state.has(SkillNames.base_skill_photography, player, count=2))
    set_rule(world.get_location(CareerNames.base_career_style_influencer_8B, player),
             lambda state: state.has(SkillNames.base_skill_writing, player, count=6)
                           and state.has(SkillNames.base_skill_charisma, player, count=5)
                           and state.has(SkillNames.base_skill_painting, player, count=4))
    set_rule(world.get_location(CareerNames.base_career_style_influencer_9B, player),
             lambda state: state.has(SkillNames.base_skill_writing, player, count=7)
                           and state.has(SkillNames.base_skill_charisma, player, count=6)
                           and state.has(SkillNames.base_skill_painting, player, count=7))
    set_rule(world.get_location(CareerNames.base_career_style_influencer_10B, player),
             lambda state: state.has(SkillNames.base_skill_writing, player, count=8)
                           and state.has(SkillNames.base_skill_charisma, player, count=7)
                           and state.has(SkillNames.base_skill_painting, player, count=6))
    # Tech Guru
    set_rule(world.get_location(CareerNames.base_career_tech_guru_3, player),
             lambda state: state.has(SkillNames.base_skill_programming, player, count=1))
    set_rule(world.get_location(CareerNames.base_career_tech_guru_4, player),
             lambda state: state.has(SkillNames.base_skill_programming, player, count=2)
                           and state.has(SkillNames.base_skill_video_gaming, player, count=1))
    set_rule(world.get_location(CareerNames.base_career_tech_guru_5, player),
             lambda state: state.has(SkillNames.base_skill_programming, player, count=3)
                           and state.has(SkillNames.base_skill_video_gaming, player, count=2))
    set_rule(world.get_location(CareerNames.base_career_tech_guru_6, player),
             lambda state: state.has(SkillNames.base_skill_programming, player, count=4)
                           and state.has(SkillNames.base_skill_video_gaming, player, count=5))
    set_rule(world.get_location(CareerNames.base_career_tech_guru_7A, player),
             lambda state: state.has(SkillNames.base_skill_programming, player, count=5)
                           and state.has(SkillNames.base_skill_video_gaming, player, count=4))
    set_rule(world.get_location(CareerNames.base_career_tech_guru_7B, player),
             lambda state: state.has(SkillNames.base_skill_programming, player, count=5)
                           and state.has(SkillNames.base_skill_video_gaming, player, count=4))
    set_rule(world.get_location(CareerNames.base_career_tech_guru_8A, player),
             lambda state: state.has(SkillNames.base_skill_programming, player, count=5)
                           and state.has(SkillNames.base_skill_video_gaming, player, count=5))
    set_rule(world.get_location(CareerNames.base_career_tech_guru_9A, player),
             lambda state: state.has(SkillNames.base_skill_programming, player, count=6)
                           and state.has(SkillNames.base_skill_video_gaming, player, count=7))
    set_rule(world.get_location(CareerNames.base_career_tech_guru_10A, player),
             lambda state: state.has(SkillNames.base_skill_programming, player, count=7)
                           and state.has(SkillNames.base_skill_video_gaming, player, count=9))
    set_rule(world.get_location(CareerNames.base_career_tech_guru_8B, player),
             lambda state: state.has(SkillNames.base_skill_programming, player, count=6)
                           and state.has(SkillNames.base_skill_charisma, player, count=1))
    set_rule(world.get_location(CareerNames.base_career_tech_guru_9B, player),
             lambda state: state.has(SkillNames.base_skill_programming, player, count=8)
                           and state.has(SkillNames.base_skill_charisma, player, count=3))
    set_rule(world.get_location(CareerNames.base_career_tech_guru_10B, player),
             lambda state: state.has(SkillNames.base_skill_programming, player, count=9)
                           and state.has(SkillNames.base_skill_charisma, player, count=5))
    # Writer
    set_rule(world.get_location(CareerNames.base_career_writer_3, player),
             lambda state: state.has(SkillNames.base_skill_writing, player, count=1))
    set_rule(world.get_location(CareerNames.base_career_writer_4, player),
             lambda state: state.has(SkillNames.base_skill_writing, player, count=2))
    set_rule(world.get_location(CareerNames.base_career_writer_5, player),
             lambda state: state.has(SkillNames.base_skill_writing, player, count=3))
    set_rule(world.get_location(CareerNames.base_career_writer_6A, player),
             lambda state: state.has(SkillNames.base_skill_writing, player, count=4))
    set_rule(world.get_location(CareerNames.base_career_writer_6B, player),
             lambda state: state.has(SkillNames.base_skill_writing, player, count=4))
    set_rule(world.get_location(CareerNames.base_career_writer_7A, player),
             lambda state: state.has(SkillNames.base_skill_writing, player, count=6)
                           and state.has(SkillNames.base_skill_logic, player, count=1))
    set_rule(world.get_location(CareerNames.base_career_writer_8A, player),
             lambda state: state.has(SkillNames.base_skill_writing, player, count=7)
                           and state.has(SkillNames.base_skill_logic, player, count=2))
    set_rule(world.get_location(CareerNames.base_career_writer_9A, player),
             lambda state: state.has(SkillNames.base_skill_writing, player, count=8)
                           and state.has(SkillNames.base_skill_logic, player, count=3))
    set_rule(world.get_location(CareerNames.base_career_writer_10A, player),
             lambda state: state.has(SkillNames.base_skill_writing, player, count=9)
                           and state.has(SkillNames.base_skill_logic, player, count=4))
    set_rule(world.get_location(CareerNames.base_career_writer_7B, player),
             lambda state: state.has(SkillNames.base_skill_writing, player, count=6)
                           and state.has(SkillNames.base_skill_charisma, player, count=1))
    set_rule(world.get_location(CareerNames.base_career_writer_8B, player),
             lambda state: state.has(SkillNames.base_skill_writing, player, count=7)
                           and state.has(SkillNames.base_skill_charisma, player, count=2))
    set_rule(world.get_location(CareerNames.base_career_writer_9B, player),
             lambda state: state.has(SkillNames.base_skill_writing, player, count=8)
                           and state.has(SkillNames.base_skill_charisma, player, count=3))
    set_rule(world.get_location(CareerNames.base_career_writer_10B, player),
             lambda state: state.has(SkillNames.base_skill_writing, player, count=9)
                           and state.has(SkillNames.base_skill_charisma, player, count=4))
    # Part Time Jobs
    set_rule(world.get_location(CareerNames.base_ptj_babysitter_3, player),
             lambda state: state.has(SkillNames.base_skill_charisma, player, count=1))
    set_rule(world.get_location(CareerNames.base_ptj_barista_3, player),
             lambda state: state.has(SkillNames.base_skill_mixology, player, count=1))
    set_rule(world.get_location(CareerNames.base_ptj_fastfood_employee_3, player),
             lambda state: state.has(SkillNames.base_skill_cooking, player, count=1))
    set_rule(world.get_location(CareerNames.base_ptj_manual_laborer_3, player),
             lambda state: state.has(SkillNames.base_skill_gardening, player, count=1))
    set_rule(world.get_location(CareerNames.base_ptj_retail_employee_3, player),
             lambda state: state.has(SkillNames.base_skill_charisma, player, count=1))
    # Aspirations
    set_rule(world.get_location(AspirationNames.base_aspiration_exercise_demon, player),
             lambda state: state.has(SkillNames.base_skill_fitness, player, count=3))
    set_rule(world.get_location(AspirationNames.base_aspiration_fit_to_a_t, player),
             lambda state: state.has(SkillNames.base_skill_fitness, player, count=5))
    set_rule(world.get_location(AspirationNames.base_aspiration_bodybuilder, player),
             lambda state: state.has(SkillNames.base_skill_fitness, player, count=9))
    set_rule(world.get_location(AspirationNames.base_aspiration_fine_artist, player),
             lambda state: state.has(SkillNames.base_skill_painting, player, count=3))
    set_rule(world.get_location(AspirationNames.base_aspiration_brushing_with_greatness, player),
             lambda state: state.has(SkillNames.base_skill_painting, player, count=5))
    set_rule(world.get_location(AspirationNames.base_aspiration_painter_extraordinaire, player),
             lambda state: state.has(SkillNames.base_skill_painting, player, count=9))
    set_rule(world.get_location(AspirationNames.base_aspiration_competent_wordsmith, player),
             lambda state: state.has(SkillNames.base_skill_writing, player, count=3))
    set_rule(world.get_location(AspirationNames.base_aspiration_novelest_novelist, player),
             lambda state: state.has(SkillNames.base_skill_writing, player, count=5))
    set_rule(world.get_location(AspirationNames.base_aspiration_bestselling_author, player),
             lambda state: state.has(SkillNames.base_skill_writing, player, count=9))
    set_rule(world.get_location(AspirationNames.base_aspiration_fine_tuned, player),
             lambda state: state.has(SkillNames.base_skill_guitar, player, count=3)
                           or state.has(SkillNames.base_skill_violin, player, count=3)
                           or state.has(SkillNames.base_skill_piano, player, count=3))
    set_rule(world.get_location(AspirationNames.base_aspiration_harmonious, player),
             lambda state: state.has(SkillNames.base_skill_guitar, player, count=5)
                           or state.has(SkillNames.base_skill_violin, player, count=5)
                           or state.has(SkillNames.base_skill_piano, player, count=5))
    set_rule(world.get_location(AspirationNames.base_aspiration_musical_genius, player),
             lambda state: state.has(SkillNames.base_skill_guitar, player, count=9)
                           or state.has(SkillNames.base_skill_violin, player, count=9)
                           or state.has(SkillNames.base_skill_piano, player, count=9))
    set_rule(world.get_location(AspirationNames.base_aspiration_criminal_mind, player),
             lambda state: state.has(SkillNames.base_skill_mischief, player, count=2))
    set_rule(world.get_location(AspirationNames.base_aspiration_public_enemy, player),
             lambda state: state.has(SkillNames.base_skill_mischief, player, count=7)
                           and (state.has(SkillNames.base_skill_handiness, player, count=1)
                                or state.has(SkillNames.base_skill_programming, player, count=3)))
    set_rule(world.get_location(AspirationNames.base_aspiration_artful_trickster, player),
             lambda state: state.has(SkillNames.base_skill_mischief, player, count=2))
    set_rule(world.get_location(AspirationNames.base_aspiration_professional_prankster, player),
             lambda state: state.has(SkillNames.base_skill_mischief, player, count=5))
    set_rule(world.get_location(AspirationNames.base_aspiration_chief_of_mischief, player),
             lambda state: state.has(SkillNames.base_skill_mischief, player, count=9))
    set_rule(world.get_location(AspirationNames.base_aspiration_captain_cook, player),
             lambda state: state.has(SkillNames.base_skill_cooking, player, count=4))
    set_rule(world.get_location(AspirationNames.base_aspiration_culinary_artist, player),
             lambda state: state.has(SkillNames.base_skill_cooking, player, count=4)
                           and state.has(SkillNames.base_skill_mixology, player, count=1))
    set_rule(world.get_location(AspirationNames.base_aspiration_master_chef, player),
             lambda state: (state.has(SkillNames.base_skill_gourmet, player, count=5)
                            and state.has(SkillNames.base_skill_cooking, player, count=7))
                           or (state.has(SkillNames.base_skill_gourmet, player, count=4)
                               and state.has(SkillNames.base_skill_mixology, player, count=6)
                               and state.has(SkillNames.base_skill_charisma, player, count=3)))
    set_rule(world.get_location(AspirationNames.base_aspiration_electric_mixer, player),
             lambda state: state.has(SkillNames.base_skill_mixology, player, count=3))
    set_rule(world.get_location(AspirationNames.base_aspiration_beverage_boss, player),
             lambda state: state.has(SkillNames.base_skill_mixology, player, count=6)
                           and state.has(SkillNames.base_skill_cooking, player, count=3))
    set_rule(world.get_location(AspirationNames.base_aspiration_master_mixologist, player),
             lambda state: state.has(SkillNames.base_skill_mixology, player, count=9)
                           and state.has(SkillNames.base_skill_cooking, player, count=3))
    set_rule(world.get_location(AspirationNames.base_aspiration_prudent_student, player),
             lambda state: state.has(SkillNames.base_skill_logic, player, count=2))
    set_rule(world.get_location(AspirationNames.base_aspiration_jack_of_some_trades, player),
             lambda state: count_skills_over(3, state, player) >= 4)
    set_rule(world.get_location(AspirationNames.base_aspiration_pantologist, player),
             lambda state: count_skills_over(4, state, player) >= 5)
    set_rule(world.get_location(AspirationNames.base_aspiration_renaissance_sim, player),
             lambda state: count_skills_over(7, state, player) >= 6)
    set_rule(world.get_location(AspirationNames.base_aspiration_erudite, player),
             lambda state: state.has(SkillNames.base_skill_logic, player, count=5))
    set_rule(world.get_location(AspirationNames.base_aspiration_rocket_scientist, player),
             lambda state: state.has(SkillNames.base_skill_handiness, player, count=4))
    set_rule(world.get_location(AspirationNames.base_aspiration_nerd_brain, player),
             lambda state: state.has(SkillNames.base_skill_logic, player, count=9))
    set_rule(world.get_location(AspirationNames.base_aspiration_technically_adept, player),
             lambda state: state.has(SkillNames.base_skill_programming, player, count=2))
    set_rule(world.get_location(AspirationNames.base_aspiration_computer_geek, player),
             lambda state: state.has(SkillNames.base_skill_programming, player, count=2))
    set_rule(world.get_location(AspirationNames.base_aspiration_computer_whiz, player),
             lambda state: state.has(SkillNames.base_skill_programming, player, count=3)
                           and state.has(SkillNames.base_skill_video_gaming, player, count=2))
    set_rule(world.get_location(AspirationNames.base_aspiration_up_to_date, player),
             lambda state: state.has(SkillNames.base_skill_charisma, player, count=3))
    set_rule(world.get_location(AspirationNames.base_aspiration_romance_juggler, player),
             lambda state: state.has(SkillNames.base_skill_charisma, player, count=5))
    set_rule(world.get_location(AspirationNames.base_aspiration_serial_romantic, player),
             lambda state: state.has(SkillNames.base_skill_charisma, player, count=5))
    set_rule(world.get_location(AspirationNames.base_aspiration_garden_variety, player),
             lambda state: state.has(SkillNames.base_skill_gardening, player, count=3))
    set_rule(world.get_location(AspirationNames.base_aspiration_nature_nurturer, player),
             lambda state: state.has(SkillNames.base_skill_gardening, player, count=5))
    set_rule(world.get_location(AspirationNames.base_aspiration_freelance_botanist, player),
             lambda state: state.has(SkillNames.base_skill_gardening, player, count=9))
    set_rule(world.get_location(AspirationNames.base_aspiration_hooked, player),
             lambda state: state.has(SkillNames.base_skill_fishing, player, count=3))
    set_rule(world.get_location(AspirationNames.base_aspiration_reel_smart, player),
             lambda state: state.has(SkillNames.base_skill_fishing, player, count=5))
    set_rule(world.get_location(AspirationNames.base_aspiration_angling_ace, player),
             lambda state: state.has(SkillNames.base_skill_fishing, player, count=9))
    set_rule(world.get_location(AspirationNames.base_aspiration_practical_joker, player),
             lambda state: state.has(SkillNames.base_skill_comedy, player, count=2))
    set_rule(world.get_location(AspirationNames.base_aspiration_standup_startup, player),
             lambda state: state.has(SkillNames.base_skill_comedy, player, count=2))
    set_rule(world.get_location(AspirationNames.base_aspiration_funny, player),
             lambda state: state.has(SkillNames.base_skill_comedy, player, count=5)
                           and (state.has(SkillNames.base_skill_guitar, player, count=2)
                                or state.has(SkillNames.base_skill_violin, player, count=2)))
    set_rule(world.get_location(AspirationNames.base_aspiration_joke_star, player),
             lambda state: state.has(SkillNames.base_skill_comedy, player, count=9))
    set_rule(world.get_location(AspirationNames.base_aspiration_well_liked, player),
             lambda state: state.has(SkillNames.base_skill_charisma, player, count=3))
    set_rule(world.get_location(AspirationNames.base_aspiration_super_friend, player),
             lambda state: state.has(SkillNames.base_skill_charisma, player, count=5))
    set_rule(world.get_location(AspirationNames.base_aspiration_friend_of_the_world, player),
             lambda state: state.has(SkillNames.base_skill_charisma, player, count=9))
    set_rule(world.get_location(AspirationNames.base_aspiration_neighborly_advisor, player),
             lambda state: state.has(SkillNames.base_skill_charisma, player, count=6))

    # Skillchecks

    skills = {
        SkillNames.base_skill_comedy: 10,
        SkillNames.base_skill_charisma: 10,
        SkillNames.base_skill_logic: 10,
        SkillNames.base_skill_fitness: 10,
        SkillNames.base_skill_writing: 10,
        SkillNames.base_skill_fishing: 10,
        SkillNames.base_skill_gardening: 10,
        SkillNames.base_skill_video_gaming: 10,
        SkillNames.base_skill_programming: 10,
        SkillNames.base_skill_handiness: 10,
        SkillNames.base_skill_cooking: 10,
        SkillNames.base_skill_mixology: 10,
        SkillNames.base_skill_gourmet: 10,
        SkillNames.base_skill_mischief: 10,
        SkillNames.base_skill_piano: 10,
        SkillNames.base_skill_violin: 10,
        SkillNames.base_skill_guitar: 10,
        SkillNames.base_skill_painting: 10,
        SkillNames.base_skill_photography: 5,
        SkillNames.base_skill_rocket_science: 10,
    }

    for skill, max_count in skills.items():
        for count in range(1, max_count):
            set_rule(world.get_location(f"{skill} {count + 1}", player),
                     lambda state, c=count, s=skill: state.has(s, player, count=c))

    if options.goal.value == options.goal.option_bodybuilder:
        world.completion_condition[player] = lambda state: state.can_reach(
            world.get_location(AspirationNames.base_aspiration_bodybuilder, player), player=player)
    elif options.goal.value == options.goal.option_painter_extraordinaire:
        world.completion_condition[player] = lambda state: state.can_reach(
            world.get_location(AspirationNames.base_aspiration_painter_extraordinaire, player), player=player)
    elif options.goal.value == options.goal.option_bestselling_author:
        world.completion_condition[player] = lambda state: state.can_reach(
            world.get_location(AspirationNames.base_aspiration_bestselling_author, player), player=player)
    elif options.goal.value == options.goal.option_musical_genius:
        world.completion_condition[player] = lambda state: state.can_reach(
            world.get_location(AspirationNames.base_aspiration_musical_genius, player), player=player)
    elif options.goal.value == options.goal.option_public_enemy:
        world.completion_condition[player] = lambda state: state.can_reach(
            world.get_location(AspirationNames.base_aspiration_public_enemy, player), player=player)
    elif options.goal.value == options.goal.option_chief_of_mischief:
        world.completion_condition[player] = lambda state: state.can_reach(
            world.get_location(AspirationNames.base_aspiration_chief_of_mischief, player), player=player)
    elif options.goal.value == options.goal.option_successful_lineage:
        world.completion_condition[player] = lambda state: state.can_reach(
            world.get_location(AspirationNames.base_aspiration_successful_lineage, player), player=player)
    elif options.goal.value == options.goal.option_big_happy_family:
        world.completion_condition[player] = lambda state: state.can_reach(
            world.get_location(AspirationNames.base_aspiration_big_happy_family, player), player=player)
    elif options.goal.value == options.goal.option_master_chef:
        world.completion_condition[player] = lambda state: state.can_reach(
            world.get_location(AspirationNames.base_aspiration_master_chef, player), player=player)
    elif options.goal.value == options.goal.option_master_mixologist:
        world.completion_condition[player] = lambda state: state.can_reach(
            world.get_location(AspirationNames.base_aspiration_master_mixologist, player), player=player)
    elif options.goal.value == options.goal.option_fabulously_wealthy:
        world.completion_condition[player] = lambda state: state.can_reach(
            world.get_location(AspirationNames.base_aspiration_fabulously_wealthy, player), player=player)
    elif options.goal.value == options.goal.option_mansion_baron:
        world.completion_condition[player] = lambda state: state.can_reach(
            world.get_location(AspirationNames.base_aspiration_mansion_baron, player), player=player)
    elif options.goal.value == options.goal.option_renaissance_sim:
        world.completion_condition[player] = lambda state: state.can_reach(
            world.get_location(AspirationNames.base_aspiration_renaissance_sim, player), player=player)
    elif options.goal.value == options.goal.option_nerd_brain:
        world.completion_condition[player] = lambda state: state.can_reach(
            world.get_location(AspirationNames.base_aspiration_nerd_brain, player), player=player)
    elif options.goal.value == options.goal.option_computer_whiz:
        world.completion_condition[player] = lambda state: state.can_reach(
            world.get_location(AspirationNames.base_aspiration_computer_whiz, player), player=player)
    elif options.goal.value == options.goal.option_serial_romantic:
        world.completion_condition[player] = lambda state: state.can_reach(
            world.get_location(AspirationNames.base_aspiration_serial_romantic, player), player=player)
    elif options.goal.value == options.goal.option_soulmate:
        world.completion_condition[player] = lambda state: state.can_reach(
            world.get_location(AspirationNames.base_aspiration_soulmate, player), player=player)
    elif options.goal.value == options.goal.option_freelance_botanist:
        world.completion_condition[player] = lambda state: state.can_reach(
            world.get_location(AspirationNames.base_aspiration_freelance_botanist, player), player=player)
    elif options.goal.value == options.goal.option_the_curator:
        world.completion_condition[player] = lambda state: state.can_reach(
            world.get_location(AspirationNames.base_aspiration_the_curator, player), player=player)
    elif options.goal.value == options.goal.option_angling_ace:
        world.completion_condition[player] = lambda state: state.can_reach(
            world.get_location(AspirationNames.base_aspiration_angling_ace, player), player=player)
    elif options.goal.value == options.goal.option_joke_star:
        world.completion_condition[player] = lambda state: state.can_reach(
            world.get_location(AspirationNames.base_aspiration_joke_star, player), player=player)
    elif options.goal.value == options.goal.option_party_animal:
        world.completion_condition[player] = lambda state: state.can_reach(
            world.get_location(AspirationNames.base_aspiration_party_animal, player), player=player)
    elif options.goal.value == options.goal.option_friend_of_the_world:
        world.completion_condition[player] = lambda state: state.can_reach(
            world.get_location(AspirationNames.base_aspiration_friend_of_the_world, player), player=player)
    elif options.goal.value == options.goal.option_neighborly_advisor:
        world.completion_condition[player] = lambda state: state.can_reach(
            world.get_location(AspirationNames.base_aspiration_neighborly_advisor, player), player=player)


def count_skills_over(threshold: int, state, player) -> int:
    total_count = 0

    if state.has(SkillNames.base_skill_charisma, player, count=threshold):
        total_count += 1
    if state.has(SkillNames.base_skill_fitness, player, count=threshold):
        total_count += 1
    if state.has(SkillNames.base_skill_mischief, player, count=threshold):
        total_count += 1
    if state.has(SkillNames.base_skill_logic, player, count=threshold):
        total_count += 1
    if state.has(SkillNames.base_skill_cooking, player, count=threshold):
        total_count += 1
    if state.has(SkillNames.base_skill_mixology, player, count=threshold):
        total_count += 1
    if state.has(SkillNames.base_skill_comedy, player, count=threshold):
        total_count += 1
    if state.has(SkillNames.base_skill_writing, player, count=threshold):
        total_count += 1
    if state.has(SkillNames.base_skill_fishing, player, count=threshold):
        total_count += 1
    if state.has(SkillNames.base_skill_gardening, player, count=threshold):
        total_count += 1
    if state.has(SkillNames.base_skill_video_gaming, player, count=threshold):
        total_count += 1
    if state.has(SkillNames.base_skill_programming, player, count=threshold):
        total_count += 1
    if state.has(SkillNames.base_skill_photography, player, count=threshold):
        total_count += 1
    if state.has(SkillNames.base_skill_handiness, player, count=threshold):
        total_count += 1
    if state.has(SkillNames.base_skill_piano, player, count=threshold):
        total_count += 1
    if state.has(SkillNames.base_skill_violin, player, count=threshold):
        total_count += 1
    if state.has(SkillNames.base_skill_guitar, player, count=threshold):
        total_count += 1
    if state.has(SkillNames.base_skill_painting, player, count=threshold):
        total_count += 1
    if state.has(SkillNames.base_skill_rocket_science, player, count=threshold):
        total_count += 1
    if state.has(SkillNames.base_skill_gourmet, player, count=threshold):
        total_count += 1

    return total_count
