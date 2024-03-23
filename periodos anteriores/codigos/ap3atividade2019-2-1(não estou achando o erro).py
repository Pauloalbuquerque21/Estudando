arquivo = input("Digite o nome do arquivo:")
menor_menor2 = ()
def transforme_list(arquivo):
    lista_completa = list()
    arquivo_texto = open(arquivo,"r")
    for listas in arquivo_texto.readlines():
        lista1 = listas.strip().split()
        lista_completa.append(lista1)
    return  lista_completa
transforme = transforme_list(arquivo)
print(transforme)

def menor_maior(listas):
    elemento_0=listas[0]
    elemento_0_0 = int(elemento_0[0])
    elemento_0_1 = int(elemento_0[1])
    menor = maior = (((elemento_0_0**(1/2))+(elemento_0_1**(1/2))**(1/2)))
    for listas_inter in listas:
        for elementos in listas_inter:
            elementos_0_0 = int(elementos[0])
            elementos_0_1=int(elementos[1])
            resultado = (((elementos_0_0)**(1/2)+(elementos_0_1)**(1/2)))
            if resultado >= maior:
                lista_maior = elementos
                maior = resultado
            if resultado <= menor:
                lista_menor = elementos
                menor = resultado 
    return lista_menor,lista_maior
menor_menor2 = menor_maior(transforme)
print(menor_menor2)

def distancia(maior,menor):
    lista_maior = list()
    lista_menor = list()
    for int1 in maior:
        numero = float(int1)
        lista_maior.append(numero)
    for int2 in menor:
        numero = float(int2)
        lista_menor.append(numero)
    cateto1 = lista_maior[0] - lista_menor[0]
    cateto2 = lista_maior[1] - lista_menor[1]
    resul_catetos = ((cateto1**(1/2))+(cateto2**(1/2)))**(1/2)
    return resul_catetos,lista_maior,lista_menor
distancia2=distancia(menor_menor2)
print(distancia2)


def mostrar(menor_list,maior_list,distancia):
    maior_tupla = (maior_list[0],maior_list[1])
    menor_tupla = (menor_list[0],menor_list[1])
    print(f'Pontos mas distantes:{maior_tupla} e {menor_tupla}')
    print(f'Distância entre eles (com precisão de uma casa decimal:{distancia})')




lista_ponto = transforme_list(arquivo)
diferenca = menor_maior(lista_ponto)
distanca_pontos = distancia(diferenca[1],diferenca[0])
mostrar(distanca_pontos[2],distanca_pontos[1],distanca_pontos[0])


