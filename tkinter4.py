from tkinter import *


def push1(event):
    e1.insert('end',"1")

def push2(event):
    e1.insert('end',"2")

def pushC(event):
    e1.delete(0,'end')

root = Tk()
root.title("계산기")

e1 = Entry(root, width=33, bg="yellow")
e1.grid(row=0, column=0, columnspan=5)

list = [["7","8","9","/","C"],
        ["4","5","6","*"," "],
        ["1","2","3","-"," "],
        ["0",".","=","+"," "]]

for row in range(len(list)):
    for colum in range(len(list[0])):
        b1=Button(root, text=list[row][colum], width=5)
        b1.grid(row = row+1, column = colum)
        if(list[row][colum] == "1"):
            b1.bind("<Button-1>",push1)
        elif(list[row][colum]=="2"):
            b1.bind("<Button-1>",push2)
        elif(list[row][colum]=="C"):
            b1.bind("<Button-1>",pushC)
            
        
