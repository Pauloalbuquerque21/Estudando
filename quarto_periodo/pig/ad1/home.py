from classes import suduko
print('-+'*20)
print(f'SUDOKO'.center(20))
print('-+'*20)
print('Regra:\nvocê só tem direito de 3 erros.\nFavor digitar as linhas e colunas de 0 até 8\nDigitar as dificuldade sem acentuação')


dificuldade = suduko(str(input('Digite a Dificuldade, Sem acentuação[Facil,Medio e Dificil]:').strip().lower()))
print(f'Dificuldade selecionada:{dificuldade}')
lista=dificuldade.suduku_pricipal()
dificul = dificuldade.detect()
dificuldade.suduko_usuario(lista,dificul)



