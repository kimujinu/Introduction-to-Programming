dict = {}

while (input("물건을 입력하시겠습니까(y/n):") == "y"):
    key = input("물건 이름을 입력하세요:")
    value = int(input("개수를 입력하세요:"))
    dict[key] = value

while (input("물건을 검색하시겠습니까(y/n):") == "y"):
    key = input("물건 이름을 입력하세요:")
    if(key in dict):
        print("물건의 개수는", dict[key],"입니다.")
    else :
        print("입력하신 이름의 물건에 해당하는 정보가 없습니다.")

