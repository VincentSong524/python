prompt = "Please enter you age(Enter quit when you are finished):"

while True:
    age = input(prompt)
    if age == 'quit':
        break
    else:
        age = int(age)
        if age < 3:
            print("Receivable 0 Yuan.")
        elif age <= 12:
            print("Receivable 10 Yuan.")
        else:
            print("Receivable 15 Yuan.")