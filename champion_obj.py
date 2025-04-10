import requests
class Champion:
    def __init__(self, name: str, region: str):
        self.name = name
        self.region = region
        
        pass
    def get_champion_basic_info(self):
        
        champion_obj = requests.get(f"https://ddragon.leagueoflegends.com/cdn/15.7.1/data/pt_BR/champion/{self.name}.json").json()
        champion_obj = champion_obj["data"][self.name]
        return champion_obj
    def get_champion_images(self):
        champion_icon = requests.get(f"https://ddragon.leagueoflegends.com/cdn/15.7.1/img/champion/{self.name}.png")
        if champion_icon.status_code == 200:
            print("Icon found")
            with open(f'img/icon-{self.name}.jpg', 'wb') as file:
                file.write(champion_icon.content)
        
        champion_splash = requests.get(f"https://ddragon.leagueoflegends.com/cdn/img/champion/splash/{self.name}_0.jpg")
        if champion_splash.status_code == 200:
            print("Splash found")
            with open(f'img/splash-{self.name}.jpg', 'wb') as file:
                file.write(champion_splash.content)
        
        champion_loading = requests.get(f"https://ddragon.leagueoflegends.com/cdn/img/champion/loading/{self.name}_0.jpg")
        if champion_loading.status_code == 200:
            print("Loading found")
            with open(f'img/loading-{self.name}.jpg', 'wb') as file:
                file.write(champion_loading.content)