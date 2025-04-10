import requests
import os
class Champion:
    """
    A class to represent a specific League of Legends champion's data.
    """
    def __init__(self, name: str, region="NA"):
        self.name = name.title().replace(" ", "")
        self.region = region
        
        pass
    def get_champion_basic_info(self):
        
        champion_obj = requests.get(f"https://ddragon.leagueoflegends.com/cdn/15.7.1/data/{self.region}/champion/{self.name}.json").json()
        champion_obj = champion_obj["data"][self.name]
        return champion_obj
    def get_champion_images(self):
        champion_dir = f"images/champion_imgs/{self.name}_imgs"
        os.system(f"cd images/champion_imgs && mkdir {self.name}_imgs && cd ../..")
        champion_icon = requests.get(f"https://ddragon.leagueoflegends.com/cdn/15.7.1/img/champion/{self.name}.png")
        if champion_icon.status_code == 200:
            print("Icon found")
            try:
                with open(f'{champion_dir}/icon-{self.name}.jpg', 'wb') as file:
                    file.write(champion_icon.content)
            except Exception as e:
                print(f"Error saving icon: {e}")

        champion_loading = requests.get(f"https://ddragon.leagueoflegends.com/cdn/img/champion/loading/{self.name}_0.jpg")
        if champion_loading.status_code == 200:
            print("Loading found")
            try:
                with open(f'{champion_dir}/loading-{self.name}.jpg', 'wb') as file:
                    file.write(champion_loading.content)
            except Exception as e:      
                print(f"Error saving loading screen: {e}")    
        champion_splash = requests.get(f"https://ddragon.leagueoflegends.com/cdn/img/champion/splash/{self.name}_0.jpg")
        if champion_splash.status_code == 200:
            print("Splash found")
            try:
                with open(f'{champion_dir}/splash-{self.name}.jpg', 'wb') as file:
                    file.write(champion_splash.content)
            except Exception as e:
                print(f"Error saving splash art: {e}")