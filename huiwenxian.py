import turtle

step = 2
for _ in range(100):
    turtle.forward(step)
    turtle.right(90)
    step += 2

turtle.done()