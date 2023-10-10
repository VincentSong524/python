users = ['admin', 'john', 'vincent', 'dick']

if users:
    for user in users:
        if user == 'admin':
            print("Hello admin, would you like to see a status report?")
        else:
            print(f"Hello {user}, thank you for logining in again.")
else:
    print("We need to find some users!")
