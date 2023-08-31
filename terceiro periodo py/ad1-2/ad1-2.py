dado = list()
quant = 0
tamanho = int (input('Qual o tamanho da permutação:'))
while True:
    inf = int(input(f'Digite o {quant+1}° valor:'))
    if inf in dado:
        print('Valor digitádo já existe na permutação, favor tente novamente!')
    else:
        dado.append(inf)
        quant+=1
    if quant == tamanho:
         break
print(dado)