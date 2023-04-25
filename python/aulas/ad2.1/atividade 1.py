quant = 0
lista = []
while True:
    n1 = str(input('Digite os pontos:')).strip()
    if len(n1) == 0 and quant == 0:
        print('Nenhum ponto foi lido - Aprimeira linha lida estava vazia')
    elif len(n1) == 0 and quant !=0:
        break
    lista.append(n1)
    quant = 1 + quant
print('Listagem dos Pontos Lidos:')
for c in range(0,len(lista)):
    print(f'({lista[c]})\n')
print('Fim da listagem')
print(f'{lista}')