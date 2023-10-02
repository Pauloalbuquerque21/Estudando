quantidade_linha = information_matriz = 0
dados_das_matrizes =  dados_divididos_num = list()
dados_matriz = list()
for quant_matrizes in range(0,2):
    quantidade_linha = 0
    print()
    while True:
        quantidade_linha += 1
        information_matriz = input(f'Matriz {quant_matrizes+1} Linhas {quantidade_linha}:')
        dados_divididos_str = information_matriz.split()
        dados_divididos_num = list()
        for c in range(0,len(dados_divididos_str)):
            dados_divididos_num.append(int(dados_divididos_str[c]))
        if len(information_matriz) == 0:
            dados_das_matrizes.append(quantidade_linha-1)
            break
        else:
            #if quantidade_linha > 1:
            #    if len(dados_matriz[quantidade_linha-2]) != len(dados_divididos):
            #        quantidade_linha -= 1
            #        print('Fazor digitar o mesmo número de colunas que matriz anterior ')
            #    else:
            #        dados_matriz.append(dados_divididos)
            #elif c == 1 and quantidade_linha > 1:
            #    n1 = len(dados_matriz)
            #    if len(dados_matriz[n1]-1) != len(dados_divididos):
                #    quantidade_linha -= 1
                #    print('Fazor digitar o mesmo número de colunas que matriz anterior ')
                #else:
                #    dados_matriz.append(dados_divididos)
            #else:
            dados_matriz.append(dados_divididos_num)