from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import ItemClassification, Location

from . import items

if TYPE_CHECKING:
    from .world import SAGEWorld

# Every location must have a unique integer ID associated with it.
# We will have a lookup from location name to ID here that, in world.py, we will import and bind to the world class.
# Even if a location doesn't exist on specific options, it must be present in this lookup.
LOCATION_NAME_TO_ID = {
    "Pizzascape Complete": 1,
    "Ancient Cheese Complete": 2,
    "Bloodsauce Dungeon Complete": 3,
    "Snick's Challenge Complete": 4,
    "Pizzascape S Rank": 5,
    "Ancient Cheese S Rank": 6,
    "Bloodsauce Dungeon S Rank": 7,
    "Pizzascape Toppin (Mushroom)": 8,
    "Pizzascape Toppin (Cheese)": 9,
    "Pizzascape Toppin (Tomato)": 10,
    "Pizzascape Toppin (Sausage)": 11,
    "Pizzascape Toppin (Pineapple)": 12,
    "Ancient Cheese Toppin (Mushroom)": 13,
    "Ancient Cheese Toppin (Cheese)": 14,
    "Ancient Cheese Toppin (Tomato)": 15,
    "Ancient Cheese Toppin (Sausage)": 16,
    "Ancient Cheese Toppin (Pineapple)": 17,
    "Bloodsauce Dungeon Toppin (Mushroom)": 13,
    "Bloodsauce Dungeon Toppin (Cheese)": 14,
    "Bloodsauce Dungeon Toppin (Tomato)": 15,
    "Bloodsauce Dungeon Toppin (Sausage)": 16,
    "Bloodsauce Dungeon Toppin (Pineapple)": 17,
    "Treasure (Pizzascape)": 18,
    "Treasure (Ancient Cheese)": 19,
    "Treasure (Bloodsauce Dungeon)": 20,
    "Pizzascape Secret 1": 21,
    "Pizzascape Secret 2": 22,
    "Pizzascape Secret 3": 23,
    "Pizzascape Secret 4": 24,
    "Pizzascape Secret 5": 25,
    "Pizzascape Secret 6": 26,
    "Ancient Cheese Secret 1": 27,
    "Ancient Cheese Secret 2": 28,
    "Ancient Cheese Secret 3": 29,
    "Ancient Cheese Secret 4": 30,
    "Ancient Cheese Secret 5": 31,
    "Ancient Cheese Secret 6": 32,
    "Bloodsauce Dungeon Secret 1": 33,
    "Bloodsauce Dungeon Secret 2": 34,
    "Bloodsauce Dungeon Secret 3": 35,
    "Bloodsauce Dungeon Secret 4": 36,
    "Bloodsauce Dungeon Secret 5": 37,
    "Bloodsauce Dungeon Secret 6": 38,

}


# Each Location instance must correctly report the "game" it belongs to.
# To make this simple, it is common practice to subclass the basic Location class and override the "game" field.
class SAGELocation(Location):
    game = "Pizza Tower SAGE Demo"


# Let's make one more helper method before we begin actually creating locations.
# Later on in the code, we'll want specific subsections of LOCATION_NAME_TO_ID.
# To reduce the chance of copy-paste errors writing something like {"Chest": LOCATION_NAME_TO_ID["Chest"]},
# let's make a helper method that takes a list of location names and returns them as a dict with their IDs.
# Note: There is a minor typing quirk here. Some functions want location addresses to be an "int | None",
# so while our function here only ever returns dict[str, int], we annotate it as dict[str, int | None].
def get_location_names_with_ids(location_names: list[str]) -> dict[str, int | None]:
    return {location_name: LOCATION_NAME_TO_ID[location_name] for location_name in location_names}


def create_all_locations(world: SAGEWorld) -> None:
    create_regular_locations(world)


def create_regular_locations(world: SAGEWorld) -> None:
    # Finally, we need to put the Locations ("checks") into their regions.
    # Once again, before we do anything, we can grab our regions we created by using world.get_region()
    pizzascape = world.get_region("Pizzascape")
    ancient_cheese = world.get_region("Ancient Cheese")
    bloodsauce_dungeon = world.get_region("Bloodsauce Dungeon")
    snick_challenge = world.get_region("Snick's Challenge")

    # One way to create locations is by just creating them directly via their constructor.
    #bottom_left_chest = SAGELocation(
        #world.player, "Bottom Left Chest", world.location_name_to_id["Bottom Left Chest"], overworld
    #)

    # You can then add them to the region.
    #overworld.locations.append(bottom_left_chest)

    # A simpler way to do this is by using the region.add_locations helper.
    # For this, you need to have a dict of location names to their IDs (i.e. a subset of location_name_to_id)
    # Aha! So that's why we made that "get_location_names_with_ids" helper method earlier.
    # You also need to pass your overridden Location class.
    pizzascape_locs = get_location_names_with_ids(["Pizzascape Complete", "Pizzascape S Rank", "Pizzascape Toppin (Mushroom)"
    "Pizzascape Toppin (Cheese)", "Pizzascape Toppin (Tomato)", "Pizzascape Toppin (Sausage)" "Pizzascape Toppin (Pineapple)"
    "Pizzascape Secret 1", "Pizzascape Secret 2", "Pizzascape Secret 3", "Pizzascape Secret 4", "Pizzascape Secret 5","Pizzascape Secret 6"])
    pizzascape.add_locations(pizzascape_locs, SAGELocation)

    ancient_cheese_locs = get_location_names_with_ids(["Ancient Cheese Complete", "Ancient Cheese S Rank", "Ancient Cheese Toppin (Mushroom)"
    "Ancient Cheese Toppin (Cheese)", "Ancient Cheese Toppin (Tomato)", "Ancient Cheese Toppin (Sausage)" "Ancient Cheese Toppin (Pineapple)"
    "Ancient Cheese Secret 1", "Ancient Cheese Secret 2", "Ancient Cheese Secret 3", "Ancient Cheese Secret 4", "Ancient Cheese Secret 5","Ancient Cheese Secret 6"])
    ancient_cheese.add_locations(ancient_cheese_locs, SAGELocation)

    bloodsauce_dungeon_locs = get_location_names_with_ids(["Bloodsauce Dungeon Complete", "Bloodsauce Dungeon S Rank", "Bloodsauce Dungeon Toppin (Mushroom)"
    "Bloodsauce Dungeon Toppin (Cheese)", "Bloodsauce Dungeon Toppin (Tomato)", "Bloodsauce Dungeon Toppin (Sausage)" "Bloodsauce Dungeon Toppin (Pineapple)"
    "Bloodsauce Dungeon Secret 1", "Bloodsauce Dungeon Secret 2", "Bloodsauce Dungeon Secret 3", "Bloodsauce Dungeon Secret 4", "Bloodsauce Dungeon Secret 5","Bloodsauce Dungeon Secret 6"])
    bloodsauce_dungeon.add_locations(bloodsauce_dungeon_locs, SAGELocation)

    snick_challenge_locs = get_location_names_with_ids(["Snick's Challenge Complete"])
    snick_challenge.add_locations(snick_challenge_locs, SAGELocation)

    # Locations may be in different regions depending on the player's options.
    # In our case, the hammer option puts the Top Middle Chest into its own room called Top Middle Room.
    #top_middle_room_locations = get_location_names_with_ids(["Top Middle Chest"])
    #if world.options.hammer:
        #top_middle_room = world.get_region("Top Middle Room")
        #top_middle_room.add_locations(top_middle_room_locations, APQuestLocation)
    #else:
        #overworld.add_locations(top_middle_room_locations, APQuestLocation)

    # Locations may exist only if the player enables certain options.
    # In our case, the extra_starting_chest option adds the Bottom Left Extra Chest location.
    if world.options.SRanks:
        # Once again, it is important to stress that even though the Bottom Left Extra Chest location doesn't always
        # exist, it must still always be present in the world's location_name_to_id.
        # Whether the location actually exists in the seed is purely determined by whether we create and add it here.
        srank_pizzascape = get_location_names_with_ids(["Pizzascape S Rank"])
        pizzascape.add_locations(srank_pizzascape, SAGELocation)

        srank_ancient_cheese = get_location_names_with_ids(["Ancient Cheese S Rank"])
        ancient_cheese.add_locations(srank_ancient_cheese, SAGELocation)

        srank_bloodsauce_dungeon = get_location_names_with_ids(["Bloodsauce Dungeon S Rank"])
        bloodsauce_dungeon.add_locations(srank_bloodsauce_dungeon, SAGELocation)


#def create_events(world: SAGEWorld) -> None:
    # Sometimes, the player may perform in-game actions that allow them to progress which are not related to Items.
    # In our case, the player must press a button in the top left room to open the final boss door.
    # AP has something for this purpose: "Event locations" and "Event items".
    # An event location is no different than a regular location, except it has the address "None".
    # It is treated during generation like any other location, but then it is discarded.
    # This location cannot be "sent" and its item cannot be "received", but the item can be used in logic rules.
    # Since we are creating more locations and adding them to regions, we need to grab those regions again first.
    #top_left_room = world.get_region("Top Left Room")
    #final_boss_room = world.get_region("Final Boss Room")

    # One way to create an event is simply to use one of the normal methods of creating a location.
    #button_in_top_left_room = APQuestLocation(world.player, "Top Left Room Button", None, top_left_room)
    #top_left_room.locations.append(button_in_top_left_room)

    # We then need to put an event item onto the location.
    # An event item is an item whose code is "None" (same as the event location's address),
    # and whose classification is "progression". Item creation will be discussed more in items.py.
    # Note: Usually, items are created in world.create_items(), which for us happens in items.py.
    # However, when the location of an item is known ahead of time (as is the case with an event location/item pair),
    # it is common practice to create the item when creating the location.
    # Since locations also have to be finalized after world.create_regions(), which runs before world.create_items(),
    # we'll create both the event location and the event item in our locations.py code.
    #button_item = items.APQuestItem("Top Left Room Button Pressed", ItemClassification.progression, None, world.player)
    #button_in_top_left_room.place_locked_item(button_item)

    # A way simpler way to do create an event location/item pair is by using the region.create_event helper.
    # Luckily, we have another event we want to create: The Victory event.
    # We will use this event to track whether the player can win the game.
    # The Victory event is a completely optional abstraction - This will be discussed more in set_rules().
    #world.region.snick_challenge.add_event(
        #"Snick's Challenge Complete", "Victory", location_type=SAGELocation, item_type=items.SAGEItem
    #)

    # If you create all your regions and locations line-by-line like this,
    # the length of your create_regions might get out of hand.
    # Many worlds use more data-driven approaches using dataclasses or NamedTuples.
    # However, it is worth understanding how the actual creation of regions and locations works,
    # That way, we're not just mindlessly copy-pasting! :)
