import math
import turtle
import time
h=int(input("Enter height of the wall: "))
w=int(input("Enter width of the wall: "))
print("For 1 can covers 7 sq.cms of wall")
print("Your wall needs: ",end="")
no_of_cans=math.ceil((h*w)/7)
def paint():
    print(f"{no_of_cans} cans")
paint()
c=turtle.Turtle()
c.hideturtle()
def square():
    time.sleep(2)
    for i in range(4):
        c.forward(100)
        c.left(90)
def can():
    c.speed(5)
    c.width(5)
    c.begin_fill()
    c.color("#000000", "#FF0000")
    square()
    c.end_fill()
    c.penup()
    c.left(90)
    c.forward(100)
    c.right(90)
    c.forward(100)
    c.pendown()
    c.left(90)
    c.width(10)
    c.circle(50,180)
    c.penup()
    c.setpos(30,30)
    c.left(45)
    c.pendown()
    c.write(no_of_cans,move=False,align="left",font=('algerian',30,'normal'))
    turtle.exitonclick()
can()



