from Turtle import*                         #Turtle.py 에 있는 모든 메소드를 상속하여 Prob2에서 사용할수 있도록 선언합니다.

TurtleScreen = getscreen().bgcolor("black") # 배경색을 black으로 지정합니다.
t=myTurtle()                                # t로 Turtle 안에 있는 myTurtle클래스를 사용할수있도록 객체 선언합니다.
onscreenclick(t.drawstar)                   # 화면을 클릭하면 반응하는 메소드 입니다.
mainloop()                                  # 윈도우 창을 윈도우가 종료될 때 까지 실행합니다. 
