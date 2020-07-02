print("안녕하세요?")
name = input("이름이 어떻게 되시나요?")
print("만나서 반갑습니다.",name,"씨")
print("이름의 길이는 다음과 같군요.",len(name))
print("이름의 길이는 다음과 같군요."+str(len(name)))
print("이름의 길이는 다음과 같군요.%d"%len(name))
print("이름의 길이는 다음과 같군요.%s"%5) #이런것도 가능함
print("이름의 길이는 다음과 같군요.%s %s"%(7,8)) #이런것도 가능함
age = int(input("나이가 어떻게 되시나요?")) 
print("내년이면",age+1,"살이 되시는군요.")
age2 = input("나이가 어떻게 되시나요?")
print("내년이면",int(age2)+1,"살이 되시는군요.")

print("abc",end=' ') #end 원하는거 넣는 함수
print("acd")

names = ["나봉", "찌뽀", "니뽀", "진뽀"]
names[0]
names[0][0]
names.append("나억이") #끝에 추가
names.count("나봉") #나봉 카운트
#names.clear()
names.sort() 
