from tkinter import *

def change_img():
    path = inputBox.get()
    img = PhotoImage(file = path)
    imageLabel.configure(image= img)
    imageLabel.image = img

root = Tk()

photo = PhotoImage(file="Lenna.png")
imageLabel = Label(root, image=photo)
imageLabel.pack()

imputBox = Entry(root)
inputBox.pack()

button = Button(root,text="Submit", command=change_img)
button.pack()

root.mainloop()

