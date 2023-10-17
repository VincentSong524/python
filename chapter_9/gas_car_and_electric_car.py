class Car:
    """一次模拟汽车的简单尝试"""
    
    def __init__(self, make, model, year) -> None:
        """"初始化描述汽车的属性。"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    
    def get_descriptive_name(self):
        """返回整洁的描述性信息"""

        long_name = f"{self.year} {self.make} {self.model}"
        return long_name
    

    def read_odometer(self):
        """打印一条指出汽车里程的消息。"""
        print(f"This car has {self.odometer_reading} miles on it.")

    
    def update_odometer(self, mileage):
        """
        将里程表读数设置为指定的值。
        禁止将里程表读数往回调。
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")


    def increment_ofometer(self, miles):
        """将里程表读数增加指定的量"""
        if miles >= 0:
            self.odometer_reading += miles
        else:
            print("You can't roll back an odometer!")

    
    def fill_gas_tank(self):
        """汽车有油箱。"""
        print("This car need a gas tank!")


class Battery:
    """模拟电动汽车电瓶。"""

    def __init__(self, battery_size=75) -> None:
        """初始化电瓶的属性。"""
        self.battery_size = battery_size


    def describe_battery(self):
        """打印一条描述电瓶容量的消息。"""
        print(f"This car has a {self.battery_size}-kWh battery.")


    def get_range(self):
        """打印电瓶的续航里程“"""
        range = self.battery_size * 3
        print(f"This car can go about {range} miles on a full charge.")

    
    def upgrade_battery(self):
        """检测电池电量是否是一百如果不是一百就设置为一百"""
        if self.battery_size != 100:
            self.battery_size = 100


class ElectricCar(Car):
    """电动汽车的独特之处。"""

    def __init__(self, make, model, year) -> None:
        """
        初始化父类的属性。
        在初始化电动汽车特有的属性。
        """
        super().__init__(make, model, year)
        self.battery = Battery()


    def describe_battery(self):
        """打印一条描述电瓶容量的消息。"""
        print(f"This car has a {self.battery}-kWh battery.")

    
    def fill_gas_tank(self):
        """电动汽车没有油箱。"""
        print("This car doesn't need a gas tank!")




my_tesla = ElectricCar('tesla', 'model s', 2019)
my_tesla.update_odometer(100)
my_tesla.read_odometer()
my_tesla.fill_gas_tank()

print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()

"""
my_new_car = Car('audi', 'a4', 2019)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()

my_new_car.update_odometer(23)
my_new_car.read_odometer()

my_new_car.increment_ofometer(23_500)
my_new_car.read_odometer()
"""

byd = ElectricCar('BYD', '秦', '2023')
print(byd.get_descriptive_name())
byd.battery.get_range()
byd.battery.upgrade_battery()
byd.battery.get_range()
