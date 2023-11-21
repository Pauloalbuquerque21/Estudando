conjunto = set()
maior_dic = dict()
numero = 0
while numero >= 0:
    numero = int(input('Digite um número'))
    if numero >= 0:
        conjunto.add(numero)
if len(conjunto) == 1:
    print(f'Apenas um valor foi lido:{conjunto[0]}')
elif len(conjunto) > 1:
    maior = conjunto[0]
    for numeros in conjunto:
        if maior < numeros:
            maior = numeros
    maior_dic.setdefault('primeiro',maior)
    conjunto.discard(maior)
    segunda = conjunto[0]
    for numero2 in conjunto:
        if segunda < numeros