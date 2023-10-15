sandwich_orders = ['sandwich_0', 'pastrami', 'sandwich_1', 'pastrami', 'sandwich_2', 'pastrami']
finished_sandwiches = []

for sandwich in sandwich_orders:
    print(f"I made your {sandwich}.")
    finished_sandwiches.append(sandwich)
    #sandwich_orders.remove(sandwich)#我认为这里的删除导致了的原列表顺序的改变，导致了程序的错误

print(finished_sandwiches)

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
print(sandwich_orders)