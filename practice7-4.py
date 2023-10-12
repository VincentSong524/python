prompt = "Please enter pizza toppings(Enter quit when you are finshed.):"

while True:
    toppings = input(prompt)
    if toppings == 'quit':
        break
    else:
        print(f"\nWe will add {toppings} in pizza.")

active = True
while active:
    toppings = input(prompt)
    if toppings == 'quit':
        active = False
    else:
        print(f"\nWe will add {toppings} in pizza.")

toppings = ''
while toppings != 'quit':
    toppings = input(prompt)
    if toppings != 'quit':
        print(f"\nWe will add {toppings} in pizza.")