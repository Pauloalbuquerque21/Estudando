valor=float(input('Digite um valor com duas casas decimais:'))
quanti100 = 0
quanti50 = 0
quanti20 = 0
while True:
    if valor >= 100:
        valor = valor - 100
        quanti100 = quanti100 + 1
    elif valor >= 50:
        valor = valor - 50
        quanti50 = quanti50 + 1
    elif valor >= 20:
        valor = valor - 20
        quanti20 = quanti20 + 1
    elif valor >= 10:
        valor = valor - 10
        quanti10 = quanti10 + 1
    elif valor >= 5:
        valor = valor - 5
        quanti5 = quanti5 + 1
    elif valor >= 2:
        
    else:
        print('Fim')
        print(valor)
        break

print(quanti100,quanti50,)

    