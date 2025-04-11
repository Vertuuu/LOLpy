#NOTE: Unit testing like this surely isn't the best way to test a class, but it works for now. As the project grows, we will need to implement a more robust testing framework.

from LOLpy import ChampionImages
import os
from time import sleep

line_header = "=" * 50
line = "-" * 50
champion_name = "Briar" #change this to the champion you want to test(use the "key" from the API: https://cdn.merakianalytics.com/riot/lol/resources/latest/en-US/champions.json)

print(f"\n{line_header}\nChampionImages() class debug\n{line_header}\n")

#test if the ChampionImages() object can be created
try:
    champion = ChampionImages(champion_name, "en-US")
except Exception as e:
    print(f"Error creating ChampionImages() object: {e}⛔\n{line}")

#test if .get_champion_icon() method works
try:
    champion.get_icon()
    sleep(0.5)  # Wait for the image to be saved
    path = f"images/champion_imgs/{champion_name}_imgs/icon-{champion_name}.jpg"
    assert os.path.exists(path), "Champion icon not found"
    assert (os.path.getsize(path)>0), "Champion icon is empty"
    assert os.path.isfile(path), "Champion icon is not a file"
    print(f"Champion Icon saved successfully✅\n{line}")
except Exception as e:
    print(f"Error getting champion icon: {e}⛔\n{line}")

#test if .get_loading_screen_img() method works
try:
    champion.get_loading_screen_img()
    sleep(0.5)  # Wait for the image to be saved
    path = f"images/champion_imgs/{champion_name}_imgs/loading-{champion_name}.jpg"
    assert os.path.exists(path), "Champion loading screen image not found"
    assert (os.path.getsize(path)>0), "Champion loading screen image is empty"
    assert os.path.isfile(path), "Champion loading screen image is not a file"
    print(f"Champion Loading Screen image saved successfully✅\n{line}")
except Exception as e:
    print(f"Error getting champion loading screen image: {e}⛔\n{line}")

#test if .get_splash_art() method works
try:
    champion.get_splash_art()
    sleep(0.5)  # Wait for the image to be saved
    path = f"images/champion_imgs/{champion_name}_imgs/splash-{champion_name}.jpg"
    assert os.path.exists(path), "Champion splash art not found"
    assert (os.path.getsize(path)>0), "Champion splash art is empty"
    assert os.path.isfile(path), "Champion splash art is not a file"
    print(f"Champion Splash Art saved successfully✅\n{line}")
except Exception as e:
    print(f"Error getting champion splash art: {e}⛔\n{line}")

#test if .get_all_champion_images() method works
try:
    champion.get_all_champion_images()
    sleep(0.5)  # Wait for the images to be saved
    path = f"images/champion_imgs/{champion_name}_imgs/icon-{champion_name}.jpg"
    assert os.path.exists(path), "Champion icon not found"
    assert (os.path.getsize(path)>0), "Champion icon is empty"
    assert os.path.isfile(path), "Champion icon is not a file"
    path = f"images/champion_imgs/{champion_name}_imgs/loading-{champion_name}.jpg"
    assert os.path.exists(path), "Champion loading screen image not found"
    assert (os.path.getsize(path)>0), "Champion loading screen image is empty"
    assert os.path.isfile(path), "Champion loading screen image is not a file"
    path = f"images/champion_imgs/{champion_name}_imgs/splash-{champion_name}.jpg"
    assert os.path.exists(path), "Champion splash art not found"
    assert (os.path.getsize(path)>0), "Champion splash art is empty"
    assert os.path.isfile(path), "Champion splash art is not a file"
    print(f"All Champion Images saved successfully✅\n{line}")
except Exception as e:
    print(f"Error getting all champion images: {e}⛔\n{line}")

#test if .get_champion_skins() method works
try:
    skin_names = champion.get_champion_skins()
    sleep(0.5)  # Wait for the images to be saved
    for i in range(len(skin_names)):
        skin_name = skin_names[i].replace(" ", "_").replace("/", "_").replace("'", "_").replace(":", "_").replace("!", "_").replace(".", "_").replace(",", "_")
        path = f"images/champion_imgs/{champion_name}_imgs/skins/{champion_name}-{skin_name}.jpg"
        assert os.path.exists(path), f"Champion {skin_name} skin splash art not found"
        assert (os.path.getsize(path)>0), f"Champion {skin_name} skin splash art is empty"
        assert os.path.isfile(path), f"Champion {skin_name} skin splash art is not a file"
    print(f"Champion Skins saved successfully✅\n{line}")
except Exception as e:
    print(f"Error getting champion skins: {e}⛔\n{line}")

