import turtle

t = turtle.Turtle()
t.shape("turtle")

t.penup() #펜을 올려서 그림이 그려지지 않게 하는 함수
t.goto(100,100) #거북이를 100 100으로 이동시킨다.
#t.left(45)
#t.fd(100*(2**0.5))
t.write("거북이가 여기로 오면 양수 입니다.")
t.goto(100,0)
t.write("거북이가 여기로 오면 0입니다.")
t.goto(100,-100)
t.write("거북이가 여기로 오면 음수입니다.")
t.goto(0,0)

t.pendown() #penup반대
s=int(turtle.textinput("숫자입력박스","숫자를 입력하세요: "))

if s>0:
    t.goto(100,100)
if s==0 :
    t.goto(100,0)
if s<0 :
    t.goto(100,-100)



