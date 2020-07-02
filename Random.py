import random 
#random.seed(0) #랜덤순열이 바뀜. (1)이렇게 하면 seed(0)이 가지고있는 순열 seed(1)이 가지고 있는 순열이 다름
time = random.randint(1,24)
sunny = random.choice([True, False])

if time>=6 and time<=9 and sunny :
    print("좋은 아침입니다. 지금 시각은 %d시 입니다" %time)
    print("화창하네이")
    print(sunny)
    print("종달새 존나게 우네이")
else :
    print("지금 시각은 %d시 입니다" %time)
    print("현재 날씨가 화창하지 않네이")
    print(sunny)
    print("종달새 닥치고")

