name1 = input("입력파일이름(확장자까지 넣어주세요)")
name2 = input("출력파일이름(확장자까지 넣어주세요)")

file1 = open(name1,"r", encoding="UTF8")
file2 = open(name2,"w")

data = file1.read()
file2.write(data)

file1.close()
file2.close() 
