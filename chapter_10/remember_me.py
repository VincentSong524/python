import json


def greet_user():
    """问候用户，并指出其名字。"""

    filename = 'username.json'
    try:
            
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        username = input("What is your name:")
        with open(filename, 'w') as f:
            json.dump(username, f)
            print(f"We'll remember you when you come vack, {username}!")
    else:
        print(f"Welcome back, {username}")


if __name__ == "__main__":
    greet_user()
