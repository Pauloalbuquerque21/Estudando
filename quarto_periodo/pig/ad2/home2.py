from classes3 import suduko
from tkinter import *
print('-+'*20)
print(f'SUDOKO'.center(20))
print('-+'*20)
print('Regra:\nvocê só tem direito de 3 erros.\nFavor digitar as linhas e colunas de 0 até 8\nDigitar as dificuldade sem acentuação')


#dificuldade = suduko(str(input('Digite a Dificuldade, Sem acentuação[Facil,Medio e Dificil]:').strip().lower()))
#print(f'Dificuldade selecionada:{dificuldade}')
#lista=dificuldade.suduku_pricipal()
#dificul = dificuldade.detect()
#dificuldade.suduko_usuario(lista,dificul)


def dificuldade():
    global dificuldade2, dificuldade1, botao_dificuldade
    #apagar o label infor
    infor.pack_forget()
    botao.pack_forget()
    #dificuldade
    dificuldade1 = Label(janela_principal, text='Digite a dificuldade')
    dificuldade1.pack(side='top')

    #Parte onde escrevemos.
    dificuldade2 = Entry(janela_principal,width=30)
    dificuldade2.pack(side='top')

    botao_dificuldade = Button(janela_principal, text="Enter", command = botao_clicado )
    botao_dificuldade.pack(side="top")

def botao_clicado():
    global a
    #Atribuir o valor do Entry no texto_dificuldade
    texto_dificuldade = dificuldade2.get()
    
    dificuldade = suduko(texto_dificuldade)

    #apagar o dificuldade1,dificuldade2 e voão
    dificuldade1.pack_forget()
    dificuldade2.pack_forget()
    botao_dificuldade.pack_forget()

    #Tela do jogo
    a = Label(janela_principal,background='white', width=40, height=20)
    a.pack(side='top')

    lista=dificuldade.suduku_pricipal()
    dificul = dificuldade.detect()
    #print(f'{lista},{dificul}')
    #dificuldade.suduko_usuario(lista,dificul)
    
    # Criando uma string para representar as informações do jogo
    info_jogo = ""
    for linha in lista:
        info_jogo += " ".join(linha) + "\n"
    
    # Adicionando as informações do jogo à string
    info_jogo += "\nVertical: " + " ".join(map(str, range(9)))
    
    # Exibindo as informações do jogo no Label "a"
    a.config(text=info_jogo)

janela_principal = Tk()

#TITULO
janela_principal.title('SUDUKO')
janela_principal.geometry("400x500")


#labels
infor = Label(janela_principal, text='Regra:\nvocê só tem direito de 3 erros.\nFavor digitar as linhas e colunas de 0 até 8\nDigitar as dificuldade sem acentuação',background='white')
infor.pack(side='top')

botao = Button(janela_principal, text="Iniciar o jogo", command = dificuldade )
botao.pack(side="bottom")

janela_principal.mainloop()

