from Champion import Champion
if __name__ == "__main__":
    # Create a Champion object
    champion = Champion("Akali", "NA")

    # Get images of the champion and save them to a directory with the champion's name inside images/champion_imgs
    champion.get_champion_images()