import turtle as t


t.color("yellow")
t.fillcolor("yellow")
t.begin_fill()
for _ in range(8):
    t.forward(100)
    t.left(90)
    t.forward(100)
    t.right(180-45)
t.end_fill()
t.done()