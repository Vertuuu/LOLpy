import requests
import os
from time import sleep
class Champion:
    """
    A class to represent a specific League of Legends champion's data.
    """
    def __init__(self, key: str, region="en-US"):
        """
        Initializes the Champion object with the champion's name and region.
        """
        self.key = key
        self.region = region
        self.champion_obj = requests.get(f"https://cdn.merakianalytics.com/riot/lol/resources/latest/{self.region}/champions/{self.key}.json").json()
    def get_champion_key(self):
        """
        Returns the champion key.
        """
        champion_key = self.champion_obj["key"]
        return champion_key
    def get_champion_name(self):
        """
        Returns the champion name
        """
        champion_name = self.champion_obj["name"]
        return champion_name
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
    def get_champion_lore(self):
        """
        Returns champion's lore, which is, actually, a summarized version of it's lore
        """
        champion_bio = self.champion_obj["lore"]
        return champion_bio
    def get_champion_lanes(self):
        """
        Returns champion's lanes
        """
        champion_lanes = list(self.champion_obj["positions"])
        return  champion_lanes
    def get_champion_resource(self):
        """
        Return champion's resource to cast abilities
        """
        champion_resource = self.champion_obj["resource"]
        return champion_resource
    
    def get_champion_range(self):
        """
        Return champion's attack range type
        """
        champion_range = self.champion_obj["attackType"]
        return champion_range
    
    def get_abilities_names(self):
        """
        Returns a dict with champion's passive and abilities names
        """
        champion_abilities = self.champion_obj["abilities"]
        p = champion_abilities["P"][0]["name"]
        q = champion_abilities["Q"][0]["name"]
        w = champion_abilities["W"][0]["name"]
        e = champion_abilities["E"][0]["name"]
        r = champion_abilities["R"][0]["name"]
        champion_abilities = {
            "P": p,
            "Q": q,
            "W": w,
            "E": e,
            "R": r
        }
        return champion_abilities
    def get_abilities_sources(self):
        """
        Returns a dict with champion's passive and abilities image sources
        """
        champion_abilities = self.champion_obj["abilities"]
        p = champion_abilities["P"][0]["icon"]
        q = champion_abilities["Q"][0]["icon"]
        w = champion_abilities["W"][0]["icon"]
        e = champion_abilities["E"][0]["icon"]
        r = champion_abilities["R"][0]["icon"]
        champion_abilities = {
            "P": p,
            "Q": q,
            "W": w,
            "E": e,
            "R": r
        }
        return champion_abilities
    def get_abilities_description(self):
        """
        Returns a dict with champion's passive and abilities descriptions
        """
        champion_abilities = self.champion_obj["abilities"]
        p = champion_abilities["P"][0]["effects"][0]["description"]
        q = champion_abilities["Q"][0]["effects"][0]["description"]
        w = champion_abilities["W"][0]["effects"][0]["description"]
        e = champion_abilities["E"][0]["effects"][0]["description"]
        r = champion_abilities["R"][0]["effects"][0]["description"]
        champion_abilities = {
            "P": p,
            "Q": q,
            "W": w,
            "E": e,
            "R": r
        }
        return champion_abilities

    def get_release_date(self):
        """
        Returns the date that the champion was released
        """
        champion_release = self.champion_obj["releaseDate"]
        return champion_release
    def get_price(self):
        """
        Returns a dict with champion's price in blue essences and RP
        """
        champion_price = self.champion_obj["price"]
        blue = champion_price["blueEssence"]
        rp = champion_price["rp"]

        champion_price = {
            "blueEssence": blue,
            "rp": rp
        }
        return champion_price

class ChampionImages(Champion):
    def __init__(self, key: str, imgs_dir="", region="en-US"):
        """
        Initializes the ChampionImages object with the champion's key and region.
        """
        super().__init__(key, region)
        self.imgs_dir = os.getcwd() if imgs_dir == "" else str(imgs_dir)
        if not os.path.isdir(self.imgs_dir):
            raise ValueError(f"Directory '{self.imgs_dir}' does not exist.")
        self.champion_dir = f"{self.imgs_dir}\\images\\champion_imgs\\{self.key}_imgs"

    def create_imgs_dir(self):
        os.system(f"cd {self.imgs_dir} && mkdir images")
        os.system(f"cd {self.imgs_dir}\\images && mkdir champion_imgs")
        os.system(f"cd {self.imgs_dir}\\images\\champion_imgs && mkdir {self.key}_imgs")
        os.system(f"cd {self.champion_dir} && mkdir skins")
    def get_all_champion_images_sources(self):
        """
        Returns the source URLs for all champion's default images
        (icon, loading screen image and splash art, in order)
        """
        icon, loading, splash = self.get_icon_source(), self.get_loading_screen_source(), self.get_splash_art_source()
        return [icon, loading, splash]
    def get_icon_source(self):
        """
        Returns the source URL for a champion's icon
        """
        champion_icon = self.champion_obj["icon"]
        return champion_icon
    
    def get_splash_art_source(self):
        """
        Returns the source URL for a champion's splash art
        """
        champion_splash = self.champion_obj["skins"][0]["uncenteredSplashPath"]
        return champion_splash
    
    def get_loading_screen_source(self):
        """
        Returns the source URL for a champion's loading screen image
        """
        champion_loading = self.champion_obj["skins"][0]["loadScreenPath"]
        return champion_loading
    
    def get_champion_skins_sources(self):
        champion_skins = self.champion_obj["skins"]
        champion_skins = champion_skins[1:]
        return champion_skins
    
    def download_all_champion_images(self):
        """
        Retrieves all images of the champion and saves them to a directory with the champion's key inside images/champion_imgs.
        """
        self.create_imgs_dir()
        self.download_icon()
        self.download_loading_screen_img()
        self.download_splash_art()

    def download_icon(self):
        if not os.path.isdir(self.champion_dir):
            self.create_imgs_dir()
        champion_icon = self.get_icon_source()
        champion_icon = requests.get(f"{champion_icon}")
        if champion_icon.status_code == 200:
            try:
                with open(f'{self.champion_dir}\\icon-{self.key}.jpg', 'wb') as file:
                    file.write(champion_icon.content)
            except Exception as e:
                print(f"Error saving icon: {e}")

    def download_loading_screen_img(self):
        if not os.path.isdir(self.champion_dir):
            self.create_imgs_dir()
        champion_loading = self.get_loading_screen_source()
        champion_loading = requests.get(f"{champion_loading}")
        if champion_loading.status_code == 200:
            with open(f'{self.champion_dir}\\loading-{self.key}.jpg', 'wb') as file:
                file.write(champion_loading.content)

    def download_splash_art(self):
        if not os.path.isdir(self.champion_dir):
            self.create_imgs_dir()
        champion_splash = self.get_splash_art_source()
        champion_splash = requests.get(f"{champion_splash}")
        if champion_splash.status_code == 200:
            try:
                with open(f'{self.champion_dir}\\splash-{self.key}.jpg', 'wb') as file:
                    file.write(champion_splash.content)
            except Exception as e:
                print(f"Error saving splash art: {e}")

    def download_champion_skins(self):
        if not os.path.isdir(self.champion_dir):
            self.create_imgs_dir()
        champion_skins = self.get_champion_skins_sources()
        skins_names = list([skin["name"] for skin in champion_skins])
        for skin in champion_skins:
            try:
                skin_name = skin["name"].replace(" ", "_").replace("/", "_").replace("'", "_").replace(":", "_").replace("!", "_").replace(".", "_").replace(",", "_")
                skin_splash = skin["uncenteredSplashPath"]
                skin_splash = requests.get(f"{skin_splash}")
                if skin_splash.status_code == 200:
                    with open(f'{self.champion_dir}\\skins\\{self.key}-{skin_name}.jpg', 'wb') as file:
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



            