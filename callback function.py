#callback function : 이벤트가 발생했을 때, 이벤트를 처리하는 함수
import turtle
t=turtle.Turtle()
t.shape("turtle")

def square(x,y) :
    t.penup()
    t.goto(x,y)
    t.pendown()
    length = 100
    for i in range(4):
        t.forward(length)
        t.left(90)



s= turtle.Screen()
s.onscreenclick(square)

