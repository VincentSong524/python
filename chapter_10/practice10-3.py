file_name = 'guest.txt'

with open(file_name, 'a') as file_object:
    print("please enter your information: ")
    user_info = str(input())
    file_object.write(f"{user_info}\n")