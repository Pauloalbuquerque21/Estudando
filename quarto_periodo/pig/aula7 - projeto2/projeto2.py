
resultado = open('arquivo.txt','r')
dados = resultado.readlines()
quantidade = len(dados)
print(dados)
print(quantidade)
numeros = list()
fracao = list()
for c1 in dados:
    strings = c1.strip().split()
    for str in strings:
        
        ints = int(str)
        fracao.append(ints)
    numeros.append(fracao)

print(numeros)