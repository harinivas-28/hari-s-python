import turtle

pen=turtle.Turtle()
pen.color("red", "blue")
for i in range(5):
    pen.left(45)
    pen.forward(100)
    pen.right(135)
    pen.forward(100)
    pen.right(-45)

turtle.done()