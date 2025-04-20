from car import Car, ElectricCar
#可以导入整个类 然后使用句点表示法访问需要的类 import car

my_bettle = Car('volkswagen', 'beetle', 2019)
print(my_bettle.get_descriptive_name())

my_tesla = ElectricCar('tesla', 'roadster', 2019)
print(my_tesla.get_descriptive_name())