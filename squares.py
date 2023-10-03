squares = []#创建空列表
for value in range(1, 11):
    square = value ** 2
    squares.append(square)

print(squares)

print(f"The Min number in squares is {min(squares)}")
print(f"The Mix number in squares is {max(squares)}")
print(f"The sum number in squares is {sum(squares)}")


#以下为列表解析内容:

squares = [value**2 for value in range(1, 11)]
print(squares)
#列表解析格式: 列表名 = [临时变量的处理表达式 for 临时变量 in 元素生成表达式]