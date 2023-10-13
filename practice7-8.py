sandwich_orders = ['sandwich_0', 'sandwich_1', 'sandwich_2']
finished_sandwiches = []

print(sandwich_orders)

for sandwich in sandwich_orders:
    print(f"I made your {sandwich}.")
    finished_sandwiches.append(sandwich)
    print(f"sandwich_orders:{sandwich_orders}")
    #sandwich_orders.remove(sandwich)#我认为这里的删除导致了的原列表顺序的改变，导致了程序的错误

print(sandwich_orders)

print(finished_sandwiches)