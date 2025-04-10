import requests
import os
from time import sleep
class Champion:
    """
    A class to represent a specific League of Legends champion's data.
    """
    def __init__(self, name: str, region="en_US"):
        """
        Initializes the Champion object with the champion's name and region.
        """
        self.name = name.title().replace(" ", "")
        self.region = region
        self.champion_obj = requests.get(f"https://ddragon.leagueoflegends.com/cdn/15.7.1/data/{self.region}/champion/{self.name}.json").json()

    def get_champion_key(self):
        """
        Returns the champion key.
        """
        
        champion_key = self.champion_obj["data"][self.name]["key"]
        return champion_key
    
    def get_champion_title(self):
        """
        Returns the champion title.
        """
        champion_title = self.champion_obj["data"][self.name]["title"]
        return champion_title
    
    # def get_champion_basic_info(self):
        
    #     champion_obj = requests.get(f"https://ddragon.leagueoflegends.com/cdn/15.7.1/data/{self.region}/champion/{self.name}.json").json()
    #     champion_obj = champion_obj["data"][self.name]
    #     return champion_obj
    class ChampionImages:
        def __init__(self, name: str, region="en_US"):
            """
            Initializes the ChampionImages object with the champion's name and region.
            """
            self.name = name.title().replace(" ", "")
            self.region = region
            self.champion_dir = f"images/champion_imgs/{self.name}_imgs"
            os.system(f"mkdir images && cd images && mkdir champion_imgs")
            os.system(f"cd images/champion_imgs && mkdir {self.name}_imgs && cd ../..")
        def get_all_champion_images(self):
            """
            Retrieves all images of the champion and saves them to a directory with the champion's name inside images/champion_imgs.
            """
            self.get_icon()
            self.get_loading_screen_img()
            self.get_splash_art()

        def get_icon(self):
            champion_icon = requests.get(f"https://ddragon.leagueoflegends.com/cdn/15.7.1/img/champion/{self.name}.png")
            if champion_icon.status_code == 200:
                print("Icon found")
                try:
                    with open(f'{self.champion_dir}/icon-{self.name}.jpg', 'wb') as file:
                        file.write(champion_icon.content)
                except Exception as e:
                    print(f"Error saving icon: {e}")
        def get_loading_screen_img(self):
            champion_loading = requests.get(f"https://ddragon.leagueoflegends.com/cdn/img/champion/loading/{self.name}_0.jpg")
            if champion_loading.status_code == 200:
                print("Loading found")
                try:
                    with open(f'{self.champion_dir}/loading-{self.name}.jpg', 'wb') as file:
                        file.write(champion_loading.content)
                except Exception as e:      
                    print(f"Error saving loading screen: {e}")

        def get_splash_art(self):
            champion_splash = requests.get(f"https://ddragon.leagueoflegends.com/cdn/img/champion/splash/{self.name}_0.jpg")
            if champion_splash.status_code == 200:
                print("Splash found")
                try:
                    with open(f'{self.champion_dir}/splash-{self.name}.jpg', 'wb') as file:
                        file.write(champion_splash.content)
                except Exception as e:
                    print(f"Error saving splash art: {e}")