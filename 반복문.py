import turtle
t=turtle.Turtle()
t.shape("turtle")

for i in [1,2,3,4,5]:
    print("방문을 환영합니다.")

for i in [1,5,7,10,5]:
    print("ㅎㅇ",i)

for i in range(10):
    print("Zzz")

for i in [1,2,3,4,5]:
    print("9*", i , "=", 9*i)

a = range(10) #a=0~9

b = range(2,10,2) # b = 2,4,6,8,10  2부터 9까지 2씩 증가.

for i in range(2,10,2) :
    print(i)


a = int(input("그릴 원의 개수를 입력하시오: "))  
deg = 360/a

for i in range(a) :
    t.circle(100)
    t.right(deg)


A = [1,5,4,3,2]

for pknu in A:
    print(pknu)

# 정삼각형 그리기
for i in range(3):
    t.forward(100)
    t.left(360/3)


c = int(turtle.textinput("","변의 개수를 입력하세요: "))
deg = int(360/c)

for i in range(c) :
    t.forward(100)
    t.left(deg)


    



