from turtle import *

class MyTurtle(Turtle):
    def square(self, length):
        for i in range(0,4):
            self.fd(length)
            self.left(90)

