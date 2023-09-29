cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()#正向排序
print(cars)

cars.sort(reverse=True)#反向排序
print(cars)


cars = ['bmw', 'audi', 'toyota', 'subaru']
print("Here is the original list:")
print(cars)

print('\nHere is the sorted list:')
print(sorted(cars))#临时排序

print('\nHere is the original list again:')
print(cars)

cars.reverse()
print(cars)
cars.reverse()
print(cars)