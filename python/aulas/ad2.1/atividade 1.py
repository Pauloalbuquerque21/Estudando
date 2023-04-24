lista = []
quant = n1 = 0
while True:
    n1 = input('Digite as coordenadas:')
    if quant == 0 and n1 == 0:
        print('Nenhum conto foi lido - A primeira linha lida está vazia')
    elif quant != 0 and n1 == 0:
        break
    lista.append(n1)
    quant = 1 + quant
print(f'Número de vezez: {quant}')
print(f'os elementos {lista}')
