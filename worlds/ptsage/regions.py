from __future__ import annotations

from typing import TYPE_CHECKING
# if fucky wucky needs entrances again
from BaseClasses import Region

if TYPE_CHECKING:
    from .world import SAGEWorld

# A region is a container for locations ("checks"), which connects to other regions via "Entrance" objects.
# Many games will model their Regions after physical in-game places, but you can also have more abstract regions.
# For a location to be in logic, its containing region must be reachable.
# The Entrances connecting regions can have rules - more on that in rules.py.
# This makes regions especially useful for traversal logic ("Can the player reach this part of the map?")

# Every location must be inside a region, and you must have at least one region.
# This is why we create regions first, and then later we create the locations (in locations.py).


def create_and_connect_regions(world: SAGEWorld) -> None:
    create_all_regions(world)
    connect_regions(world)


def create_all_regions(world: SAGEWorld) -> None:
    # Creating a region is as simple as calling the constructor of the Region class.
    pizzascape = Region("Pizzascape", world.player, world.multiworld)
    ancient_cheese = Region("Ancient Cheese", world.player, world.multiworld)
    bloodsauce_dungeon = Region("Bloodsauce Dungeon", world.player, world.multiworld)
    snick_challenge = Region("Snick's Challenge", world.player, world.multiworld)
    hub_area = world.get_region("Snick Amateur Games Expo")

    # Let's put all these regions in a list.
    regions = [pizzascape, ancient_cheese, bloodsauce_dungeon, snick_challenge, hub_area]

    # Some regions may only exist if the player enables certain options.
    # In our case, the Hammer locks the top middle chest in its own room if the hammer option is enabled.
    #if world.options.hammer:
        #top_middle_room = Region("Top Middle Room", world.player, world.multiworld)
        #regions.append(top_middle_room)

    # We now need to add these regions to multiworld.regions so that AP knows about their existence.
    world.multiworld.regions += regions


def connect_regions(world: SAGEWorld) -> None:
    # We have regions now, but still need to connect them to each other.
    # But wait, we no longer have access to the region variables we created in create_all_regions()!
    # Luckily, once you've submitted your regions to multiworld.regions,
    # you can get them at any time using world.get_region(...).
    pizzascape = world.get_region("Pizzascape")
    ancient_cheese = world.get_region("Ancient Cheese")
    bloodsauce_dungeon = world.get_region("Bloodsauce Dungeon")
    snick_challenge = world.get_region("Snick's Challenge")
    hub_area = world.get_region("Snick Amateur Games Expo")

    # Okay, now we can get connecting. For this, we need to create Entrances.
    # Entrances are inherently one-way, but crucially, AP assumes you can always return to the origin region.
    # One way to create an Entrance is by calling the Entrance constructor.
    #hub_to_pizzascape = Entrance(world.player, "Hub to Pizzascape", parent=hub_area)
    #hub_area.exits.append(hub_to_pizzascape)

    # You can then connect the Entrance to the target region.
    #hub_to_pizzascape.connect(pizzascape)

    # An even easier way is to use the region.connect helper.
    hub_area.connect(pizzascape, "Hub To Pizzascape", lambda state: state.has("Pizzascape Access", world.player))
    hub_area.connect(ancient_cheese, "Hub To Ancient Cheese", lambda state: state.has("Ancient Cheese Access", world.player))
    hub_area.connect(bloodsauce_dungeon, "Hub To Bloodsauce Dungeon", lambda state: state.has("Bloodsauce Dungeon Access", world.player))
    hub_area.connect(snick_challenge, "Hub to Snick's Challenge", lambda state: state.has("Snick's Challenge Access", world.player))

    # The region.connect helper even allows adding a rule immediately.
    # We'll talk more about rule creation in the set_all_rules() function in rules.py.
    #hub_area.connect(, "Overworld to Top Left Room", lambda state: state.has("Key", world.player))

    # Some Entrances may only exist if the player enables certain options.
    # In our case, the Hammer locks the top middle chest in its own room if the hammer option is enabled.
    # In this case, we previously created an extra "Top Middle Room" region that we now need to connect to Overworld.
    #if world.options.hammer:
        #top_middle_room = world.get_region("Top Middle Room")
        #overworld.connect(top_middle_room, "Overworld to Top Middle Room")
