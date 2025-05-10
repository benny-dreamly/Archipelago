from typing import Callable, TYPE_CHECKING

from BaseClasses import CollectionState

if TYPE_CHECKING:
    from . import MM4World


def get_region_rules(player):
    return {
        "Example Region -> Example Region 2":
            lambda state: state.has("Example Item", player),

    }

def get_location_rules(player):
    return {
        "Example Location":
            lambda state: state.has("Example Item", player),
    }