from tkinter import *
def clica (e):
    txt = f"Mouse clicado em {e.y} e {e.x}"
    r.configure(text=txt)
janela_principal = Tk()
r = Label()
r.pack(expand=True, fill= "both")

janela_principal.geometry("200x200")
janela_principal.bind("<Button-1>", clica)
janela_principal.mainloop()