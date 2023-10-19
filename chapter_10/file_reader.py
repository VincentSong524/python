file_name = '/home/ubuntu/python/chapter_10/pi_digits.txt'

name = 'pi_digits.txt'

with open(name) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())


pi_string = ''
for line in lines:
    pi_string += line.strip()

print(pi_string)
print(len(pi_string))