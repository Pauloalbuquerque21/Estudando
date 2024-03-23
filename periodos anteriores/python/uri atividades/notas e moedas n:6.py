valor=float(input('Digite um valor com duas casas decimais:'))
quanti100 = 0
quanti50 = 0
quanti20 = 0
quanti10 = 0
quanti5 = 0
quanti2 = 0
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
        valor = valor -2
        quanti2 = quanti2 + 1 
    else:
        print('Fim')
        print(valor)
        break

print(f'NOTAS:\n{quanti100} notas(s) de R$ 100,00\n{} notas(s) de R$ 50,00\n{} notas(s) de 20,00\n{} notas(s) de 10,00\n{} nota(s) de 5,00\n{} nota(s) 2,00')

    