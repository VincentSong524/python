"""一组可用于表示电动汽车的类"""

from car import Car

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
