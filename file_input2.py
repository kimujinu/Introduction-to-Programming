infile = open("test.txt","w",encoding="UTF8") # w는 완전 새로 쓰이고

infile.write("김잔우 010-1315-1616\n")

infile.close() #close를 하지않으면 저장이 되지않음.

infile2 = open("test.txt","a",encoding="UTF8") # a는 덧붙이는것

infile2.write("김찌뽀 010-1315-1616\n")

infile2.close()

