import json

file_name = 'favorite_number.json'

favortie_num = input("please enter your favorite number: ")

with open(file_name, 'w') as f:
    json.dump(favortie_num, f)