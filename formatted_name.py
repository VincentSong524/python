import get_formatted_name
from get_formatted_name import get_formatted_name
from get_formatted_name import get_formatted_name as fn
import get_formatted_name as mn #将模块名字重命名的导入方式，而不是将函数重命名
from get_formatted_name import *

#循环输入
while True:
    print("\nPlease tell me your name:")
    print("(enter 'q' at any time to quit)")
    
    f_name = input("First name: ")
    if f_name == 'q':
        break
    
    l_name = input("Last name: ")
    if l_name == 'q':
        break

    formatted_name = get_formatted_name(f_name, l_name)
    print(f"\nHello, {formatted_name}")

f_name = 'vincent'
l_name = 'Song'
internet_name = mn.get_formatted_name(f_name, l_name)
print(internet_name)