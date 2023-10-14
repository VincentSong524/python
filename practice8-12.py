def sandwich_toppings(*toppings):
    """接受顾客要在三明治中添加的一系列食材，并概述"""
    print("You order sandwich toppings are:")
    for topping in toppings:
        print(topping)

sandwich_toppings('apple', 'bananas')