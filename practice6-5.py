rivers = {
    'nile': 'egypt',
    'Yangtze': 'China',
    'Shenandoah': 'United States of America',
}

for river, county in rivers.items():
    print(f'The {river.title()} runs through {county.title()}.')