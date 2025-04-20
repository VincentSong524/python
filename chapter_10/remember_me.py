import json

def get_stored_username():
    """如果存储了用户名，就获取它。"""
    filename = 'username.json'
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username
    
def get_new_username():
    """"获取新用户名"""
    filename = 'username.json'
    with open(filename, 'w') as f:
        username = input("Please enter your name: ")
        json.dump(username, f)
    
def greet_user():
        """问候用户，并指出其名字。"""
        username = get_stored_username()
        
        if username:
            print(f"Is your name {username}(yes/no)?")
            judgment = input()
            if judgment == 'yes':
                print(f"Welcome back, {username}")
            else:
                get_new_username()
        else:
            #
            username = input("What is your name:")
            filename = 'username.json'
            with open(filename, 'w') as f:
                json.dump(username, f)
                print(f"We'll remember you when you come vack, {username}!")


if __name__ == "__main__":
    greet_user()
