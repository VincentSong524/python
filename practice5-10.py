current_users = ['admin', 'john', 'vincent', 'dick', 'Bob']
new_users = ['john', 'dick', 'harry', 'hunter', 'kate']

for user in new_users:
    if user in current_users:
        print("You need other username.")
    else:
        print("This username are not use.")
