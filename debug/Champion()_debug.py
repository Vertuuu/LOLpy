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

