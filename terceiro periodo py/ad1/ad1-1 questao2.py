pares = quant = impares = quantpares = quantimpares = maior = menor = 0
while True:
    quant += 1
    valores = input(f'Digite {quant}° número inteiros:')
    if len(valores) == 0:
        break
    if quant == 1:
        maior = valores
        menor = valores
    else:
        if valores > maior:
            maior = valores
        if valores < menor:
            menor = valores
    if valores % 2 == 0:
        pares = valores + pares
        quantpares += 1
    else:
        impares = valores + impares
        quantimpares += 1

print(f'Menor:{menor}\nMaior{maior}\nMédia dos pares:{pares/quantpares:.2f}\nMédia dos impares:{impares/quantimpares:.3f}')