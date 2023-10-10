favorite_pizza = ['a', 'b', 'c']
for pizza in favorite_pizza:
    print(f"{pizza.title()} is my favorite pizza.")
print('I really love pizza!')

friend_pizza = favorite_pizza[:]
favorite_pizza.append('lemon')
friend_pizza.append('apple')
print("My favorite pizzas are:")
for i in favorite_pizza:
    print(i)

print("My friend's favorite pizzas are:")
for i in friend_pizza:
    print(i)

