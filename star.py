import turtle

# 设置屏幕
screen = turtle.Screen()
screen.title("绘制红色五角星")

# 创建海龟对象
t = turtle.Turtle()
t.speed(3)

# 设置颜色
t.color("red")
t.fillcolor("red")
# 开始填充
t.begin_fill()
t.goto(-150, 0)  # 回到原点
# 绘制五角星
for _ in range(5):
    t.forward(150)  
    t.left((180-36)/2)    # 五角星的角度
    t.forward(150)
    t.right(144)  

# 结束填充
t.end_fill()

# 完成
turtle.done()