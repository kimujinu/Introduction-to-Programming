import tkinter as tk

def open():
    pass

def quit():
    window.quit()
    
window = tk.Tk()
menubar = tk.Menu(window)
filemenu = tk.Menu(menubar)
infomenu = tk.Menu(menubar)

filemenu.add_command(label="열기", command=open)
filemenu.add_command(label="종료", command=quit)
filemenu.add_command(label="저장")

infomenu.add_command(label="만든이")

menubar.add_cascade(label="파일", menu=filemenu)
menubar.add_cascade(label="정보", menu=infomenu)

window.config(menu=menubar)
window.mainloop()
