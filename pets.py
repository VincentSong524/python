pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)

while 'cat' in pets:
    pets.remove('cat')

print(pets)

def describe_pet(pet_name, animal_type='dog'):#这里有一个问题：有默认值的参数必须放到没有默认值的参数的后面。难以置信，五年前的东西我居然还记着。
    """显示成宠物的信息"""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

#使用位置实参
describe_pet('harry', 'hamster')
#使用关键字实参
describe_pet(animal_type='hamster', pet_name='harry')
#只为pet_name提供实参，因为animal_type有默认值
describe_pet('willie')