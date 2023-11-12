import turtle

pen = turtle.Turtle()
pen.color("magenta", "yellow")
pen.begin_fill()
for i in range(4):
    pen.left(45)
    pen.forward(100)
    pen.right(135)
    pen.forward(100)
pen.end_fill()
turtle.done()