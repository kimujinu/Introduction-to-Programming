import turtle
t= turtle.Turtle();
t.shape("turtle");

def square(length) :        #이 함수는 입력받은 length 길이 만큼의 변을 가진 정사각형을 그린다.
    for i in range(4):          # length는 양수로 정 사각형의 한변의 길이를 뜻한다.
        t.forward(length)       # 이 함수는 리턴한다.
        t.left(90)


def n_polygon(n,length):  # n각형을 그리는 함수정의
    for i in range(n):      
        t.forward(length)
        t.left(360/n)

for i in range(3):
    square(100);
    t.penup();
    t.forward(150);
    t.pendown();

for i in range(10):
    t.left(20)
    n_polygon(6,100)
