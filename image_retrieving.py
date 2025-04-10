from Champion import Champion
if __name__ == "__main__":
    # Create a Champion object
    champion_name = "Aatrox"
    champion = Champion(champion_name)

    champion.ChampionImages(champion_name).get_icon()
    champion.ChampionImages(champion_name).get_splash_art()
    champion.ChampionImages(champion_name).get_loading_screen_img()
    # Get images of the champion and save them to a directory with the champion's name inside images/champion_imgs
    champion.ChampionImages(champion_name).get_all_champion_images()
    