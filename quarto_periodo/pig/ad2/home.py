from tkinter import *
from classes2 import suduko

"""
lista = ['1234\n','3456']
lista2 = []
def botao_clicado():
#visualisar o prigrama 

    listas=[[],[],[],[],[],[],[],[],[]]
    for c in range(0,9):
        for c2 in range(0,9):
            listas[c].append(".")
        
    horinzontal = ['0','1','2','3','4','5','6','7','8']
    vertical = [0,1,2,3,4,5,6,7,8]
    horizontal_visual = ' '.join(horinzontal)
    print(f'   {horizontal_visual}')
    print('   ------------------')
    lista2.append(horizontal_visual)
    for c in range(0,9):
        listas[c] = '  '.join(listas[c])
    
    a.configure(text=f'   {horizontal_visual}\n   -------------------\n{vertical[0]}| {listas[0]}\n{vertical[1]}| {listas[1]}')
"""
def botao_clicado():
    dificuldade = suduko(str(input('Digite a Dificuldade, Sem acentuação[Facil,Medio e Dificil]:').strip().lower()))
    print(f'Dificuldade selecionada:{dificuldade}')
    lista=dificuldade.suduku_pricipal()
    dificul = dificuldade.detect()
    p1=dificuldade.suduko_usuario(lista,dificul)
    a.configure(text = p1.resultado)

janela_principal = Tk()
#TITULO
janela_principal.title('SUDUKO')
janela_principal.geometry("400x500")

a = Label(janela_principal,background='red', width=40, height=20 )
a.pack(side='top')

botao = Button(janela_principal, text="Clique aqui", command = botao_clicado )
botao.pack(side="bottom")

janela_principal.mainloop()
