import os

#获取脚本文件的绝对路径
script_dir = os.path.dirname(__file__)

#要处理的文件名称
file_name = 'pi_million_digits.txt'

# 构建要处理的文件的相对路径
file_to_process = os.path.join(script_dir, file_name)

with open(file_name) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

#print(f"{pi_string[:52]}...")
#print(len(pi_string))

birthday = input("Enter your birthday, in the form yyyymmdd: ")
if birthday in pi_string:
    print("Your birthday appears in the first million digits of pi!")
else:
    print("Your birthday does not appear in the first million digits of pi.")