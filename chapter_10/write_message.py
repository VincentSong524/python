filename = 'programming.txt'
with open(filename, 'w') as file_object:
    file_object.write("I love programming.\n")
    file_object.write('I love create new games.\n')

with open(filename, 'a') as file_object:
    file_object.write('I also love finding meaning in large datesets.\n')
    file_object.write('I love create apps that can run in browser.\n')