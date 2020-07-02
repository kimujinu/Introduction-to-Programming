import turtle
import random
import math

player= turtle.Turtle()
player.color("blue")
player.shape("turtle")
player.penup()
player.speed(0)


a1=turtle.Turtle()
a1.color("red")
a1.shape("circle")
a1.penup()
a1.speed(0)
a1.goto(random.randint(-300, 300),random.randint(-300,300))


a2=turtle.Turtle()
a2.color("red")
a2.shape("circle")
a2.penup()
a2.speed(0)
a2.goto(random.randint(-300, 300),random.randint(-300,300))

def turnleft():
    player.left(30)

def turnright():
    player.right(30)

def forward():
    player.forward(4)

def backward():
    player.backward(4)


screen = player.getscreen()
screen.onkeypress(turnleft, "Left")
screen.onkeypress(turnright, "Right")
screen.onkeypress(forward, "Up")
screen.onkeypress(backward, "Down")
screen.listen()

def play() :
    #player.forward(4)
    a1.forward(2)
    a2.forward(2)
    a1_p=a1.position()
    a2_p=a2.position()
    player_p=player.position()

    dis_a1p=math.sqrt((a1_p[0]-player_p[0])**2 + (a1_p[1]-player_p[1])**2)
    dis_a2p=math.sqrt((a2_p[0]-player_p[0])**2 + (a2_p[1]-player_p[1])**2)

    if(dis_a1p <=4 or dis_a2p<=4):
        player.write("game over")
    else:
        screen.ontimer(play, 10)
    


screen.ontimer(play, 10)
