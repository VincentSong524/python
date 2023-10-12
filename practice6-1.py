friend_0 = {
    'first_name': 'henry',
    'last_name': 'morgan',
    'age': '23',
    'place_city': 'New York',
}

friend_1 = {
    'first_name': 'henry',
    'last_name': 'morgan',
    'age': '23',
    'place_city': 'New York',
}

friend_2 = {
    'first_name': 'henry',
    'last_name': 'morgan',
    'age': '23',
    'place_city': 'New York',
}

people = [
    friend_0,
    friend_1,
    friend_2
]

for info in people:
    for key, value in info.items():
        print(f"{key}: {value}")
    print()