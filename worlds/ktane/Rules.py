import typing
from ..generic.Rules import add_rule
#from .Regions import v6areas


def set_rules(multiworld, options, player):

    # sections rules
    menu_region = multiworld.get_region("Menu", player)
    section1_region = multiworld.get_region("Section 1", player)
    section2_region = multiworld.get_region("Section 2", player)
    section3_region = multiworld.get_region("Section 3", player)
    section4_region = multiworld.get_region("Section 4", player)
    section5_region = multiworld.get_region("Section 5", player)
    section6_region = multiworld.get_region("Section 6", player)

    menu_region.connect(connecting_region=section1_region, rule=lambda state: True)
    menu_region.connect(connecting_region=section2_region,
                        rule=lambda state: state.has("Bomb Fragment", player, 1))
    menu_region.connect(connecting_region=section3_region,
                        rule=lambda state: state.has("Bomb Fragment", player, 5))
    menu_region.connect(connecting_region=section4_region,
                        rule=lambda state: state.has("Bomb Fragment", player, 15))
    menu_region.connect(connecting_region=section5_region,
                        rule=lambda state: state.has("Bomb Fragment", player, 30))
    menu_region.connect(connecting_region=section6_region,
                        rule=lambda state: state.has("Bomb Fragment", player, 50))

    # bomb rules
    section1_region.connect(connecting_region=multiworld.get_region("Bomb 1.1", player),
                            rule=lambda state: True)

    section2_region.connect(connecting_region=multiworld.get_region("Bomb 2.1", player),
                            rule=lambda state: True)

    section2_region.connect(connecting_region=multiworld.get_region("Bomb 2.2", player),
                            rule=lambda state: state.has("Simon Says", player))

    section2_region.connect(connecting_region=multiworld.get_region("Bomb 2.3", player),
                            rule=lambda state: state.has("Memory", player))

    section2_region.connect(connecting_region=multiworld.get_region("Bomb 2.4", player),
                            rule=lambda state: state.has("Maze", player))

    section2_region.connect(connecting_region=multiworld.get_region("Bomb 2.5", player),
                            rule=lambda state: state.has("Who's on First", player))

    section2_region.connect(connecting_region=multiworld.get_region("Bomb 2.6", player),
                            rule=lambda state: state.has("Simon Says", player)
                                               and state.has("Memory", player)
                                               and state.has("Maze", player)
                                               and state.has("Who's on First", player)
                                               and state.has("Time++", player, 1))

    section3_region.connect(connecting_region=multiworld.get_region("Bomb 3.1", player),
                            rule=lambda state: state.has("Morse Code", player))

    section3_region.connect(connecting_region=multiworld.get_region("Bomb 3.2", player),
                            rule=lambda state: state.has("Password", player))

    section3_region.connect(connecting_region=multiworld.get_region("Bomb 3.3", player),
                            rule=lambda state: state.has("Complicated Wires", player))

    section3_region.connect(connecting_region=multiworld.get_region("Bomb 3.4", player),
                            rule=lambda state: state.has("Wire Sequence", player))

    section3_region.connect(connecting_region=multiworld.get_region("Bomb 3.5", player),
                            rule=lambda state: state.has("Simon Says", player)
                                               and state.has("Memory", player)
                                               and state.has("Maze", player)
                                               and state.has("Who's on First", player))

    section3_region.connect(connecting_region=multiworld.get_region("Bomb 3.6", player),
                            rule=lambda state: state.has("Complicated Wires", player)
                                               and state.has("Memory", player)
                                               and state.has("Maze", player)
                                               and state.has("Wire Sequence", player)
                                               and state.has("Password", player)
                                               and state.has("Morse Code", player)
                                               and state.has("Time++", player, 1))

    section3_region.connect(connecting_region=multiworld.get_region("Bomb 3.7", player),
                            rule=lambda state: state.has("Complicated Wires", player)
                                               and state.has("Wire Sequence", player))

    section3_region.connect(connecting_region=multiworld.get_region("Bomb 3.8", player),
                            rule=lambda state: state.has("Simon Says", player)
                                               and state.has("Maze", player)
                                               and state.has("Morse Code", player)
                                               and state.has("Time++", player, 2))

    section4_region.connect(connecting_region=multiworld.get_region("Bomb 4.1", player),
                            rule=lambda state: state.has("Who's on First", player)
                                               and state.has("Complicated Wires", player)
                                               and state.has("Capacitor", player)
                                               and state.has("Time++", player, 1))

    section4_region.connect(connecting_region=multiworld.get_region("Bomb 4.2", player),
                            rule=lambda state: state.has("Simon Says", player)
                                               and state.has("Memory", player)
                                               and state.has("Vent Gas", player)
                                               and state.has("Time++", player, 1))

    section4_region.connect(connecting_region=multiworld.get_region("Bomb 4.3", player),
                            rule=lambda state: state.has("Maze", player)
                                               and state.has("Morse Code", player)
                                               and state.has("Knob", player)
                                               and state.has("Time++", player, 1))

    section4_region.connect(connecting_region=multiworld.get_region("Bomb 4.4", player),
                            rule=lambda state: state.has("Maze", player)
                                               and state.has("Password", player)
                                               and state.has("Complicated Wires", player)
                                               and state.has("Wire Sequence", player)
                                               and state.has("Time++", player, 2))

    section5_region.connect(connecting_region=multiworld.get_region("Bomb 5.1", player),
                            rule=lambda state: state.has("Who's on First", player)
                                               and state.has("Time++", player, 2))

    section5_region.connect(connecting_region=multiworld.get_region("Bomb 5.2", player),
                            rule=lambda state: state.has("Maze", player)
                                               and state.has("Time++", player, 2))

    section5_region.connect(connecting_region=multiworld.get_region("Bomb 5.3", player),
                            rule=lambda state: state.has("Password", player)
                                               and state.has("Time++", player, 2))

    section5_region.connect(connecting_region=multiworld.get_region("Bomb 5.4", player),
                            rule=lambda state: state.has("Simon Says", player)
                                               and state.has("Morse Code", player)
                                               and state.has("Time++", player, 2))

    section5_region.connect(connecting_region=multiworld.get_region("Bomb 5.5", player),
                            rule=lambda state: state.has("Knob", player)
                                               and state.has("Capacitor", player)
                                               and state.has("Vent Gas", player)
                                               and state.has("Who's on First", player)
                                               and state.has("Maze", player)
                                               and state.has("Password", player)
                                               and state.has("Time++", player, 2))

    section5_region.connect(connecting_region=multiworld.get_region("Bomb 5.6", player),
                            rule=lambda state: state.has("Complicated Wires", player)
                                               and state.has("Simon Says", player)
                                               and state.has("Wire Sequence", player)
                                               and state.has("Time++", player, 2))

    section6_region.connect(connecting_region=multiworld.get_region("Bomb 6.1", player),
                            rule=lambda state: state.has("Knob", player)
                                               and state.has("Capacitor", player)
                                               and state.has("Vent Gas", player)
                                               and state.has("Who's on First", player)
                                               and state.has("Maze", player)
                                               and state.has("Memory", player)
                                               and state.has("Simon Says", player)
                                               and state.has("Morse Code", player)
                                               and state.has("Password", player)
                                               and state.has("Complicated Wires", player)
                                               and state.has("Wire Sequence", player)
                                               and state.has("Time++", player, 6))

    # section completed rules
    add_rule(multiworld.get_location("Section 1 Completed", player),
             lambda state: state.can_reach("1.1 The First Challenge - 3 Modules Solved", "Location", player))

    add_rule(multiworld.get_location("Section 2 Completed", player),
             lambda state: state.can_reach("2.1 Double Trouble - 6 Modules Solved", "Location", player)
                           and state.can_reach("2.2 Oh! The Lights! - 3 Modules Solved", "Location", player)
                           and state.can_reach("2.3 Remember - 3 Modules Solved", "Location", player)
                           and state.can_reach("2.4 Don't Get Lost - 3 Modules Solved", "Location", player)
                           and state.can_reach("2.5 Confusion - 3 Modules Solved", "Location", player)
                           and state.can_reach("2.6 Speedster I - 3 Modules Solved", "Location", player))

    add_rule(multiworld.get_location("Section 3 Completed", player),
             lambda state: state.can_reach("3.1 Back in the 40s - 3 Modules Solved", "Location", player)
                           and state.can_reach("3.2 Code Breaker - 3 Modules Solved", "Location", player)
                           and state.can_reach("3.3 Verticality - 3 Modules Solved", "Location", player)
                           and state.can_reach("3.4 Learning the Alphabet - 3 Modules Solved", "Location", player)
                           and state.can_reach("3.5 Precision Time - 4 Modules Solved", "Location", player)
                           and state.can_reach("3.6 Longer Bomb - 9 Modules Solved", "Location", player)
                           and state.can_reach("3.7 Rat Nest - 6 Modules Solved", "Location", player)
                           and state.can_reach("3.8 Speedster II - 5 Modules Solved", "Location", player))

    add_rule(multiworld.get_location("Section 4 Completed", player),
             lambda state: state.can_reach("4.1 Hold it! - 4 Modules Solved", "Location", player)
                           and state.can_reach("4.2 Master Hacker - 4 Modules Solved", "Location", player)
                           and state.can_reach("4.3 Wheel of Misfortune - 4 Modules Solved", "Location", player)
                           and state.can_reach("4.4 Speedster III - 4 Modules Solved", "Location", player))

    add_rule(multiworld.get_location("Section 5 Completed", player),
             lambda state: state.can_reach("5.1 Miscommunication - 4 Modules Solved", "Location", player)
                           and state.can_reach("5.2 Invisible Walls - 7 Modules Solved", "Location", player)
                           and state.can_reach("5.3 Cipher Decrypter - 9 Modules Solved", "Location", player)
                           and state.can_reach("5.4 Stroboscopic - 6 Modules Solved", "Location", player)
                           and state.can_reach("5.5 Attention Needed - 5 Modules Solved", "Location", player)
                           and state.can_reach("5.6 Speedster IV - 4 Modules Solved", "Location", player))

    # multiworld completion rule
    multiworld.completion_condition[player] = lambda state: state.can_reach("Bomb 6.1", 'Region', player)
