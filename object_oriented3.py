from turtle import *

class Ball:
        def __init__(self, color, size, speed):
            # 공의 위치
            self.x = 0
            self.y = 0
            
            # 공의 속도 벡터
            self.xspeed = speed
            self.yspeed = speed
            
            # 공의 크기
            self.size = size
            
            # 공의 색상
            self.color = color
            self.turtle = Turtle()
            self.turtle.shape("circle")
            self.turtle.color(color, color)
            self.turtle.resizemode("user")
            self.turtle.shapesize(size, size, 10)

            # 메소드 정의
        def move(self):
            self.x += self.xspeed
            self.y += self.yspeed
            self.turtle.goto(self.x, self.y)

        def rotate(self, deg):
            self.turtle.right(deg)
        
        def move2(self, distance):
            self.turtle.fd(distance)
            
ball = Ball("red", 2, 100)
ball2 = Ball("green",1,200)
ball3 = Ball("blue",3, 300)


ball.move()
ball2.rotate(90)
ball2.move2(100)
ball3.rotate(180)
ball3.move2(180)
