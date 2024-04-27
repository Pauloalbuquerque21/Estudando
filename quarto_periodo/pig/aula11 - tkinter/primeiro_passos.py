from tkinter import *

def botao_clicado():
    a.config(text='Botao Clicar esquerdo')
    b.config(text='Botão clicar direito')
    c.config(text='botão clicar top', font='Arial 24 bold', border = 5, background = 'yellow')

janela_principal = Tk()

#titulo
janela_principal.title('Estudando Tkinter')

#Frame com alguns parametros
frame_superior = Frame(janela_principal, borderwidth=2, relief = "groove", background = 'white',width=200, height=200)
frame_superior.pack(expand=True)



#informação dentro do programa
a = Label(frame_superior, text = "Ola mundo esquerda")
a.pack(side="left",padx=10, pady=10)

#informação dentro do programa b
b = Label(frame_superior, text = "Ola mundo direita", background='red')
b.pack(side="right",padx=10, pady=10)

#informação dentro do programa c
c = Label(frame_superior, text = "Ola mundo top")
c.pack(side="top",padx=10, pady=10)

botao = Button(janela_principal, text="Clique aqui", command = botao_clicado )
botao.pack(side="top")

janela_principal.mainloop()