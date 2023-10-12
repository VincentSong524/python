favorite_places = {
    'name1': ['place1', 'place2', 'place3'],
    'name2': ['place1', 'place2', 'place3'],
    'name3': ['place1', 'place2', 'place3']
}

for key, value in favorite_places.items():
    print(f"{key} favorite places are:")
    for place in value:
        print(f"{place}")
    print()