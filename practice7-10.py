#创建列表
favorite_places = []
#循环提示用户输入
while True:
    place = input("If your could visit one place in the world, where would you go? ")
    favorite_places.append(place)
    active = input("continue?(yes/no) ")
    if active == 'no':
        break
#询问是否继续

print(favorite_places)