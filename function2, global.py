
def cal_area(radius = 100): # 매개변수 기본값 100 선언
    global r        # 전역변수 선언, 왠만하면 쓰지 않는것이 좋음.
    result = 3.14 * r**2
    r=100
    return result

r= float(input("원의 반지름: "))
area = cal_area()
print(area,r)


################################################

def greet(name, msg1="temp", msg2="temp", msg3="temp"): # 매개변수 기본값은 뒤쪽순서대로 채워야된다. 앞에부터 채우면 에러남.
    print("안녕", name+", "+msg1 +msg2 + msg3)

greet("나봉","찌뽀","니뽀","나억")

