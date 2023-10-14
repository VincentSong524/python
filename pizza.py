#存储所点披萨信息
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
}

#概述所点的披萨
print(f"You ordered a {pizza['crust']}-crust pizza "
      "with the following toppings:")

for topping in pizza['toppings']:
    print("\t" + topping)

def make_pizza(*toppings):
    """打印顾客点的所有配料"""
    for topping in toppings:
        print(topping)

make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')