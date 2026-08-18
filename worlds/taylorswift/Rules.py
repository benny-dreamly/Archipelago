from __future__ import annotations

from typing import TYPE_CHECKING

from .locations import LOCATION_TABLE
from .regions import ALBUM_REGIONS

if TYPE_CHECKING:
    from . import TaylorSwiftWorld


def set_all_rules(world: TaylorSwiftWorld) -> None:
    for loc in world.multiworld.get_locations(world.player):
        data = LOCATION_TABLE[loc.name]
        if data.vault:
            loc.access_rule = lambda state, r=data.region: state.has("Vault Tracks", world.player)


def set_completion_condition(world: TaylorSwiftWorld) -> None:
    required_items = []
    for album_name, option_name in ALBUM_REGIONS.items():
        if getattr(world.options, option_name).value:
            required_items.append(album_name)

    if world.options.include_vault_tracks.value:
        required_items.append("Vault Tracks")
    if world.options.include_re_recordings.value:
        required_items.append("Re-recordings")

    def victory_condition(state):
        return all(state.has(item, world.player) for item in required_items)

    world.multiworld.completion_condition[world.player] = victory_condition
