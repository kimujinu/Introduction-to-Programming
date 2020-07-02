import random #행맨 게

wordfile = open("word.txt","r")
words = wordfile.readlines()
solution = random.choice(words) #리스트중 하나를 랜덤으로 뽑아줌

try1 = 0
word_index = 0

while True:
    solution = solution.rstrip() #단어 우측 끝에 있는 공백삭제
    length = len(solution) # 맞춰야할 문자의 개수(단어의 길이)

    for i in range(length):
        if(i<word_index):
            print(solution[i], end="") # 붙여 쓰기위해 쓰임 end=""
        else:
            print('_', end="")
    print("")
    
    in_char = input("단어를 추측하시오:")
    try1 = try1 + 1
    if(solution[word_index]==in_char):
        word_index = word_index + 1
    
    if(word_index == length):
        break



