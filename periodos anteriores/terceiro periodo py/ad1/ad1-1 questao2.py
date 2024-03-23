pares = quant = dado = impares = quantpares = quantimpares = maior = menor = 0
while True:
    quant += 1
    valores = input(f'Digite um número inteiros:')
    if len(valores) == 0:
        break
    else:
        dado = int(valores)
        if quant == 1:
            maior = dado
            menor = dado
        else:
            if dado > maior:
                maior = dado
            if dado < menor:
                menor = dado
        if dado % 2 == 0:
            pares = dado + pares
            quantpares += 1
        else:
            impares = dado + impares
            quantimpares += 1

print(f'Menor:{menor}\nMaior:{maior}')
if quantpares >= 1:
    print(f'Media dos pares:{pares/quantpares:.2f}')
else:
    print(f'Media dos pares:{pares:.2f}')
if quantimpares >= 1:
    print(f'Media dos pares:{impares/quantimpares:.3f}')
else:
    print(f'Media dos impares:{impares:.3f}')




