import turtle

p=turtle.Turtle()
p.screen.bgcolor("black")
p.penup()
p.setpos(0,-300)
p.pensize(2)
p.color("red")
p.pendown()
p.left(90)
p.fd(100)
p.speed(100)
p.shape('turtle')
def tree(i):
    if i<10:
        return
    else:
        p.fd(i)
        p.color("orange")
        p.circle(2)
        p.color("brown")
        p.left(30)
        tree(3*i/4)
        p.right(60)
        tree(3*i/4)
        p.left(30)
        p.bk(i)
tree(100)

turtle.done()
