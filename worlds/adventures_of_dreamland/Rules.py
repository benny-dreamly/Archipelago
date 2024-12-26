from worlds.generic.Rules import forbid_items_for_player, add_rule, set_rule
from typing import Optional, TypedDict, Dict, List, Tuple
from .data import LocationName, ItemName

class LocationLogic(TypedDict):
    name: str
    requires: Optional[Tuple[str]]

normal_logic_table: List[LocationLogic] = [
    {
        "name": LocationName.solve_3,
        "requires": (ItemName.pp3, ItemName.p3, ItemName.broom, ItemName.magnifying_glass),
     },
    {
        "name": LocationName.solve_4,
        "requires": (ItemName.pp4, ItemName.p4),
     },
    {"name": LocationName.pickup_hb, "requires": ItemName.hf_a},
    {"name": LocationName.pickup_hc, "requires": ItemName.hf_b},
    {"name": LocationName.pickup_hd, "requires": ItemName.hf_c},
    {"name": LocationName.pickup_he, "requires": ItemName.hf_d},
    {"name": LocationName.pickup_hf, "requires": ItemName.hf_e},
    {"name": LocationName.pickup_hg, "requires": ItemName.hf_f},
    {"name": LocationName.pickup_hh, "requires": ItemName.hf_g},
    {"name": LocationName.pickup_hi, "requires": ItemName.hf_h},
    {"name": LocationName.pickup_hj, "requires": ItemName.hf_i},
    {"name": LocationName.pickup_hk, "requires": ItemName.hf_j},
    {"name": LocationName.pickup_hl, "requires": ItemName.hf_k},
    {"name": LocationName.pickup_hm, "requires": ItemName.hf_l},
    {"name": LocationName.pickup_fc, "requires": ItemName.hf_m},
    {"name": LocationName.unlock_sfe, "requires": ItemName.p2},
    {"name": LocationName.pickup_pp2, "requires": ItemName.p2},
    {
        "name": LocationName.reassemble_h3,
        "requires": (
            ItemName.hf_a, ItemName.hf_b, ItemName.hf_c, ItemName.hf_d,
            ItemName.hf_e, ItemName.hf_f, ItemName.hf_g, ItemName.hf_h,
            ItemName.hf_i, ItemName.hf_j, ItemName.hf_k, ItemName.hf_l,
            ItemName.hf_m, ItemName.glue_stick
        ),
    },
    {
        "name": LocationName.decipher_h3,
        "requires": (
            ItemName.hf_a, ItemName.hf_b, ItemName.hf_c, ItemName.hf_d,
            ItemName.hf_e, ItemName.hf_f, ItemName.hf_g, ItemName.hf_h,
            ItemName.hf_i, ItemName.hf_j, ItemName.hf_k, ItemName.hf_l,
            ItemName.hf_m, ItemName.glue_stick, ItemName.h3
        )
    },
    {"name": LocationName.decipher_h1, "requires": (ItemName.h1, ItemName.c1, ItemName.c1_2)},
    {"name": LocationName.fill_bkt, "requires": ItemName.empty_bucket},
    {"name": LocationName.pickup_mg, "requires": ItemName.h3},
    {"name": LocationName.open_tdr, "requires": (ItemName.broom, ItemName.magnifying_glass)},
    {"name": LocationName.pickup_pp3, "requires": (ItemName.magnifying_glass, ItemName.broom)},
    {"name": LocationName.burn_bm, "requires": (ItemName.broom, ItemName.lighter, ItemName.filled_bucket, ItemName.empty_bucket)},
    {"name": LocationName.extinguish_fire, "requires": (ItemName.broom, ItemName.lighter, ItemName.filled_bucket, ItemName.empty_bucket)},
    {"name": LocationName.pickup_pp4, "requires": (ItemName.broom, ItemName.lighter, ItemName.filled_bucket, ItemName.empty_bucket)},
]


def create_rules(self):
    player = self.multiworld

    set_rule(self.multiworld.get_entrance("Cell Puzzle"), lambda state: state.can_solve_puzzle_1(player))
    set_rule(self.multiworld.get_entrance("Vault"))


def can_solve_puzzle_1(self, player):
    return self.has(ItemName.p1, player) and self.has(ItemName.pp1, player)

def can_solve_puzzle_2(self, player):
    return self.has(ItemName.p2, player) and self.has(ItemName.pp2, player)

