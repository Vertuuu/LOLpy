#NOTE: Unit testing like this surely isn't the best way to test a class, but it works for now. As the project grows, we will need to implement a more robust testing framework.
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from configs import (DEBUG_CHAMPION_NAME)
from LOLpy.LOLpy import Champion

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

