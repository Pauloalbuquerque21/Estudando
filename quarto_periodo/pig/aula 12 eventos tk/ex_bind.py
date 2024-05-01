from tkinter import *

def clica(e):
    txt = f"Mouse clicado em\n {e.x}, {e.y}"
    r.configure(text = txt)

r=Label()
r.pack(expand=True, fill="bo0th")
r.master.geometry('200x200')
r.bind('<Button-1>',clica)
mainloop