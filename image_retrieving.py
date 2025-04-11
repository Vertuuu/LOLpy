from Champion import Champion, Champions, ChampionImages
if __name__ == "__main__":
    # Create a Champion object
    all_champions = Champions("en_US").get_champion_list()
    for i, champion in enumerate(all_champions):
        champion_name = champion["name"]
        print(f"{i} - Champion Name: {champion_name}")
        champion = ChampionImages(champion_name)
        champion.get_all_champion_images()
        champion.get_champion_skins()
        