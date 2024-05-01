from tkinter import *

def clique(event):
    print('Clique do mouse detectado nas coordenadas:', event.x, event.y)
    click.config(text=f'Clique do mouse detectado nas coordenadas:{event.x} e {event.y}')
janela_principal = Tk()

#Criando um rótulo
rotulo = Label(janela_principal, text='Clique aqui!')
rotulo.pack()

#Definindo um tamanho
janela_principal.geometry("500x200")

click = Label(janela_principal, text='Não clicou ainda')
click.pack(side='bottom')
#Associando o evento de clique do mouse ao rótulo
rotulo.bind('<Button-1>', clique)

janela_principal.mainloop()