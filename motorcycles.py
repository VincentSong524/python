motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles[0] = "ducati"
print(motorcycles)

motorcycles.append("ducati")
print(motorcycles)

motorcycles.insert(0,'honda')
print(motorcycles)

del motorcycles[-1]
print(motorcycles)

print(motorcycles.pop())
print(motorcycles)

print(f"My first motorcycles is {motorcycles.pop(0)}.")
print(motorcycles)
motorcycles.remove("yamaha")
print(motorcycles)

a = motorcycles.remove('ducati')
print(a)#无法成功，返回None。