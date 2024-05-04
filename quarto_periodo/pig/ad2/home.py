from tkinter import *
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
    print('  ------------------')
    lista2.append(horizontal_visual)
    for c in range(0,9):
        lista_visual = ' '.join(listas[c])
    
    a.configure(text=f'{vertical[0]}| {lista_visual[0]}')
    a.configure(text=f'{vertical[1]}| {lista_visual[1]}')
    a.configure(text=f'{vertical[2]}| {lista_visual[2]}')
    a.configure(text=f'{vertical[3]}| {lista_visual[3]}')
    a.configure(text=f'{vertical[4]}| {lista_visual[4]}')
    a.configure(text=f'{vertical[5]}| {lista_visual[5]}')
    a.configure(text=f'{vertical[6]}| {lista_visual[6]}')
    a.configure(text=f'{vertical[7]}| {lista_visual[7]}')
    a.configure(text=f'{vertical[8]}| {lista_visual[8]}')
    


janela_principal = Tk()
#TITULO
janela_principal.title('SUDUKO')
janela_principal.geometry("400x500")

a = Label(janela_principal,background='red', width=40, height=20 )
a.pack(side='top')

botao = Button(janela_principal, text="Clique aqui", command = botao_clicado )
botao.pack(side="bottom")

janela_principal.mainloop()

