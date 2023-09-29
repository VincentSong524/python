name_list = ['传鑫', '建军', '天昊', '万昊']

for i in range(int(len(name_list))):
    print(f'{name_list[i]}')

print(f"{name_list[3]} can't came here, but 鸡脖 came.")
name_list.remove('天昊')
name_list.append('鸡脖')

for i in range(int(len(name_list))):
    print(f'{name_list[i]}')

name_list.insert(0, '昌龙')
print(name_list)

name_list.insert(3, '天昊')
print(name_list)

name_list.append('王迪')
print(name_list)

print("Because the table can't use , we only invite two man.")

while (int(len(name_list)) > 2):
    print(f'Sorry, we need delete {name_list.pop()}.')

print(f'{name_list[0]} and {name_list[1]} still in invite list.')

del name_list[0]

del name_list[0]

print(name_list)