class Car:
    brand = "현대" # 클래스 변수, 특징:모든 객체에서 하나의 변수를 다 공유하는것. 전역변수와 비슷함.
    def __init__(self,speed = 10,color="red",model="none"): # 기본값을 꼭 넣어줘야 함.
        self.speed = speed # self를 붙여줘야 객체변수가 됨.
        self.color = color
        self.model = model
        # length = 50 이라면 self.가 적혀있지 않기 때문에 지역변수 처리라서 init함수가 끝나게 되면 length변수가 사라짐.
        
    def drive(self):
        self.speed=10 # 객체 변수 , 객체마다 가지고 있는 것. 객체 내부에서 사용되는 변수

    def __srt__(self): # 이 클래스에 대한 인터페이스 다른 객체와 의사소통을 위한 메소드
        return "이거봐"

    def __repr__(self): #이 클래스에 대한 설명같은 것 적는 메소드, 사용자에게 이 클래스에 대한 설명을 적는 메소드
        print("차")

    

myCar = Car()
myCar.drive()       # 객체 안의 drive() 메소드가 호출된다.
print(myCar.speed)  # 10이 출력된다. 위의 drive가 호출되어야 speed를 참조할수 있음.
print(myCar.brand)  

myCar2 = Car()
myCar2.drive()
myCar2.speed = 20
myCar2.brand = "기아" # 새로 생성하는것
Car.brand = "기아" # myCar3.brand 변수의 이름도 바뀜. 클래스 변수 이름을 바뀌기 위함.
print(myCar2.speed)
print(myCar2.brand)

myCar3 = Car()
myCar3.drive()
myCar3.speed = 30
myCar3.brand = "삼성"
print(myCar3.speed)
print(myCar3.brand)
print(Car.brand)

myCar4 = Car(60,"blue")
print(myCar4.speed)
print(myCar4.color)
print(myCar4.brand)
print(myCar4)

