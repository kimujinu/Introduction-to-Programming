from PIL import Image, ImageTk  # PIL 모듈에서 몇 개의 클래스를 포함시킨다.
import random # random 라이브러리 선언 
import tkinter as tk  # tkinter 모듈을 포함시킨다.


def change_rock(): # 사용자가 바위 버튼을 눌렀을 때 실행되는 함수입니다.
    com_random = random.randint(0,2)      # 0~2까지 번호가 랜덤하게 나오도록 하는 코드입니다.
    print('rock') 
    rock_image = Image.open("rock.png")   #이미지를 불러온다.
    rock_rotate = rock_image.rotate(270)  #영상을 270도 회전한다.
    img = ImageTk.PhotoImage(rock_rotate) #tk 형식으로 영상을 변환한다.
    user_imageLabel.configure(image= img) # user_imageLabel의 사진의 형태를 변화시키위한 코드입니다.
    user_imageLabel.image = img           # user_imageLabel에 사진을 띄우기 위한 코드입니다.
    result_Label.configure(text= '')              # result_Label의 형태를 변화시키위한 코드입니다
    print(com_random)
    
    if com_random == 0 : # 만약 random의 숫자가 0이라면 컴퓨터는 보자기를 냅니다.
        com_paper_image = Image.open("paper.png")          # 이미지를 불러온다.
        com_paper_rotate = com_paper_image.rotate(90)      # 영상을 90도 회전한다.
        com_img = ImageTk.PhotoImage(com_paper_rotate)     # tk 형식으로 영상을 변환한다.
        com_imageLabel.configure(image= com_img)           # com_imageLabel의 사진의 형태를 변화시키위한 코드입니다.
        com_imageLabel.image = com_img                     # com_imageLabel에 사진을 띄우기 위한 코드입니다.
        
        result_Label.configure(text= '<<<<<')              # result_Label의 형태를 변화시키위한 코드입니다.
        judge_Label.configure(text= '컴퓨터 승!',fg="red") # judge_Label의 형태를 변화시키위한 코드입니다. 
    elif com_random == 1 :# 만약 random의 숫자가 1이라면 컴퓨터는 바위를 냅니다.
        com_rock_image = Image.open("rock.png")            # 이미지를 불러온다.
        com_rock_rotate = com_rock_image.rotate(90)        # 영상을 90도 회전한다.
        com_img = ImageTk.PhotoImage(com_rock_rotate)      # tk 형식으로 영상을 변환한다.
        com_imageLabel.configure(image= com_img)           # com_imageLabel의 사진의 형태를 변화시키위한 코드입니다.
        com_imageLabel.image = com_img                     # com_imageLabel에 사진을 띄우기 위한 코드입니다.
        result_Label.configure(text= '=====')              # result_Label의 형태를 변화시키위한 코드입니다.  
        judge_Label.configure(text= '무승부!',fg="gray")   # judge_Label의 형태를 변화시키위한 코드입니다.
    else : #나머지 숫자 '2'라면 컴퓨터는 가위를 냅니다.
        com_scissors_image = Image.open("scissors.png")    # 이미지를 불러온다.
        com_scissors_rotate = com_scissors_image.rotate(90)# 영상을 90도 회전한다.
        com_img = ImageTk.PhotoImage(com_scissors_rotate)  # tk 형식으로 영상을 변환한다.
        com_imageLabel.configure(image= com_img)           # com_imageLabel의 사진의 형태를 변화시키위한 코드입니다.
        com_imageLabel.image = com_img                     # com_imageLabel에 사진을 띄우기 위한 코드입니다.
        result_Label.configure(text= '>>>>>')              # result_Label의 형태를 변화시키위한 코드입니다.
        judge_Label.configure(text= '사용자 승!',fg="green") # judge_Label의 형태를 변화시키위한 코드입니다.


def change_paper(): # 사용자가 보자기 버튼을 눌렀을 때 실행되는 함수입니다.
    com_random = random.randint(0,2)       # 0~2까지 번호가 랜덤하게 나오도록 하는 코드입니다.
    print('paper')      
    paper_image = Image.open("paper.png")  #이미지를 불러온다.
    paper_rotate = paper_image.rotate(270) #영상을 270도 회전한다.
    img = ImageTk.PhotoImage(paper_rotate) # tk 형식으로 영상을 변환한다.
    user_imageLabel.configure(image= img)  # user_imageLabel의 사진의 형태를 변화시키위한 코드입니다.
    user_imageLabel.image = img            # user_imageLabel에 사진을 띄우기 위한 코드입니다.
    result_Label.configure(text= '')              # result_Label의 형태를 변화시키위한 코드입니다
    print(com_random)

    if com_random == 0 : # 만약 random의 숫자가 0이라면 컴퓨터는 보자기를 냅니다.
        com_paper_image = Image.open("paper.png")     # 이미지를 불러온다.
        com_paper_rotate = com_paper_image.rotate(90) # 영상을 90도 회전한다.
        com_img = ImageTk.PhotoImage(com_paper_rotate)# tk 형식으로 영상을 변환한다.
        com_imageLabel.configure(image= com_img)      # com_imageLabel의 사진의 형태를 변화시키위한 코드입니다.
        com_imageLabel.image = com_img                # com_imageLabel에 사진을 띄우기 위한 코드입니다.
        result_Label.configure(text= '=====')         # result_Label의 형태를 변화시키위한 코드입니다.
        judge_Label.configure(text= '무승부!',fg="gray")  # judge_Label의 형태를 변화시키위한 코드입니다. 
    elif com_random == 1 : # 만약 random의 숫자가 1이라면 컴퓨터는 바위를 냅니다.
        com_rock_image = Image.open("rock.png")     # 이미지를 불러온다.
        com_rock_rotate = com_rock_image.rotate(90) # 영상을 90도 회전한다.
        com_img = ImageTk.PhotoImage(com_rock_rotate)# tk 형식으로 영상을 변환한다.
        com_imageLabel.configure(image= com_img)     # com_imageLabel의 사진의 형태를 변화시키위한 코드입니다.
        com_imageLabel.image = com_img               # com_imageLabel에 사진을 띄우기 위한 코드입니다.
        result_Label.configure(text= '>>>>>')        # result_Label의 형태를 변화시키위한 코드입니다.
        judge_Label.configure(text= '사용자 승!',fg="green") # judge_Label의 형태를 변화시키위한 코드입니다.
    else :  #나머지 숫자 '2'라면 컴퓨터는 가위를 냅니다.
        com_scissors_image = Image.open("scissors.png")     # 이미지를 불러온다.
        com_scissors_rotate = com_scissors_image.rotate(90) # 영상을 90도 회전한다.
        com_img = ImageTk.PhotoImage(com_scissors_rotate)   # tk 형식으로 영상을 변환한다.
        com_imageLabel.configure(image= com_img)            # com_imageLabel의 사진의 형태를 변화시키위한 코드입니다.
        com_imageLabel.image = com_img                      # com_imageLabel에 사진을 띄우기 위한 코드입니다.
        result_Label.configure(text= '<<<<<')               # result_Label의 형태를 변화시키위한 코드입니다.
        judge_Label.configure(text= '컴퓨터 승!',fg="red")  # judge_Label의 형태를 변화시키위한 코드입니다.
    
    
def change_scissors(): # 사용자가 가위 버튼을 눌렀을 때 실행되는 함수입니다.
    com_random = random.randint(0,2)            # 0~2까지 번호가 랜덤하게 나오도록 하는 코드입니다.
    print('scissors')
    scissors_image = Image.open("scissors.png") # 이미지를 불러온다.
    scissors_rotate = scissors_image.rotate(270) # 영상을 270도 회전한다.
    img = ImageTk.PhotoImage(scissors_rotate)    # tk 형식으로 영상을 변환한다.
    user_imageLabel.configure(image= img)        # user_imageLabel의 사진의 형태를 변화시키위한 코드입니다.
    user_imageLabel.image = img                  # user_imageLabel에 사진을 띄우기 위한 코드입니다.
    result_Label.configure(text= '')              # result_Label의 형태를 변화시키위한 코드입니다
    print(com_random)
    
    if com_random == 0 :  # 만약 random의 숫자가 0이라면 컴퓨터는 보자기를 냅니다.
        com_paper_image = Image.open("paper.png")     # 이미지를 불러온다.
        com_paper_rotate = com_paper_image.rotate(90) # 영상을 90도 회전한다.
        com_img = ImageTk.PhotoImage(com_paper_rotate)# tk 형식으로 영상을 변환한다.
        com_imageLabel.configure(image= com_img)      # com_imageLabel의 사진의 형태를 변화시키위한 코드입니다.
        com_imageLabel.image = com_img                # com_imageLabel에 사진을 띄우기 위한 코드입니다.
        result_Label.configure(text= '>>>>>')         # result_Label의 형태를 변화시키위한 코드입니다.
        judge_Label.configure(text= '사용자 승!',fg="green") # judge_Label의 형태를 변화시키위한 코드입니다.
    elif com_random == 1 : # 만약 random의 숫자가 1이라면 컴퓨터는 바위를 냅니다.
        com_rock_image = Image.open("rock.png")     # 이미지를 불러온다.
        com_rock_rotate = com_rock_image.rotate(90) # 영상을 90도 회전한다.
        com_img = ImageTk.PhotoImage(com_rock_rotate) # tk 형식으로 영상을 변환한다.
        com_imageLabel.configure(image= com_img)      # com_imageLabel의 사진의 형태를 변화시키위한 코드입니다.
        com_imageLabel.image = com_img                # com_imageLabel에 사진을 띄우기 위한 코드입니다.
        result_Label.configure(text= '<<<<<')          # result_Label의 형태를 변화시키위한 코드입니다.
        judge_Label.configure(text= '컴퓨터 승!',fg="red") # judge_Label의 형태를 변화시키위한 코드입니다.
    else :  #나머지 숫자 '2'라면 컴퓨터는 가위를 냅니다.
        com_scissors_image = Image.open("scissors.png")     # 이미지를 불러온다.
        com_scissors_rotate = com_scissors_image.rotate(90) # 영상을 90도 회전한다.
        com_img = ImageTk.PhotoImage(com_scissors_rotate)   # tk 형식으로 영상을 변환한다.
        com_imageLabel.configure(image= com_img)            # com_imageLabel의 사진의 형태를 변화시키위한 코드입니다.
        com_imageLabel.image = com_img                      # com_imageLabel에 사진을 띄우기 위한 코드입니다.
        result_Label.configure(text= '=====')               # result_Label의 형태를 변화시키위한 코드입니다.
        judge_Label.configure(text= '무승부!',fg="gray")    # judge_Label의 형태를 변화시키위한 코드입니다.
        
    


window = tk.Tk()                        # window의 이름으로 tk설정
window.title("Rock, Scissors, Paper")   # 제목 설정
canvas = tk.Canvas(window)              # 윈도우를 생성하고 윈도우 안에 캔버스를 생성한다.

user_imageLabel = tk.Label(window)                   # 그리드 형식으로 window에 배치하기 위해 레이블로 변환한다. 
user_imageLabel.grid(row=0,column=0)                    # 0,0 위치에 주먹이미지 레이블을 배치한다.

result_Label = tk.Label(window,width=15,text="버튼을 눌러주세요",font="gelvetica 35 italic") # 가운데 결과판단 레이블을 선언한다.
result_Label.grid(row=0,column=1)                                   # 0,1 위치에 그리드 레이블을 배치한다.

com_imageLabel = tk.Label(window)                    #그리드 형식으로 배치하기 위해 레이블로 변환을 합니다.     
com_imageLabel.grid(row=0,column=2)                  # 0,2 위치에 그리드 레이블을 배치한다.

user_Label = tk.Label(window, text="사용자",font="gelvetica 25 italic") # user_label을 window에 배치하기 위해 텍스트와 폰트를 설정하여 선언합니다.
user_Label.grid(row=1,column=0)                                         # 1,0 위치에 그리드 레이블을 배치한다.

judge_Label = tk.Label(window, text="",font="gelvetica 20 italic",fg="green") #judge_label을 window에 배치하기 위해 텍스트와 폰트와 색깔을 설정하여 선언합니다.
judge_Label.grid(row=1,column=1)                                                       # 1,1 위치에 그리드 레이블을 배치한다

com_Label = tk.Label(window, text="컴퓨터",font="gelvetica 25 italic") #com_label을 window에 배치하기 위하여 텍스트와 폰트를 설정하여 선언합니다.
com_Label.grid(row=1,column=2)                                         #1,2 위치에 그리드 레이블을 배치합니다.

rock_btn = tk.Button(window, text="바위",width=20,height=5,activebackground="black",activeforeground="white",command=change_rock) # rock_btn을 window에 배치하기위해 텍스트와 클릭시 배경은 검은색, 글씨는 흰색, change_rock 함수가 실행되도록 선언합니다.
rock_btn.grid(row=2,column=0)                                                                                                     # 2,0 위치에 그리드 레이블을 배치합니다.

paper_btn = tk.Button(window, text="보",width=20,height=5,activebackground="black",activeforeground="white",command=change_paper) # paper_btn을 window에 배치하기위해 텍스트와 클릭시 배경은 검은색, 글씨는 흰색, change_paper 함수가 실행되도록 선언합니다.
paper_btn.grid(row=2,column=1)                                                                                                    # 2,1 위치에 그리드 레이블을 배치합니다.

scissors_btn = tk.Button(window, text="가위",width=20,height=5,activebackground="black",activeforeground="white",command=change_scissors) #scissors_btn을 window에 배치하기위해 텍스트와 클릭시 배경은 검은색, 글씨는 흰색, change_scissors 함수가 실행되도록 선언합니다.
scissors_btn.grid(row=2,column=2)                                                                                                         # 2,2 위치에 그리드 레이블을 배치합니다.

window.mainloop()  # 윈도우 창을 윈도우가 종료될 때 까지 실행합니다.
