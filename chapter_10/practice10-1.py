file_name = 'learning_python.txt'

#读取整个文件
with open(file_name) as file_object:
    #直接打印
    contents = file_object.read()
    print(contents)

with open(file_name) as file_object:
    #遍历文件对象打印
    for line in file_object:
        print(line.strip())

with open(file_name) as file_object:
    #将各行存储在一个列表中，再在with代码块外打印
    lines = [line for line in file_object]
    
for line in lines:
    print(line.strip())