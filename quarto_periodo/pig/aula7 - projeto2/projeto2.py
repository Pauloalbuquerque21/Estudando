import os
print(os.getcwd())
resultado = open('arquivo.txt','r')
dados = resultado.readlines()
quantidade = len(dados)
print(dados)
for c1 in range(0,quantidade):
    for c2 in dados[c1]:
        print(c2)
resultado.close()