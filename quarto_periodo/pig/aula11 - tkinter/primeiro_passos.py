from tkinter import *

def botao_clicado():
    a.config(text='Botao Clicar')
janela_principal = Tk()
#titulo
janela_principal.title('Estudando Tkinter')
#informação dentro do programa
a = Label(janela_principal, text = "Ola mundo")
a.pack(side="left")

#informação dentro do programa
b = Label(janela_principal, text = "Ola mundo")
b.pack(side="left")


botao = Button(janela_principal, text="Clique aqui", command = botao_clicado )
botao.pack()

janela_principal.mainloop()