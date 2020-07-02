import tkinter as tk  # tkinter 모듈을 포함시킨다.


dic={}                            # 딕셔너리 변수 선언합니다.

def fileOpen():                   # 불러오기 버튼을 누르면 실행되는 함수입니다.
    list_text.delete("1.0","end") # 불러오기를 누르면 list_text는 초기화되도록 합니다.
    file = open("Data.txt","r")   # r 모드로 "Date.txt"파일을 읽어옵니다.
    if file != None:              # Data.txt의 내용을 끝가지 읽을수있도록 합니다.
        lines = file.read()       # lines 변수에 Data.txt에서 읽어온 내용을 넣습니다.
        words = lines.split('\n') # lines에서 읽어온 내용을 \n으로 rstrip과 같은 효과를 내어 공백을 기준으로 단어를 분류하여 줍니다.
        for item in words: 
            if(item != ''):         # 공백 체크
             item = item.split(' ') # 공백 구분 
             dic[item[0]] = item[1] # 키값 밸류값 셋팅
       
        for item_dic in sorted(dic.keys(),reverse=True):                # 딕셔너리에 있는 키값기준으로 역순으로 정렬시킨 딕셔너리를 list_text에 출력하기위해 for문을 사용합니다. 
            list_text.insert('1.0', item_dic+' '+dic[item_dic]+'\n')    # 정렬된 딕셔너리를 list_text에 출력합니다.
        file.close()                                                    # file을 종료하여 줍니다.
    print(dic)

def addkey():   # 추가 버튼을 누르면 실행되는 함수입니다.
    list_text.delete("1.0","end")                                       # 추가를 누르면 list_text는 초기화되도록 합니다.
    dic[name_text.get()] = num_text.get()                               # entry안에 있는 내용을 딕셔너리의 키값 밸류값에 넣어줍니다.
    for item_dic in sorted(dic.keys(),reverse=True):                    # 딕셔너리에 있는 키값기준으로 역순으로 정렬시킨 딕셔너리를 list_text에 출력하기위해 for문을 사용합니다. 
            list_text.insert('1.0', item_dic+' '+dic[item_dic]+'\n')    # 정렬된 딕셔너리를 list_text에 출력합니다.
    

def deletekey():  # 삭제 버튼을 누르면 실행되는 함수입니다.
    num_text.delete(0,tk.END)                                           # 삭제 버튼을 누르면 num_text entry에 적혀있는 내용을 초기화 시키도록 합니다.
    if name_text.get() in dic.keys():                                   # 딕셔너리의 키값중에 name_text entry의 값과 일치하는 것이 있는지 확인합니다.
        num_text.insert(0,"삭제하였습니다.")                            # 만약 일치한다면 num_text entry에 "삭제하였습니다"를 출력합니다.
        del(dic[name_text.get()])                                       # 딕셔너리에 있는 name_text entry값과 일치하는값을 삭제합니다.
        list_text.delete("1.0","end")                                   # list_text를 업데이트 시키기위해 초기화를 시킵니다.
        for item_dic in sorted(dic.keys(),reverse=True):                # 딕셔너리에 있는 키값기준으로 역순으로 정렬시킨 딕셔너리를 list_text에 출력하기위해 for문을 사용합니다. 
            list_text.insert('1.0', item_dic+' '+dic[item_dic]+'\n')    # 정렬된 딕셔너리를 list_text에 출력합니다.
    else : # 원하는 키값이 딕셔너리에 없는 경우 
        num_text.insert(0,"찾는 사람이 없습니다.")                      # 위의 조건일 경우 num_text entry에 "찾는 사람이 없습니다"를 출력합니다. 
        
       
def searchingkey(): # 검색 버튼을 누르면 실행되는 함수입니다.
    num_text.delete(0,tk.END)                                           # 검색 버튼을 누르면 num_text entry에 적혀있는 내용을 초기화 시키도록 합니다.
    if name_text.get() in dic.keys():                                   # 딕셔너리 키값중에 name_text entry의 값과 일치하는 것이 있는지 확인합니다.
        num_text.insert(0, dic[name_text.get()])                        # 위의 조건이 맞다면 그 키값의 밸류값을 num_text entry에 출력하게 합니다.
    else : # 원하는 키값이 딕셔너리에 없는 경우
        num_text.insert(0,"찾는 사람이 없습니다.")                       # 위의 조건일 경우 num_text entry에 "찾는 사람이 없습니다"를 출력합니다.

def savefiling():  # 저장 버튼을 누르면 실행되는 함수입니다.
        file_write = open("Data.txt","w")                               # 저장 버튼이 눌려지면 Data.txt 파일에 w모드로 파일에 덮어서 새로 씁니다.
        for item_dic in dic:                                            # 딕셔너리를 파일에 적기위한 for문입니다.
            file_write.write(item_dic+' '+dic[item_dic]+'\n')           # 딕셔너리에 저장된 키와 밸류값을 file에 저장합니다.
    
window = tk.Tk()                                                        # window의 이름으로 tk설정
window.title("phone_book")                                              # 제목 설정
canvas = tk.Canvas(window)                                              # 윈도우를 생성하고 윈도우 안에 캔버스를 생성한다.

name_Label = tk.Label(window, text="이름:")                             # name_label을 window에 배치하기위해 텍스트를 설정하여 선언합니다.
num_Label = tk.Label(window, text="번호:")                              # num_label을 window에 배치하기위해 텍스트를 설정하여 선언합니다.
name_Label.grid(row=0,column=0)                                         # 0,0위치에 그리드 레이블을 배치합니다.
num_Label.grid(row=1,column=0)                                          # 1,0위치에 그리드 레이블을 배치합니다.

name_text = tk.Entry(window,bg="white", fg="black")                     # name_text를 window에 배치하기위해 배경색은 흰색, 글자색은 검은색으로 설정하여 선언합니다.
num_text = tk.Entry(window,bg="white", fg="black")                      # num_text를 window에 배치하기위해 배경색은 흰색, 글자색은 검은색으로 설정하여 선언합니다.
name_text.grid(row=0,column=1,columnspan=4)                             # 0,1위치에 columnspan의 크기는 4로 설정하여 그리드 레이블을 배치합니다.
num_text.grid(row=1,column=1,columnspan=4)                              # 1,1위치에 columnspan의 크기는 4로 설정하여 그리드 레이블을 배치합니다.

adding_btn = tk.Button(window, text="추가", command=addkey)       # adding_btn을 window에 배치하기위해 텍스트 설정과 클릭시 addkey함수가 실행되도록 선언합니다.
deleting_btn = tk.Button(window, text="삭제", command=deletekey)  # deleting_btn을 window에 배치하기위해 텍스트 설정과 클릭시 deletekey함수가 실행되도록 선언합니다.
search_btn = tk.Button(window, text="검색", command=searchingkey) # search_btn을 window에 배치하기위해 텍스트 설정과 클릭시 searchingkey함수가 실행되도록 선언합니다.
save_btn = tk.Button(window, text="저장", command=savefiling)     # save_btn을 window에 배치하기위해 텍스트 설정과 클릭시 savefiling함수가 실행되도록 선언합니다.
open_btn = tk.Button(window, text="불러오기", command=fileOpen)   # open_btn을 window에 배치하기 위해 텍스트 설정과 클릭시 fileopen함수가 실행되도록 선언합니다.

adding_btn.grid(row=2,column=0)     # 2,0위치에 그리드 레이블을 배치합니다.
deleting_btn.grid(row=2,column=1)   # 2,1위치에 그리드 레이블을 배치합니다.
search_btn.grid(row=2,column=2)     # 2,2위치에 그리드 레이블을 배치합니다.
save_btn.grid(row=2,column=3)       # 2,3위치에 그리드 레이블을 배치합니다.
open_btn.grid(row=2,column=4)       # 2,4위치에 그리드 레이블을 배치합니다.


list_text = tk.Text(window,width=30)        # list_text를 window에 배치하기위해 크기를 30으로 설정하여 선언합니다.
list_text.grid(row=3,column=0,columnspan=5) # 3,0위치에 columnspan의 크기는 5로 설정하여 그리드 레이블을 배치합니다. 


window.mainloop() # 윈도우 창을 윈도우가 종료될 때 까지 실행합니다.
