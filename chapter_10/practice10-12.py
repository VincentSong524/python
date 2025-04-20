import json

def show(file):
    """如果数字存在就显示，否则就提示用户输入数字。"""
    file_name = file
    try:
        with open(file_name) as f:
            number = json.load(f)
            print(f"I know your favorite number! It's {number}.")
    except json.decoder.JSONDecodeError:
        with open(file_name, 'w') as f:
            number = input("Please enter your favorite number: ")
            json.dump(number, f)

if __name__ == '__main__':
    file_name = 'favorite_number.json'
    show(file_name)