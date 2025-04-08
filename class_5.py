import turtle

# Set up the screen
screen = turtle.Screen()
screen.title("Turtle Drawing")

# Create a turtle object
t = turtle.Turtle()
t.speed(5)

# Draw an equilateral triangle with side length 200
side_length = 200
for _ in range(3):
    t.forward(side_length)
    t.left(120)

# Move to the center for drawing concentric circles
t.penup()
t.goto(0, -20)
t.pendown()

# Draw concentric circles with radius increasing by 20
# 绘制同心圆
for radius in range(20, 121, 20):
    t.penup()
    t.goto(0, -radius)
    t.pendown()
    t.circle(radius)

# Draw polygons with sides from 3 to 7
for sides in range(3, 8):
    t.penup()
    t.goto(0, 0)
    t.pendown()
    angle = 360 / sides
    for _ in range(sides):
        t.forward(100)
        t.left(angle)

# Finish
turtle.done()