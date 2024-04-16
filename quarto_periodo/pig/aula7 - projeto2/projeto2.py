
resultado = open('arquivo.txt','r')
dados = resultado.readlines()
quantidade = len(dados)
print(dados)
print(quantidade)
numeros = list()
for dado in dados:
    lista_str = dado.strip().split()
    print(lista_str)
    fracao = list()
    for str in lista_str:
        ints = int(str)
        fracao.append(ints)
    numeros.append(fracao)

print(numeros)