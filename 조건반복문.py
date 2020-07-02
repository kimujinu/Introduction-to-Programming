import turtle
t=turtle.Turtle()
t.shape("turtle")

password=""

while password!= "pythonisfun" :
    password = input("암호를 입력하세요: ")
print("로그인 성공")


sum = 0
i = 1
while i <= 10 :
    sum = sum + i
    i= i + 1

print(sum)

s = int(turtle.textinput("","몇각형을 원하시나요?"))

i = 0
while i < s:
    t.forward(100)
    t.left(360/s)
    i = i + 1;

