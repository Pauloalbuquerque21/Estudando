quantidade = int(input("Digite o número de arquivos:"))

def transforme_arquivos(b):
    list_dict = list()
    dict_completo = dict()
    for vezes in range(0,b):
        a = input(f"Digite o nome do {vezes} arquivo:")
        dict_dados = dict()
        list_dados = list()
        dados = open(a,"r")
        for enumerado in dados:
            enumerado2 = enumerado.strip().split()
            list_dados.append(enumerado2)
            print(list_dados)
        for indice, dado_lista in enumerate(list_dados):
            if indice % 2 != 0:
                dict_dados[list_dados[indice-1]] =  dado_lista
        list_dict.append(dict_dados)
    for vezes2 in range(0,2):
        dict_completo.update(list_dict[vezes2])
    return dict_completo

resultado_postivo = transforme_arquivos(quantidade)

        