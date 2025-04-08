import turtle

screen = turtle.Screen()
screen.title("turtle 绘制多边形和圆")
t = turtle.Turtle()

# 多边形 steps=边数
t.circle(-100, steps=3)  # Draw a circle with radius 100



t.clear()  # Clear the screen



t.color("pink")  # Set the color to blue
# 红色爱心
t.fillcolor("pink")
t.begin_fill()
t.setheading(45)
t.forward(100)
t.circle(50, extent=180)
t.right(90)
t.circle(50, extent=180)
t.forward(100)
t.end_fill()
t.penup()


t.clear()  # Clear the screen

# 绘制五角星
t.color("red")
t.fillcolor("red")
t.begin_fill()
t.home()
t.pendown()
for _ in range(5):
    t.forward(100)
    t.right(144)
t.end_fill()
t.penup()



turtle.done()
