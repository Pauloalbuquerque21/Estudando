from tkinter import *

def botao_clicado():
    a.config(text='Botao Clicar')
    b.config(text='Botão clicar+++')
janela_principal = Tk()
#titulo
janela_principal.title('Estudando Tkinter')
#informação dentro do programa
a = Label(janela_principal, text = "Ola mundo")
a.pack(side="left")

#Frame com alguns parametros
frame_superior = Frame(janela_principal, borderwidth=2, relief = "groove")
frame_superior.pack()

#informação dentro do programa b
b = Label(janela_principal, text = "Ola mundo")
b.pack(side="right")

#informação dentro do programa c
c = Label(janela_principal, text = "Ola mundo")
c.pack(side="top")

botao = Button(janela_principal, text="Clique aqui", command = botao_clicado )
botao.pack(side="top")

janela_principal.mainloop()