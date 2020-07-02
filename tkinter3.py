from tkinter import *

changecolor="red"

def paint(event):
    x1, y1 = (event.x-1), (event.y+1)
    x2, y2 = (event.x-1), (event.y+1)
    canvas.create_oval(x1, y1, x2, y2, fill=changecolor, outline= changecolor)

def change_color():
    global changecolor

    if(changecolor == "red"):
        changecolor="blue"
    else :
        changecolor="red"
    

root = Tk()

canvas = Canvas(root)
canvas.pack()
canvas.bind("<B1-Motion>",paint)

button = Button(root, text="색변환",command=change_color)
button.pack()


root.mainloop()
