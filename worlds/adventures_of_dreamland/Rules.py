from worlds.generic.Rules import forbid_items_for_player, add_rule, set_rule
from .data import LocationName, ItemName


def create_rules(self):
    player = self.player
    world = self.multiworld

    set_rule(world.get_location(LocationName.solve_1, player), lambda state: state.can_solve_puzzle_1(player))
    set_rule(world.get_location(LocationName.solve_2, player), lambda state: state.can_solve_puzzle_2(player))
    set_rule(world.get_location(LocationName.solve_3, player), lambda state: state.can_solve_puzzle_3(player))
    set_rule(world.get_location(LocationName.solve_4, player), lambda state: state.can_solve_puzzle_4(player))

    set_rule(world.get_location(LocationName.decipher_h1, player), lambda state: state.has(ItemName.h1, player) and state.has(ItemName.c1, player) and state.has(ItemName.c1_2, player))

    set_rule(world.get_location(LocationName.unlock_sfe, player), lambda state: state.can_unlock_safe(player))
    set_rule(world.get_location(LocationName.pickup_pp2, player), lambda state: state.can_unlock_safe(player))

    set_rule(world.get_location(LocationName.solve_2, player), lambda state: state.can_solve_puzzle_2(player))

    set_rule(world.get_location(LocationName.pickup_hb, player), lambda state: state.has(ItemName.hf_a, player))
    set_rule(world.get_location(LocationName.pickup_hc, player), lambda state: state.has(ItemName.hf_b, player))
    set_rule(world.get_location(LocationName.pickup_hd, player), lambda state: state.has(ItemName.hf_c, player))
    set_rule(world.get_location(LocationName.pickup_he, player), lambda state: state.has(ItemName.hf_d, player))
    set_rule(world.get_location(LocationName.pickup_hf, player), lambda state: state.has(ItemName.hf_e, player))
    set_rule(world.get_location(LocationName.pickup_hg, player), lambda state: state.has(ItemName.hf_f, player))
    set_rule(world.get_location(LocationName.pickup_hh, player), lambda state: state.has(ItemName.hf_g, player))
    set_rule(world.get_location(LocationName.pickup_hi, player), lambda state: state.has(ItemName.hf_h, player))
    set_rule(world.get_location(LocationName.pickup_hj, player), lambda state: state.has(ItemName.hf_i, player))
    set_rule(world.get_location(LocationName.pickup_hk, player), lambda state: state.has(ItemName.hf_j, player))
    set_rule(world.get_location(LocationName.pickup_hl, player), lambda state: state.has(ItemName.hf_k, player))
    set_rule(world.get_location(LocationName.pickup_hm, player), lambda state: state.has(ItemName.hf_l, player))
    set_rule(world.get_location(LocationName.pickup_fc, player), lambda state: state.has(ItemName.hf_m, player))

    set_rule(world.get_location(LocationName.reassemble_h3, player), lambda state: state.can_reassemble_hint(player))
    set_rule(world.get_location(LocationName.decipher_h3, player), lambda state: state.can_reassemble_hint and state.has(ItemName.h3, player))

    set_rule(world.get_location(LocationName.fill_bkt, player), lambda state: state.has(ItemName.empty_bucket, player))
    set_rule(world.get_location(LocationName.pickup_mg, player), lambda state: state.has(ItemName.h3, player))
    set_rule(world.get_location(LocationName.open_tdr, player), lambda state: state.has(ItemName.broom, player) and state.has(ItemName.magnifying_glass, player))
    set_rule(world.get_location(LocationName.pickup_pp3, player), lambda state: state.has(ItemName.broom, player) and state.has(ItemName.magnifying_glass, player))

    set_rule(world.get_location(LocationName.burn_bm, player), lambda state: state.has(ItemName.broom, player) and state.has(ItemName.lighter, player))
    set_rule(world.get_location(LocationName.extinguish_fire, player), lambda state: state.can_reach_location(LocationName.burn_bm, player) and state.has(ItemName.filled_bucket, player))
    set_rule(world.get_location(LocationName.pickup_pp4, player), lambda state: state.can_reach_location(LocationName.extinguish_fire, player))
    set_rule(world.get_location(LocationName.unlock_ed, player), lambda state: state.has(ItemName.key))


    world.completion_condition[player] = lambda state: state.can_reach(world.get_location(LocationName.unlock_ed, player), player=player)

def can_solve_puzzle_1(self, player):
    return self.has(ItemName.p1, player) and self.has(ItemName.pp1, player)

def can_solve_puzzle_2(self, player):
    return self.has(ItemName.p2, player) and self.has(ItemName.pp2, player)

def can_solve_puzzle_3(self, player):
    return self.has(ItemName.p3, player) and self.has(ItemName.pp3, player)

def can_solve_puzzle_4(self, player):
    return self.has(ItemName.p4, player) and self.has(ItemName.pp4, player)

def can_unlock_safe(self, player):
    return self.can_solve_puzzle_1(player) and self.has(ItemName.p2, player)

def can_reassemble_hint(self, player):
    return (self.has(ItemName.hf_a, player) and self.has(ItemName.hf_b, player) and self.has(ItemName.hf_c, player) and self.has(ItemName.hf_d, player)
            and self.has(ItemName.hf_e, player) and self.has(ItemName.hf_f, player) and self.has(ItemName.hf_g, player)
            and self.has(ItemName.hf_h, player) and self.has(ItemName.hf_i, player) and self.has(ItemName.hf_j, player)
            and self.has(ItemName.hf_k, player) and self.has(ItemName.hf_l, player) and self.has(ItemName.hf_m, player)
            and self.has(ItemName.glue_stick, player))