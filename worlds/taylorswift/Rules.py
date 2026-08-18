from __future__ import annotations

from typing import TYPE_CHECKING

from rule_builder.rules import Has, HasAll

from .Locations import LOCATION_TABLE
from .Regions import ALBUM_REGIONS

if TYPE_CHECKING:
    from . import TaylorSwiftWorld

VAULT_TRACKS_REQUIRED = Has("Vault Tracks")


def set_all_rules(world: TaylorSwiftWorld) -> None:
    set_all_location_rules(world)
    set_completion_condition(world)


def set_all_location_rules(world: TaylorSwiftWorld) -> None:
    for loc in world.multiworld.get_locations(world.player):
        data = LOCATION_TABLE[loc.name]
        if data.vault:
            world.set_rule(loc, VAULT_TRACKS_REQUIRED)


def set_completion_condition(world: TaylorSwiftWorld) -> None:
    required_items = []
    for album_name, option_name in ALBUM_REGIONS.items():
        if getattr(world.options, option_name).value:
            required_items.append(album_name)

    if world.options.include_vault_tracks.value:
        required_items.append("Vault Tracks")
    if world.options.include_re_recordings.value:
        required_items.append("Re-recordings")

    world.set_completion_rule(HasAll(*required_items))
