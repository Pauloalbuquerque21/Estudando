import tkinter as tk

def mostrar_tecla(event):
    print("Tecla pressionada:", event.char)
    txt = f"Tecla pressionada: {event.char}"
    r.config(text=txt)

janela_principal = tk.Tk()


janela_principal.geometry("200x200")

#janela_principal.geometry("200x200")

janela_principal.bind("<Key>", mostrar_tecla)

#Label
r = tk.Label(janela_principal,)
r.pack(side='bottom')




janela_principal.mainloop()