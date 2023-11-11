dados_list = []
conjunto = set()
conjunto_repitidos = set()
arquivo_texto = input('Digite o nome do arquivo:')
dados = open(arquivo_texto,'r')
dados_list = [dados2.strip() for dados2 in dados.readline()]
conjunto = dados_list
dados.close()
print(conjunto)
if len(conjunto) != 0:
    for dados3 in conjunto:
        if conjunto.count(dados3) != 1:
            conjunto_repitidos.add(dados3)
    if len(conjunto_repitidos) == 0:
        print('Nenhuma palavra com caracteres repitidos foi encontrada!!!')
    else:
        print(f'Palavras com caracteres repetidos = {conjunto_repitidos}')
else:
    print('Nenhuma palavra com caracteres repitidos foi encontrada!!!')
