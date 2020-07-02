infile = open("test.txt","r",encoding="UTF8") #infile=파일객체, "test.txt" 읽을 파일 "r" 읽기 모드
#lines = infile.read()
#line1 = infile.readline() 
#line2 = infile.readlines() # 각 줄에 대한 리스트를 반환
#print(lines)
#print(line1)
#print(line2)

#for line in line2 :
    #print(line)

while True:
    line = infile.readline()
    if not line : break
    print(line)
