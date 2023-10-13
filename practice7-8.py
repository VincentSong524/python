sandwich_orders = ['sandwich_0', 'sandwich_1', 'sandwich_2']
finished_sandwiches = []

for sandwich in sandwich_orders:
    print(f"I made your {sandwich}.")
    finished_sandwiches.append(sandwich)
    #sandwich_orders.remove(sandwich)#我认为这里的删除导致了的原列表顺序的改变，导致了程序的错误

print(finished_sandwiches)