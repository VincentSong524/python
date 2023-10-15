class Restaurant:
    """餐馆类"""

    def __init__(self, restaurant_name, cuisine_type) -> None:
        """初始化餐馆名称与烹饪类型"""

        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    

    def describe_restaurant(self):
        """打印两项属性信息"""

        print(f"{self.restaurant_name} {self.cuisine_type}.")

    
    def open_restaurant(self):
        """打印餐馆正在营业"""
        
        print("restaurant is open!")


kfc = Restaurant("KFC", 'Fried chicken')
kfc.describe_restaurant()

dicos = Restaurant("Dicos", "Fried chicken")
dicos.describe_restaurant()