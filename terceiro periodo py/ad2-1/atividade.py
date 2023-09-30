quantidade_linha = information_matriz = n1 = 0
dados_matriz = list()
dados_das_matrizes = list()
for c in range(0,2):
    print(c)

    quantidade_linha = 0
    while True:
        quantidade_linha += 1
        information_matriz = input(f'Matriz {c} Linhas {quantidade_linha}:')
        dados_divididos = information_matriz.split()
        print(dados_divididos)
        print(quantidade_linha)
        if len(information_matriz) == 0:
            dados_das_matrizes.append(quantidade_linha-1)
            break
        else:
            #if quantidade_linha > 1 and c == 0:
            #    if len(dados_matriz[quantidade_linha-2]) != len(dados_divididos):
            #        quantidade_linha -= 1
            #        print('Fazor digitar o mesmo número de colunas que matriz anterior ')
            #    else:
            #        dados_matriz.append(dados_divididos)
            #elif c == 1 and quantidade_linha > 1:
            #    n1 = len(dados_matriz)
                #if len(dados_matriz[n1]-1) != len(dados_divididos):
                #    quantidade_linha -= 1
                #    print('Fazor digitar o mesmo número de colunas que matriz anterior ')
                #else:
                #    dados_matriz.append(dados_divididos)
            #else:
            transform_num = int(dados_divididos)
            dados_matriz.append(transform_num)
print(dados_matriz)
print(dados_das_matrizes)

def leituraDeMatriz(dado):
    tamanho_matriz_a = dados_das_matrizes[0]
    tamanho_matriz_b = dados_das_matrizes[1]
    matriz_A = matriz_B = list()
    if dado in 'aA':
        for c in range(0,tamanho_matriz_a):
            for c2 in range(0,len(dados_matriz[0])):
                numb = int(dados_matriz[c][c2])
                matriz_A.append(numb)
        for c in range(0, tamanho_matriz_a):
            for c2 in range(0,):
    return matriz_A

valoresA = leituraDeMatriz('a')
print(valoresA)