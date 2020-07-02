import random


def cal(radius) :
    area = 3.14 * radius ** 2
    cir = 3.14 * radius *2
    return [area, cir] # (area, cir) 튜플의 형식으로 넘기는것, [area, cir] 리스트 형식으로 넘기는것

result1 = cal(1)
result1.append(0)
print(result1)


a=[3,4,2,3] #리스트는 변경이 가능함
b=(3,2,4,3) #튜플은 변경이 불가능, 고정값


random.choice('abcdefghij')



