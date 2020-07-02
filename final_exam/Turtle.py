from turtle import * # turtle 라이브러리안에 있는 모든 메소드 사용할수 있도록 선언합니다.
import random        # random 라이브러리 선언



class myTurtle(Turtle): # myTurtle 클래스 선언합니다.
    def drawstar(self,x,y): # drawstar 메소드를 선언합니다.
        star_color = random.choice(["white", "yellow", "blue", "skyblue", "orange", "green"]) # 별의 색깔을 랜덤하게 선택하는 소스코드입니다.
        star_size = random.randint(10,100)                                                    # 별의 크기를 랜덤하게 선택하는 소스코드입니다.
        print(star_color) 
        print(star_size)       
        self.begin_fill() # 색깔채우기를 시작합니다.
        self.penup()      # 펜을 올려 x,y의 좌표에 가기전에 색깔이 적히지 않도록 합니다.
        self.goto(x,y)    # 클릭한 좌표로 이동합니다.
        self.pendown()    # 이동한 후 펜을 내려 색칠 할 수 있도록 합니다.
        for i in range(1, 6): # 별을 그리는 for문입니다.
            self.pencolor(star_color) # 위에서 랜덤으로 정해진 색깔로 펜의 색깔을 정합니다.
            self.fillcolor(star_color) # 위에서 랜덤하게 정해진 색깔로 별을 색칠하기 시작합니다.
            self.left(144)              # 별을 그리기 위해 144 왼쪽으로 돌립니다.
            self.forward(star_size)     # 별의 크기만큼 앞으로 전진합니다.
            
        self.end_fill()                 # 색깔 칠하기를 종료합니다. 
