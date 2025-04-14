import requests
import os
from time import sleep
class Champion:
    """
    A class to represent a specific League of Legends champion's data.
    """
    def __init__(self, name: str, region="en-US"):
        """
        Initializes the Champion object with the champion's name and region.
        """
        self.name = name
        self.region = region
        self.champion_obj = requests.get(f"https://cdn.merakianalytics.com/riot/lol/resources/latest/{self.region}/champions/{self.name}.json").json()

    def get_champion_key(self):
        """
        Returns the champion key.
        """
        
        champion_key = self.champion_obj["key"]
        return champion_key
    
    def get_champion_title(self):
        """
        Returns the champion title.
        """
        champion_title = self.champion_obj["title"]
        return champion_title
    def get_champion_id(self):
        """
        Returns the champion ID.
        """
        champion_id = self.champion_obj["id"]
        return champion_id
    def get_champion_lanes(self):
        """
        Returns champion's lanes
        """
        champion_lanes = list(self.champion_obj["positions"])
        return  champion_lanes
    
    
            

class ChampionImages(Champion):
    def __init__(self, name: str, region="en-US"):
        """
        Initializes the ChampionImages object with the champion's name and region.
        """
        super().__init__(name, region)
        self.champion_dir = f"images/champion_imgs/{self.name}_imgs"
        os.system(f"mkdir images && cd images && mkdir champion_imgs")
        sleep(0.5)
        os.system(f"cd images/champion_imgs && mkdir {self.name}_imgs  && cd {self.name}_imgs && mkdir skins && cd ../../..")
        sleep(0.5)
    def get_all_champion_images(self):
        """
        Retrieves all images of the champion and saves them to a directory with the champion's name inside images/champion_imgs.
        """
        self.get_icon()
        self.get_loading_screen_img()
        self.get_splash_art()

    def get_icon(self):
        champion_icon = self.champion_obj["icon"]
        champion_icon = requests.get(f"{champion_icon}")
        if champion_icon.status_code == 200:
            try:
                with open(f'{self.champion_dir}/icon-{self.name}.jpg', 'wb') as file:
                    file.write(champion_icon.content)
            except Exception as e:
                print(f"Error saving icon: {e}")
    def get_loading_screen_img(self):
        champion_loading = self.champion_obj["skins"][0]["loadScreenPath"]
        champion_loading = requests.get(f"{champion_loading}")
        if champion_loading.status_code == 200:
            with open(f'{self.champion_dir}/loading-{self.name}.jpg', 'wb') as file:
                file.write(champion_loading.content)

    def get_splash_art(self):
        champion_splash = self.champion_obj["skins"][0]["uncenteredSplashPath"]
        champion_splash = requests.get(f"{champion_splash}")
        if champion_splash.status_code == 200:
            try:
                with open(f'{self.champion_dir}/splash-{self.name}.jpg', 'wb') as file:
                    file.write(champion_splash.content)
            except Exception as e:
                print(f"Error saving splash art: {e}")
    def get_champion_skins(self):
        champion_skins = self.champion_obj["skins"]
        skins_names = list([skin["name"] for skin in champion_skins])
        skins_names = skins_names[1:]
        for skin in champion_skins:
            try:
                skin_name = skin["name"].replace(" ", "_").replace("/", "_").replace("'", "_").replace(":", "_").replace("!", "_").replace(".", "_").replace(",", "_")
                skin_splash = skin["uncenteredSplashPath"]
                skin_splash = requests.get(f"{skin_splash}")
                if skin_splash.status_code == 200 and skin != champion_skins[0]:
                    with open(f'{self.champion_dir}/skins/{self.name}-{skin_name}.jpg', 'wb') as file:
                        file.write(skin_splash.content)
            except Exception as e:
                print(f"Error saving skin splash art: {e}")
        return skins_names
  
class Champions:
    """
    A class to represent generic League of Legends champions data.
    """
    def __init__(self, region="en-US"):
        """
        Initializes the Champion object with the champion's name and region.
        """
        self.region = region
        self.champions_data = requests.get(f"https://cdn.merakianalytics.com/riot/lol/resources/latest/{self.region}/champions.json").json()
        self.champions_data = list(self.champions_data.values())

    def get_champions_names(self):
        """
        Returns a list of all champions names.
        """
        champions_names = [champion["name"] for champion in self.champions_data]
        return champions_names
    def get_champions_ids(self):
        """
        Returns a list of all champions IDs.
        """
        champions_ids = [champion["id"] for champion in self.champions_data]
        return champions_ids
    def get_champions_keys(self):
        """
        Returns a list of all champions keys.
        """
        champions_keys = [champion["key"] for champion in self.champions_data]
        return champions_keys
    def get_champions_by_lane(self, lane: str):
        """
        Returns a list of champions in given lane.

        lanes: TOP, MIDDLE, BOTTOM, JUNGLE, SUPPORT

        """
        lane = lane.upper()
        if lane not in ["TOP", "MIDDLE", "BOTTOM", "JUNGLE", "SUPPORT"]:
            raise ValueError("Invalid lane. Choose from: TOP, MIDDLE, BOTTOM, JUNGLE, SUPPORT")
        champions_by_lane = []
        for champion in self.champions_data:
            if lane in champion["positions"]:
                champions_by_lane.append({champion["name"]: champion["positions"]})
        return champions_by_lane



            