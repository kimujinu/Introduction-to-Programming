import turtle

t=turtle.Turtle()
t.shape("turtle")

while True :
    cmd = input("명령을 입력하시오: ")
    if cmd =="I":
        t.left(90)
        t.fd(100)
    elif cmd == "R": #else if
        t.right(90)
        t.fd(100)
    else :
        print("명령어는 I 또는 R 두가지입니다.")
    
