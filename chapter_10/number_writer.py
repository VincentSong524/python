import json

numbers = [x for x in range(1, 11)]

filename = 'numbers.json'
with open(filename, 'w') as f:
    json.dump(numbers, f)