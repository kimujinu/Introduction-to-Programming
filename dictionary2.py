dict = {"a":1,"b":3,"c":4}

for a in dict :
    print(a)

print("==========================================")

for a in dict.values():
    print(a)
    
print("==========================================")

for a in dict.keys():
    print(a)

print("==========================================")

for a in dict.items(): #튜플의 형태로 키,밸류값 출력
    print(a)

print("==========================================")

for a in sorted(dict.keys()):
    print(a)

del dict["a"]

print(dict)
