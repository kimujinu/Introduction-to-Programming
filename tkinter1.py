#2020.06.02

from tkinter import * # tkinter에 포함된 모든 라이브러리를 가져온다.

def process():
    temperature = float(e1.get())
    mytemp = (temperature-32)*5/9
    e2.insert(0,str(mytemp))

def process2(): 
    temperature = float(e1.get())
    mytemp = (temperature-32)*5/9
    e2.insert(0,str(mytemp))
    
root = Tk()

L1 = Label(root, text="화씨",font="gelvetica 16 italic")
L2 = Label(root, text="섭씨")
L1.grid(row=0,column=0)
L2.grid(row=1,column=0)

e1 = Entry(root,bg="yellow", fg="black")
e2 = Entry(root)
e1.grid(row=0,column=1)
e2.grid(row=1,column=1)

b1 = Button(root, text="화씨->섭씨", command=process)
b2 = Button(root, text="섭씨->화씨", command=process2)
b1.grid(row=2,column=0)
b2.grid(row=2,column=1)

root.mainloop() # 프로그램을 종료하지 않고 언제 사용자로 부터 입력을 받을지 루프를 돌고 있음.

