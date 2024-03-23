lista_origem = [["xy3", "arroz", 120, 5.25],
["aa9", "feijão", 555, 2.99],
["ab8","banana", 100,3.99]]


def ordenaPorCampo(qualCampo,vetorDeProdutos):
    lista = vetorDeProdutos
    maior = lista[0]
    num = qualCampo - 1
    print(maior)
    for quant in range(len(lista)):
        if lista[quant][num] < maior[num]:
            maior = lista[quant]
    lista_ordem = list()
    lista_ordem.append(maior)
    lista.remove(maior)
    print(lista)
    if len(lista_ordem) != 3 :
        ordenaPorCampo(num+1,lista)
    return lista_ordem

lista_correta = ordenaPorCampo(4,lista_origem)
