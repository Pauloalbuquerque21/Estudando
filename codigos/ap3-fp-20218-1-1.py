


def ordenaPorCampo(qualCampo,vetorDeProdutos):
    lista = vetorDeProdutos
    maior = lista[0]
    num = qualCampo - 1
    for quant in range(len(lista)):
        if lista[quant][num] < maior[quant][num]:
            maior = lista[quant][num]
        lista_ordem = list()
        lista_ordem.append(maior)
        lista.remove(maior)
