class User:
    """用户信息"""

    def __init__(self, first_name, last_name) -> None:
        """初始化名字"""

        self.first_name = first_name
        self.last_name = last_name

    
    def describe_user(self):
        """打印用户信心摘要"""

        print(f"First name:{self.first_name}\tLast name:{self.last_name}")
    

    def greet_user(self):
        """个性化问候"""

        print(f"Hello, {self.first_name}.")


henry = User('Henry', 'Morgan')
henry.describe_user()
henry.greet_user()

vincent = User('Vincent', "Song")
vincent.describe_user()
vincent.greet_user()