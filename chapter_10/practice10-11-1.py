import json

num_file = 'favorite_number.json'

with open(num_file) as f:
    number = json.load(f)
    print(number)