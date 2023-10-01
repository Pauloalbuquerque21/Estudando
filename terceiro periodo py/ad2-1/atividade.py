quantidade_linha = information_matriz = 0
dados_das_matrizes =  dados_divididos_num = list()
dados_matriz = list()
for c in range(0,2):
    print(c)
    quantidade_linha = 0
    while True:
        quantidade_linha += 1
        information_matriz = input(f'Matriz {c} Linhas {quantidade_linha}:')
        dados_divididos_str = information_matriz.split()
        print(dados_divididos_str)
        dados_divididos_num = list()
        for c in range(0,len(dados_divididos_str)):
            dados_divididos_num.append(int(dados_divididos_str[c]))
        print(dados_divididos_num)
        print(quantidade_linha)
        print(dados_das_matrizes)
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
            dados_matriz.append(dados_divididos_num)
print(f'Dados_matrizes:{dados_matriz}')
print(f'Dados_das_matrizes:{dados_das_matrizes}')

def leituraDeMatriz(dado):
    tamanho_matriz_a = dados_das_matrizes[0]
    tamanho_matriz_b = dados_das_matrizes[1]
    matriz_A = matriz_B = list()
    if dado in 'aA':
        for c in range(0,tamanho_matriz_a):
            matriz_A.append(dados_matriz[c])
        return matriz_A
    if dado in 'bB':
        for c in range(tamanho_matriz_a,len(dados_matriz)):
            matriz_A.append(dados_matriz[c])
        return matriz_B
valoresB = leituraDeMatriz('b')
valoresA = leituraDeMatriz('a')

def mostraMatriz(informe_str,matriz_em_lista):
    print(f'{a}:')
    for c in range(0,len(b)):
        print(b[c])
        print()
mostraMatriz('Matriz B',valoresB)

def somaMatrizes(matriz_1,matriz_2):
    matriz_result_soma = list()
    test = list()
    if len(a) == len(b) and len(a[0]) == len(b[0]):

        for c1 in range(0,len(a)):
            test = list()
            for c2 in range(0,len(a[0])):
                test.append(0)
            matriz_result_soma.append(test)
        for c1 in range(0,len(a)):
            for c2 in range(0,len(a[0])):
                soma = a[c1][c2] + b[c1][c2]
                matriz_result_soma[c1][c2]=soma
        result_soma = matriz_result_soma
    else:
        result_soma = 'Inexistente!!!'
    return result_soma

def multiplicaMatrizes(matriz_1,matriz_2):
    mult = 0
    matriz_result_mult = list()
    if len(a[0]) == len(b):
        for linhas in range(0,len(a)):
            test = list()
            for colunas in range(0,len(b[0])):
                test.append(0)
            matriz_result_mult.append(test)
        for c in range(0,len(a)):
            for c3 in range(0,len(b[0])):
                result = 0
                for c2 in range(0,len(a[0])):
                    mult = a[c][c2] * b[c2][c3]
                    result = mult + result
                matriz_result_mult[c][c3] = result
        result_mult = matriz_result_mult
    else:
        result_mult = 'Inexistente!!'
    return result_mult




valoresSoma = somaMatrizes(valoresB,valoresA)
valoresMult = multiplicaMatrizes(valoresA,valoresB)
print('Resultado da Soma:')
print(valoresSoma)
print('Resultado da multiplicação:')
print(valoresMult)