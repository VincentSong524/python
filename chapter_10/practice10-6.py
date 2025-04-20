

while True:
    first_number = input('Please enter first number(Enter "q" to quit):')
    if first_number == 'q':
        break
    second_number = input('Please enter second number(Enter "q" to quit):')
    if second_number == 'q':
        break
    try:
        first_number = int(first_number)
        
        second_number = int(second_number)
    except ValueError:
        print("Pelase a number not a string.")
    else:
        sum = first_number + second_number
        print(f"{first_number} + {second_number} = {sum}")