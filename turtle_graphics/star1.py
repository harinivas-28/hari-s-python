import turtle

turtle.color("red", "yellow")
turtle.speed(10)
turtle.begin_fill()
for i in range(100):
    turtle.forward(200)
    turtle.left(170)
turtle.end_fill()

turtle.done()