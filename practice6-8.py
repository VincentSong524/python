dog = {
    'name': 'kiki',
    'favorite_food': 'bone',
    'color': 'black'
}

cat = {
    'name': 'coffe',
    'favorite_food': 'finsh',
    'color': 'yellow'
}

pets = [dog, cat]

for info in pets:
    for key, value in info.items():
        print(f"{key}: {value}")
    print()