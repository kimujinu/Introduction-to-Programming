import turtle                                              # 라이브러리 가져오기

t = turtle.Turtle()                                        # 해당 프로젝트에서 t라는 이름으로 라이브러리 사용한다고 선언한다.
t.shape("turtle")                                          # 거북이 모양으로 설정

bigcircle_x1 = int(input("큰 원의 중심좌표 x1 : "))        # 큰원의 중심좌표 x1을 입력받는다. int()로 하는 이유는 입력받는 타입을 정수로 바꾸어주기위해서 입니다. 밑의 경우 모두 마찬가지 입니다.
bigcircle_y1 = int(input("큰 원의 중심좌표 y1 : "))        # 큰원의 중심좌표 y1을 입력받는다. 
bigcircle_radius= int(input("큰 원의 반지름 : "))          # 큰원의 반지름을 입력받는다.

smallcircle_x2 = int(input("작은 원의 중심좌표 x2 : "))    # 작은 원의 중심좌표 x2를 입력받는다.
smallcircle_y2 = int(input("작은 원의 중심좌표 y2 : "))    # 작은 원의 중심좌표 y2를 입력받는다.
smallcircle_radius= int(input("작은 원의 반지름 : "))      # 작은 원의 반지름을 입력받는다.

t.penup()                                                  # 펜을 올려서 그림이 그려지지 않게 하는 함수 밑의 첫좌표로 이동하기 까지 그림을 못그리게 하기위해서 사용
t.goto(bigcircle_x1,bigcircle_y1-bigcircle_radius)         # 위의 입력받은 좌표로 거북이를 이동시킨다.
t.pendown()                                                # 펜을 내려 다시 거북이가 그림을 그리게 한다.
t.circle(bigcircle_radius)                                 # 입력받은 radius 만큼 거북이가 원을 그린다.

t.penup()                                                  # 펜을 올려서 그림이 그려지지 않게 하는 함수
t.goto(smallcircle_x2,smallcircle_y2-smallcircle_radius)   # 위의 입력받은 좌표로 거북이를 이동 시킨다.
t.pendown()                                                # 펜을 내려 다시 거북이가 그림을 그리게 한다.
t.circle(smallcircle_radius)                               # 입력받은 radius 만큼 거북이가 원을 그린다.

circles_distance = ((bigcircle_x1-smallcircle_x2)**2 + (bigcircle_y1-smallcircle_y2)**2)**0.5 # 원의 중심점 사이의 거리를 circles_distance라는 이름을 가진 변수안에 넣습니다. "**"이것은 제곱을 말하는겁니다.



if(circles_distance+smallcircle_radius < bigcircle_radius) : #if문으로 원의 중심점 사이의 거리+작은 원의 반지름을 합쳐서 큰 원의 반지름의 크기와 비교하여 참이면 밑의 소스코드를 실행합니다.
    t.write("작은 원은 큰 원 내부에 있습니다.")              #위의 조건이 참이라면 거북이가 "작은 원은 큰 원 내부에 있습니다"라는 문장을 출력합니다.    
elif(circles_distance<bigcircle_radius+smallcircle_radius) : # 만약 위의 조건이 참이 아니라면 원의 중심점 사이의 거리,큰원의 반지름 + 작은 원의 반지름의 크기를비교하여 참이라면 해당 소스코드가 실행됩니다.
    t.write("작은 원은 큰 원에 걸쳐져 있습니다.")              # #위의 조건이 참이라면 거북이가 "작은 원은 큰 원에 걸쳐 있습니다"라는 문장을 출력합니다.
else :                                                       #만약 위의 조건 2개가 모두 참이 아니라면 실행되는 소스코드 입니다.
    t.write("작은 원은 큰 원 외부에 있습니다.")              #위의 조건이 참이라면 거북이가 "작은 원은 큰 원 외부에 있습니다"라는 문장을 출력합니다.
