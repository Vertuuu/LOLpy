#NOTE: Unit testing like this surely isn't the best way to test a class, but it works for now. As the project grows, we will need to implement a more robust testing framework.

import os
import requests
from _configs import (DEBUG_CHAMPION_NAME, DEBUG_IMAGES_DIR)
from LOLpy import ChampionImages
from time import sleep

line_header = "=" * 50
line = "-" * 50

print(f"\n{line_header}\nChampionImages() class debug\n{line_header}\n")

#test if the ChampionImages() object can be created
try:
    champion = ChampionImages(DEBUG_CHAMPION_NAME, region="en-US")
    print(f"ChampionImages() object created. ✅\n{line}")
except Exception as e:
    print(f"Error creating ChampionImages() object: {e}⛔\n{line}")

#test if .get_icon_source() method works
print(f"\nTesting get_icon_source() method:")
try:
    source = champion.get_icon_source()     
    assert requests.get(source).status_code == 200, f"Trying to GET URL {source} didn't return 200"
    print(f"Champion Icon's source working✅\n{line}")
except Exception as e:
    print(f"Error getting to champion icon's source: {e}⛔\n{line}")

#test if .get_loading_screen_source() method works
print(f"\nTesting get_loading_screen_source() method:")
try:
    source = champion.get_loading_screen_source()     
    assert requests.get(source).status_code == 200, f"Trying to GET URL {source} didn't return 200"
    print(f"Champion Loading Screen's source working✅\n{line}")
except Exception as e:
    print(f"Error getting to champion loading screen's source: {e}⛔\n{line}")

#test if .get_splash_art_source() method works
print(f"\nTesting get_splash_art_source() method:")
try:
    source = champion.get_splash_art_source()     
    assert requests.get(source).status_code == 200, f"Trying to GET URL {source} didn't return 200"
    print(f"Champion Splash Art's source working✅\n{line}")
except Exception as e:
    print(f"Error getting to champion splash art's source: {e}⛔\n{line}")

#test if .download_icon() method works
print(f"\nTesting download_champion_icon() method:")
try:
    champion.download_icon()
    sleep(0.5)  # Wait for the image to be saved
     
    path = f"{DEBUG_IMAGES_DIR}/images/champion_imgs/{DEBUG_CHAMPION_NAME}_imgs/icon-{DEBUG_CHAMPION_NAME}.jpg"
    assert os.path.exists(path), "Champion icon not found"
    assert (os.path.getsize(path)>0), "Champion icon is empty"
    assert os.path.isfile(path), "Champion icon is not a file"
    print(f"Champion Icon saved successfully✅\n{line}")
except Exception as e:
    print(f"Error getting champion icon: {e}⛔\n{line}")

#test if .download_loading_screen_img() method works
print(f"\nTesting download_loading_screen_img() method:")
try:
    champion.download_loading_screen_img()
    sleep(0.5)  # Wait for the image to be saved
     
    path = f"{DEBUG_IMAGES_DIR}/images/champion_imgs/{DEBUG_CHAMPION_NAME}_imgs/loading-{DEBUG_CHAMPION_NAME}.jpg"
    assert os.path.exists(path), "Champion loading screen image not found"
    assert (os.path.getsize(path)>0), "Champion loading screen image is empty"
    assert os.path.isfile(path), "Champion loading screen image is not a file"
    print(f"Champion Loading Screen image saved successfully✅\n{line}")
except Exception as e:
    print(f"Error getting champion loading screen image: {e}⛔\n{line}")

#test if .download_splash_art() method works
print(f"\nTesting download_splash_art() method:")
try:
    champion.download_splash_art()
    sleep(0.5)  # Wait for the image to be saved
     
    path = f"{DEBUG_IMAGES_DIR}/images/champion_imgs/{DEBUG_CHAMPION_NAME}_imgs/splash-{DEBUG_CHAMPION_NAME}.jpg"
    assert os.path.exists(path), "Champion splash art not found"
    assert (os.path.getsize(path)>0), "Champion splash art is empty"
    assert os.path.isfile(path), "Champion splash art is not a file"
    print(f"Champion Splash Art saved successfully✅\n{line}")
except Exception as e:
    print(f"Error getting champion splash art: {e}⛔\n{line}")

#test if .download_all_champion_images() method works
print(f"\nTesting download_all_champion_images() method:")
try:
    champion.download_all_champion_images()
    sleep(0.5)  # Wait for the images to be saved
    path = f"{DEBUG_IMAGES_DIR}/images/champion_imgs/{DEBUG_CHAMPION_NAME}_imgs/icon-{DEBUG_CHAMPION_NAME}.jpg"
    assert os.path.exists(path), "Champion icon not found"
    assert (os.path.getsize(path)>0), "Champion icon is empty"
    assert os.path.isfile(path), "Champion icon is not a file"
    path = f"{DEBUG_IMAGES_DIR}/images/champion_imgs/{DEBUG_CHAMPION_NAME}_imgs/loading-{DEBUG_CHAMPION_NAME}.jpg"
    assert os.path.exists(path), "Champion loading screen image not found"
    assert (os.path.getsize(path)>0), "Champion loading screen image is empty"
    assert os.path.isfile(path), "Champion loading screen image is not a file"
    path = f"{DEBUG_IMAGES_DIR}/images/champion_imgs/{DEBUG_CHAMPION_NAME}_imgs/splash-{DEBUG_CHAMPION_NAME}.jpg"
    assert os.path.exists(path), "Champion splash art not found"
    assert (os.path.getsize(path)>0), "Champion splash art is empty"
    assert os.path.isfile(path), "Champion splash art is not a file"
    print(f"All Champion Images saved successfully✅\n{line}")
except Exception as e:
    print(f"Error getting all champion images: {e}⛔\n{line}")

#test if .download_champion_skins() method works
print(f"\nTesting download_champion_skins() method:")
try:
    skin_names = champion.download_champion_skins()
    sleep(0.5)  # Wait for the images to be saved
    for i in range(len(skin_names)):
        skin_name = skin_names[i].replace(" ", "_").replace("/", "_").replace("'", "_").replace(":", "_").replace("!", "_").replace(".", "_").replace(",", "_")
        path = f"{DEBUG_IMAGES_DIR}/images/champion_imgs/{DEBUG_CHAMPION_NAME}_imgs/skins/{DEBUG_CHAMPION_NAME}-{skin_name}.jpg"
        assert os.path.exists(path), f"Champion {skin_name} skin splash art not found"
        assert (os.path.getsize(path)>0), f"Champion {skin_name} skin splash art is empty"
        assert os.path.isfile(path), f"Champion {skin_name} skin splash art is not a file"
    print(f"Champion Skins saved successfully✅\n{line}")
except Exception as e:
    print(f"Error getting champion skins: {e}⛔\n{line}")

