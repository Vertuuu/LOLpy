from Champion import Champion
if __name__ == "__main__":
    # Create a Champion object
    champion_name = "Miss Fortune"
    champion = Champion(champion_name)
    champion.ChampionImages(champion_name).get_all_champion_images()
    champion.ChampionImages(champion_name).get_champion_skins()
    