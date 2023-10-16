class User:
    """用户信息"""

    def __init__(self, first_name, last_name) -> None:
        """初始化名字"""
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = 0

    
    def describe_user(self):
        """打印用户信心摘要"""
        print(f"First name:{self.first_name}\tLast name:{self.last_name}")
    

    def greet_user(self):
        """个性化问候"""
        print(f"Hello, {self.first_name}.")


    def increment_login_attempts(self):
        """记录登录次数"""
        self.login_attempts += 1


    def reset_login_attempts(self):
        """重置 login_attempts 的值为0。"""
        self.login_attempts = 0


#henry
henry = User('Henry', 'Morgan')
henry.describe_user()
henry.greet_user()

#vincent
vincent = User('Vincent', "Song")
vincent.describe_user()
vincent.greet_user()

#practice9-5
song = User('wansen', 'song')
song.increment_login_attempts()
song.increment_login_attempts()
song.increment_login_attempts()
print(f"{song.login_attempts}")
song.reset_login_attempts()
print(f"{song.login_attempts}")