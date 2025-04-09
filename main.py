import pprint
import os
import requests
import cassiopeia as cass
from cassiopeia import Champion, Champions
# Use any translator you like, in this example GoogleTranslator


def get_champion(champion: str):
    champion = champion.lower().strip().capitalize()
    champions_obj = requests.get(f"https://ddragon.leagueoflegends.com/cdn/15.7.1/data/pt_BR/champion/{champion}.json").json()
    champions_obj = champions_obj["data"][champion]
    print(champions_obj["recommended"])
    
if __name__ == "__main__":
    champions = Champions(region="NA")
    for champion in champions:
        try:
            print(f"\n{champion.name}\n")
            get_champion(champion.name)
        except Exception as e:
            print(f"Error: {e}")
            continue