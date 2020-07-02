import turtle                                   #라이브러리 가져오기

t= turtle.Turtle()                              #해당 프로젝트에서 t라는 이름으로 라이브러리를 사용한다고 선언
t.shape("turtle")                               #거북이 모양으로 설정
                                                
color = []                                      #color 리스트를 선언 및 초기화 합니다.
color.append(input("색상 #1을 입력하시오: "))   #append함수를 사용하여 원소를 [0]번째 리스트에 넣습니다.
color.append(input("색상 #2을 입력하시오: "))   #append함수를 사용하여 원소를 [1]번째 리스트에 넣습니다.
color.append(input("색상 #3을 입력하시오: "))   #append함수를 사용하여 원소를 [2]번째 리스트에 넣습니다.

t.fillcolor(color[0])                           #fillcolor는 채워지는 색을 지정하는 함수로 색깔 이름이 파라미터로 들어간다.
t.begin_fill()                                  #color[0] 색으로 색깔을 채우기 시작한다.
t.circle(50)                                    #반지름이 50인 원을 그린다. Begin_fill이 앞서 선언되어 있다면, fillcolor로 지정된 색상으로 채워진 원이 그려진다.
t.end_fill()                                    #색깔 채우기를 종료한다. 이 명령어 이후에 circle(50)으로 원을 그려도 색깔이 채워지지 않는다.

t.penup()                                       #펜을 올려서 그림이 그려지지 않게 하는 함수 
t.forward(100)                                  #다음 원을 그리기위해서 앞으로 100만큼 이동 시키는 함수
t.pendown()                                     #펜을 내려서 그다음 원을 그리기위해 준비

t.fillcolor(color[1])                           #fillcolor는 채워지는 색을 지정하는 함수로 색깔 이름이 파라미터로 들어간다.
t.begin_fill()                                  #color[1]의 색깔로 색을 채우기 시작한다.
t.circle(50)                                    #반지름이 50인 원을 그린다. Begin_fill이 앞서 선언되어 있다면, fillcolor로 지정된 색상으로 채워진 원이 그려진다.
t.end_fill()                                    #색깔 채우기를 종료한다. 이 명령어 이후에 circle(50)으로 원을 그려도 색깔이 채워지지 않는다.

t.penup()                                       #펜을 올려서 그림이 그려지지 않게 하는 함수
t.forward(100)                                  #다음 원을 그리기위해서 앞으로 100만큼 이동 시키는 함수
t.pendown()                                     #펜을 내려서 그다음 원을 그리기위해 준비

t.fillcolor(color[2])                           #fillcolor는 채워지는 색을 지정하는 함수로 색깔 이름이 파라미터로 들어간다.
t.begin_fill()                                  #color[2] 색으로 색깔을 채우기 시작한다.
t.circle(50)                                    #반지름이 50인 원을 그린다. Begin_fill이 앞서 선언되어 있다면, fillcolor로 지정된 색상으로 채워진 원이 그려진다.
t.end_fill()                                    #색깔 채우기를 종료한다. 이 명령어 이후에 circle(50)으로 원을 그려도 색깔이 채워지지 않는다.
