favroite_numbers = {
    'henry': [1, 4, 7],
    'vincent': [2, 4, 6, 8, 10],
    'jhon': [1, 3, 5, 7, 9],
    'harry': [1, 2, 3, 4, 5, 6, 7],
    'hunter': [1, 2, 3, 6, 8]
}

for name, numbers in favroite_numbers.items():
    print(f"{name}'s favorite are:")
    for number in numbers:
        print(number,end=' ')
    print()