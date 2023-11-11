dados_list = []
dados_list_dividido = []
words_dict = dict()
conjunto = set()
conjunto_repitidos = set()
arquivo_texto = input('Digite o nome do arquivo:')
dados = open(arquivo_texto,'r')
for lista in dados:
    palavras = lista.strip().split()
    for pal in palavras:
        if words_dict.get(pal) == None:
            words_dict[pal] = 1
        else:
            words_dict[pal] += 1
dados.close()
def mostrar(a):
    if a == {}:
        print("O dicionário ficou vazio!")
    else:
        print("Dicionário ordenado pelas palavras:")
        for chave, conteudo in a.items():
            print(f"{chave} ocorreu {conteudo} ",end = "")
            if conteudo > 1:
                print("vezes.")
            else:
                print('Vez.')
def remove(b):
    excluirChaves = list()
    for chave, valor in b.items():
        if len(chave) % 2 == 0:
            excluirChaves.append(chave)
    for pares in excluirChaves:
        b.pop(pares)
    return b

dicionario_impares = remove(words_dict)
print(dicionario_impares)
mostrar(dicionario_impares)