from typing import Callable, TYPE_CHECKING

from BaseClasses import CollectionState

if TYPE_CHECKING:
    from . import PokePinballWorld

def getdexcount(state, player):
    from .Locations import location_table
    dex_count = 0
    for name, data in location_table.items():
        if data.address < 0x1C20A0:
            if state.has(name, player):
                dex_count +=1
    return dex_count

def get_region_rules(player, options):
    return {
        "Red Table -> Viridian Forest":
            lambda state: state.has("Viridian Forest", player),
        "Blue Table -> Viridian Forest":
            lambda state: state.has("Viridian Forest", player),
        "Red Table -> Pewter City":
            lambda state: state.has("Pewter City", player),
        "Blue Table -> Mt Moon":
            lambda state: state.has("Mt Moon", player),
        "Red Table -> Cerulean City":
            lambda state: state.has("Cerulean City", player),
        "Blue Table -> Cerulean City":
            lambda state: state.has("Cerulean City", player),
        "Red Table -> Vermilion City Seaside":
            lambda state: state.has("Vermilion City Seaside", player),
        "Blue Table -> Vermilion City Streets":
            lambda state: state.has("Vermilion City Streets", player),
        "Red Table -> Rock Mountain":
            lambda state: state.has("Rock Mountain", player),
        "Blue Table -> Rock Mountain":
            lambda state: state.has("Rock Mountain", player),
        "Red Table -> Lavender Town":
            lambda state: state.has("Lavender Town", player),
        "Blue Table -> Celadon City":
            lambda state: state.has("Celadon City", player),
        "Red Table -> Cycling Road":
            lambda state: state.has("Cycling Road", player),
        "Red Table -> Safari Zone":
            lambda state: state.has("Safari Zone", player),
        "Blue Table -> Safari Zone":
            lambda state: state.has("Safari Zone", player),
        "Blue Table -> Fuchsia City":
            lambda state: state.has("Fuchsia City", player),
        "Blue Table -> Saffron City":
            lambda state: state.has("Saffron City", player),
        "Red Table -> Seafoam Islands":
            lambda state: state.has("Seafoam Islands", player),
        "Red Table -> Cinnabar Island":
            lambda state: state.has("Cinnabar Island", player),
        "Blue Table -> Cinnabar Island":
            lambda state: state.has("Cinnabar Island", player),
        "Red Table -> Indigo Plateau":
            lambda state: state.has("Indigo Plateau", player),
        "Blue Table -> Indigo Plateau":
            lambda state: state.has("Indigo Plateau", player),
            
    }

def get_location_rules(player, options):
    return {
        "Pokedex Completed":
            lambda state: getdexcount(state, player) >= options.dex_needed.value
    }