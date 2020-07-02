a = [] # []은 리스트 ()은 튜플

a.append("아이언맨")
a.append(14)
a.append(0.5)

print(a[:2]) #리스트 복사할때 사용
print(a[2:])
print(a[:])

a.insert(1,"나봉")
print(a)

a.remove(14)
print(a)

if "나봉" in a:
    print("yes")

for i in a:
    print(i)


del a[0]
print(a)

last_index = a.pop()
print(last_index)

a.append("진억")

print(a.index("진억"))
print(len(a))

for i in range(0,len(a)) :
    print(a[i])

a.append("김찌뽀")
print(a)

a.sort()
print(a)

a.reverse()
print(a)



