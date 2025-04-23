
from _configs import (DEBUG_IMAGES_ON)
from LOLpy import Champions, Champion, ChampionImages

line_header = "=" * 50
line = "-" * 50

print(f"\n{line_header}\nIntegration debug\n{line_header}\n")

#creating Champions() object
try:
    champions = Champions("en-US")
except Exception as e:
    print(f"Error creating Champions() object: {e}⛔\n{line}")

#getting champions keys
try:
    champions_keys = champions.get_champions_keys()
    assert type(champions_keys) == list, "Champions keys is not a list"
    assert len(champions_keys) > 0, "Champions keys list is empty"
    assert len(champions_keys) >= 170, "Champions keys list does not contain all champions"
    for champion in champions_keys:
        print(f"Champion Name: {champion}✅")
        assert type(champion) == str, "Champion key is not a string"
        assert len(champion) > 0, "Champion key is empty"
    print(f"{line}")
except Exception as e:
    print(f"Error getting champions keys: {e}⛔\n{line}")

for champion in champions_keys:
    try:
        champion_obj = Champion(champion, "en-US")
        
        key = champion_obj.get_champion_key()
        title = champion_obj.get_champion_title()
        id = champion_obj.get_champion_id()
        lanes = champion_obj.get_champion_lanes()
        resource = champion_obj.get_champion_resource()
        print(f"Champion's Info:\n")
        print(f"Key: {key}")
        print(f"Title: {title}")
        print(f"ID: {id}")
        print(f"Lanes: {lanes}")
        print(f"Resource: {resource}")
        print(f"{key}'s data retrieved successfully. ✅\n{line}")

        if DEBUG_IMAGES_ON:
            champion_img_obj = ChampionImages(champion, region="en-US")
            champion_img_obj.download_all_champion_images()
            champion_img_obj.download_champion_skins()
            print(f"{key}'s images retrieved successfully. ✅\n{line}")

    except Exception as e:
        print(f"Error: {e}⛔\n{line}")





