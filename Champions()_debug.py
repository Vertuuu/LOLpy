#NOTE: Unit testing like this surely isn't the best way to test a class, but it works for now. As the project grows, we will need to implement a more robust testing framework.

from LOLpy import Champions

line_header = "=" * 50
line = "-" * 50

print(f"\n{line_header}\nChampions() class debug\n{line_header}\n")
#test if the Champions() object can be created
try:
    champions = Champions("en-US")
except Exception as e:
    print(f"Error creating Champions() object: {e}⛔\n{line}")

#test if the .get_champions_names() method works
try:
    champions_names = champions.get_champions_names()
    assert type(champions_names) == list, "Champions names is not a list"
    assert len(champions_names) > 0, "Champions names list is empty"
    assert len(champions_names) >= 170, "Champions names list does not contain all champions"
    for champion in champions_names:
        print(f"Champion Name: {champion}✅")
        assert type(champion) == str, "Champion name is not a string"
        assert len(champion) > 0, "Champion name is empty"
    print(f"{line}")
except Exception as e:
    print(f"Error getting champions names: {e}⛔\n{line}")

#test if the .get_champions_ids() method works
try:
    champions_ids = champions.get_champions_ids()
    assert type(champions_ids) == list, "Champions ids is not a list"
    assert len(champions_ids) > 0, "Champions ids list is empty"
    assert len(champions_ids) >= 170, "Champions ids list does not contain all champions"
    for champion in champions_ids:
        print(f"Champion Name: {champion}✅")
        assert type(champion) == int, "Champion id is not a integer"
        assert champion > -1, "Champion id is a negative number"
    print(f"{line}")
except Exception as e:
    print(f"Error getting champions IDs: {e}⛔\n{line}")

#test if the .get_champions_keys() method works
try:
    champions_keys = champions.get_champions_keys()
    assert type(champions_keys) == list, "Champions keys is not a list"
    assert len(champions_keys) > 0, "Champions keys list is empty"
    assert len(champions_keys) >= 170, "Champions keys list does not contain all champions"
    for champion in champions_keys:
        print(f"Champion Name: {champion}✅")
        assert type(champion) == str, "Champion key is not a string"
        assert len(champion) > 0, "Champion key is empty"
    print(f"{line}")
except Exception as e:
    print(f"Error getting champions keys: {e}⛔\n{line}")

#



