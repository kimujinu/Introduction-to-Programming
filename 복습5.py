import turtle
import math

player=turtle.Turtle()
player.shape("turtle")
screen=player.getscreen()

def turnleft() :
    player.left(5)

def turnright() :
    player.right(5)

def fire():
    x = 0
    y = 0
    velocity = 50           # 초기속도50픽셀/sec
    angle = player.heading()# 초기각도
    vx= velocity * math.cos(angle * 3.14 / 180.0)# 도-> 라디안
    vy= velocity * math.sin(angle * 3.14 / 180.0)# 도-> 라디안
    player.speed(0)
    while player.ycor() >= 0 :# y좌표가음수가될때까지
            vx= vx
            vy= vy - 10
            x = x + vx
            y = y + vy
            player.goto(x, y)

            
    player.up()
    player.goto(0,0)
    player.down()
        
        
screen.onkeypress(turnleft, "Left")
screen.onkeypress(turnright, "Right")
screen.onkeypress(fire, "space")# 사용자가스페이스키를누르면
screen.listen()
