quantidade_linha = 0
dados_matriz = list()
while True:
    information_matriz.clean()
    quantidade_linha += 1
    information_matriz = input(f'Linhas {quantidade_linha}:')
    if information_matriz == 0:
        break
    else:
        dados_divididos = information_matriz.split()
        dados_matriz.append(dados_divididos)
