lista_10 = list()
lista_nao = list()
lista_crescente = list()
lista_decrescente = list()
elementos = 0 
while True:
    dados = int(input('Digite o número de elementos:'))
    if dados > 0 :
        break
while elementos != dados:
    dados2 = int(input(f'Digite o elemento {elementos+1}:'))
    if dados2 >= 0:
        elementos += 1
        if dados2 % 10 == 0:
            lista_10.append(dados2)
        else:
            lista_nao.append(dados2)
    else:
        print('Digite um número iunteiro não negativo')

print(f'{lista_10}\n{lista_nao}')

def crescente(lista):
    lista1 = lista
    menor = lista1[0]
    for dado in lista1:
        if menor >=dado:
            menor = dado
    lista_crescente.append(menor)
    print(f"LIsta: {lista_crescente}")
    lista1.remove(menor)
    if len(lista1)!=0:
        crescente(lista1)

def decrescente(lista):
    lista1 = lista
    maior = lista[0]
    for dado in lista1:
        if maior <= dado:
            maior = dado
    lista_decrescente.append(maior)
    lista1.remove(maior)
    if len(lista1) != 0:
        decrescente(lista1)
crescente(lista_10)
decrescente(lista_nao)
for c in lista_crescente:
    print(f"{c}\n")
for d in lista_decrescente:
    print(f"{d}\n")

