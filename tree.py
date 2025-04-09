import turtle as t

def draw_tree(length, level):
    if level <= 0:
        return 
    t.forward(length)
    t.right(45)
    draw_tree(length / 2, level - 1)
    t.left(90)
    draw_tree(length / 2, level - 1)
    t.right(45)
    t.backward(length)
    

t.pensize(2)
t.color("green")
t.left(90)
draw_tree(100, 6)
t.done()
