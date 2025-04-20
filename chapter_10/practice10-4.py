file_name = 'guest_book.txt'

with open(file_name, 'w') as file_object:
    while True:
        print("\nplease enter your name:(enter 'q' to quit when you finshed)")
        user_name = input()
        if user_name == 'q':
            break
        else:
            file_object.write(f"{user_name}\n")
            print(f"Welcome Mr. {user_name}.")