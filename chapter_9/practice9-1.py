class Restaurant:
    """餐馆类"""

    def __init__(self, restaurant_name, cuisine_type, number_serverd=0) -> None:
        """初始化餐馆名称与烹饪类型"""

        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_serverd = number_serverd
    

    def describe_restaurant(self):
        """打印两项属性信息"""
        print(f"{self.restaurant_name} {self.cuisine_type}.")

    
    def open_restaurant(self):
        """打印餐馆正在营业""" 
        print("restaurant is open!")

    
    def set_number_serverd(self, number_serverd):
        """修改就餐人数并打印"""
        self.number_serverd = number_serverd
        print(f"{self.number_serverd} people came here for a meal.")


    def increment_number_servverd(self, number_serverd):
        """递增就餐人数"""
        if number_serverd >= 0:
            self.number_serverd += number_serverd


#practice9-6
class IceCreamStand(Restaurant):
    """冰淇淋小店"""

    def __init__(self, restaurant_name, cuisine_type, number_serverd=0) -> None:
        super().__init__(restaurant_name, cuisine_type, number_serverd)
        self.flovors = ['apple', 'banana','organe', 'pear']


    def show_flovors(self):
        for flovor in self.flovors:
            print(f"{flovor}")


ice = IceCreamStand('IceCream', 'icecream')
ice.show_flovors()


kfc = Restaurant("KFC", 'Fried chicken')
kfc.describe_restaurant()

dicos = Restaurant("Dicos", "Fried chicken")
dicos.describe_restaurant()

how_many_get = Restaurant('KFC', 'Fried chicken', 100)
print(how_many_get.number_serverd)