import turtle
import random
import time
#background
pen=turtle.Turtle()
pen.screen.bgcolor("lightblue")
#Setting players
pen.shape('turtle')
player_one=pen
player_one.penup()
player_one.color("red")
player_one.goto(-300,250)
player_two=player_one.clone()
player_two.penup()
player_two.goto(-300,-250)
player_two.color("blue")
#Finish line
player_one.goto(300,-300)
player_one.left(90)
player_one.pendown()
player_one.color("#000000")
player_one.goto(300,280)
player_one.write('Finish', font=("Roboto",20))
player_one.penup()
player_one.goto(-300,250)
player_one.rt(90)
#now play game
die=[1,2,3,4,5,6]
player_one.pendown()
player_two.pendown()
for i in range(30):
    if(player_one.position()>=(300,300)):
        print("Player One Won")
        player_one.penup()
        player_one.goto(-100,0)
        player_one.pendown()
        player_one.write('Player One Won', font=('Roboto',24))
        player_one.hideturtle()
        break
    elif(player_two.position()>=(300,-300)):
        print("Player Two Won")
        player_two.penup()
        player_two.goto(-100,0)
        player_two.pendown()
        player_two.write('Player Two Won', font=('Roboto',24))
        player_one.hideturtle()
        break
    else:
        choice=random.choice(die)
        player_one.fd(30*choice)
        time.sleep(1)
        choice2=random.choice(die)
        player_two.fd(30*choice2)
        time.sleep(1)


turtle.done()
