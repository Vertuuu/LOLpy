#NOTE: Unit testing like this surely isn't the best way to test a class, but it works for now. As the project grows, we will need to implement a more robust testing framework.

from _configs import (DEBUG_CHAMPION_NAME)
from LOLpy import  Champion

line_header = "=" * 50
line = "-" * 50

print(f"\n{line_header}\nChampion() class debug\n{line_header}\n")
#test if the Champion() object can be created
try:
    champion = Champion(DEBUG_CHAMPION_NAME, "en-US")
    print(f"Champion() object created. ✅\n{line}")
except Exception as e:
    print(f"Error creating Champion() object: {e}⛔\n{line}")

#test if .get_champion_key() method works 
print(f"\nTesting get_champion_key() method:")
try:
    key = champion.get_champion_key()
    print(f"Champion Key: {key}✅\n{line}")
except Exception as e:  
    print(f"Error getting champion key: {e}⛔\n{line}")

#test if .get_champion_name() method works 
print(f"\nTesting get_champion_name() method:")
try:
    name = champion.get_champion_name()
    assert type(name) == str, "Champion name is not a string"
    assert len(name)>0, "Champion name is an empty string"
    print(f"Champion Name: {name}✅\n{line}")
except Exception as e:  
    print(f"Error getting champion name: {e}⛔\n{line}")

#test if .get_champion_title() method works
print(f"\nTesting get_champion_title() method:")
try:
    title = champion.get_champion_title()
    print(f"Champion Title: {title}✅\n{line}")
except Exception as e:
    print(f"Error getting champion title: {e}⛔\n{line}")

#test if .get_champion_id() method works
print(f"\nTesting get_champion_id() method:")
try:
    id = champion.get_champion_id()
    assert type(id) == int, "Champion ID is not an integer"
    assert id > 0, "Champion ID is not greater than 0"
    print(f"Champion ID: {id}✅\n{line}")
except Exception as e:
    print(f"Error getting champion ID: {e}⛔\n{line}")

#test if .get_champion_lane() method works
print(f"\nTesting get_champion_lane() method:")
try:
    lanes = champion.get_champion_lanes()
    assert type(lanes) == list, "Champion lanes is not a list"
    assert len(lanes) > 0, "Champion lanes list is empty"
    for lane in lanes:
        assert type(lane) == str, "Champion lane is not a string"
        assert len(lane) > 0, "Champion lane is empty"
        assert lane in ["TOP", "MIDDLE", "BOTTOM", "JUNGLE", "SUPPORT"], "Champion lane is not in the list"
    print(f"Champion Lanes: {lanes}✅\n{line}")
except Exception as e:
    print(f"Error getting champion lane: {e}⛔\n{line}")

#test if .get_champion_resource() method works
print(f"\nTesting get_champion_resource() method: ")
try:
    resource = champion.get_champion_resource()
    assert type(resource) == str,  "Resource is not a string"
    assert len(resource)>1, "Resource is empty"
    assert resource in ["MANA", "BLOOD_WELL", "null", "HEALTH", "RAGE", "FURY", "FEROCITY", "NONE", "HEAT", "GRIT", "ENERGY", "OTHER", "FRENZY", "CRIMSON_RUSH"], "Invalid resource type"
    print(f"Champion Resource: {resource}✅\n{line}")
except Exception as e:
    print(f"Error getting champion resource: {e}⛔\n{line}")

#test if .get_champion_range() method works
print(f"Testing get_champion_range() method works")
try:
    range = champion.get_champion_range()
    assert type(range) == str, "Range is not a string"
    assert len(range)>0, "Range is empty"
    assert range in ["MELEE", "RANGED"], "Invalid range type"
    print(f"Champion Range: {range}✅\n{line}")
except Exception as e:
    print(f"Error getting champion range: {e}⛔\n{line}")

#test if .get_abilities_names() method works
print(f"Testing get_abilities_names() method: ")
try:
    abilities  = champion.get_abilities_names()
    assert type(abilities) == dict, "Abilities is not a dict"
    assert len(abilities) == 5, "Abilities dict doesn't have 5 items"
    for key in abilities.keys():
        assert key in ["P", "Q", "W", "E", "R"]
        assert type(abilities[key]) == str, "An ability is not a string"
        assert len(abilities[key])>0, "An ability is empty"
        print(f"Champion abilities: {abilities}✅\n{line}")
except Exception as e:
    print(f"Error getting champion abilities: {e}⛔\n{line}")

#test if .get_abilities_sources() method works
print(f"Testing get_abilities_sources() method: ")
try:
    sources  = champion.get_abilities_sources()
    assert type(sources) == dict, "Sources is not a dict"
    assert len(sources) == 5, "Sources dict doesn't have 5 items"
    for key in sources.keys():
        assert key in ["P", "Q", "W", "E", "R"]
        assert type(sources[key]) == str, "An ability is not a string"
        assert len(sources[key])>0, "An ability is empty"
        print(f"Champion sources: {sources}✅\n{line}")
except Exception as e:
    print(f"Error getting champion sources: {e}⛔\n{line}")

#test if .get_release_date() method works
print(f"Testing get_release_date() method: ")
try:
    release = champion.get_release_date()
    assert type(release) == str, "Release is not a date"
    assert release.count("-") == 2, "Wrong release date format"
    print(f"Champion release date: {release}✅\n{line}")
except Exception as e:
    print(f"Error getting champion release date: {e}⛔\n{line}")

#test if .get_price() method works
print(f"Testing get_price() method: ")
try:
    price = champion.get_price()
    assert type(price) == dict, "Prices aren't a dict"
    assert len(price) == 2, "Price doesn't have 2 items"
    for key in price:
        assert key in ["blueEssence", "rp"], "Wrong dict keys for prices"
        assert type(price[key]) == int, "A price is not an Int"
        assert price[key] >= 0, "A price is invalid"
    print(f"Champion price: {price}✅\n{line}")
except Exception as e:
    print(f"Error getting champion price: {e}⛔\n{line}")   



