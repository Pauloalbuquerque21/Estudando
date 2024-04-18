
from projeto1 import franc
def visual(a):
    quantidade = len(a)
    for linha in range(0,quantidade):
        for coluna in range(0,2):
            valor1 = a[linha][coluna]
            valor2 = a[linha][coluna]
        fracao{linha} = franc(valor1,valor2)
        fracao2 = fracao{linha}
        print(f'Fração {linha} : {fracao2}')






#Parte que pega as informações do arquivo e transforma em number:
resultado = open('arquivo.txt','r')
dados = resultado.readlines()
quantidade = len(dados)
numeros = list()
for dado in dados:
    lista_str = dado.strip().split()
    fracao = list()
    for str in lista_str:
        ints = int(str)
        fracao.append(ints)
    numeros.append(fracao)


resultado.close()

franc1 = franc(numeros[0][0],numeros[0][1])
print(franc1)

