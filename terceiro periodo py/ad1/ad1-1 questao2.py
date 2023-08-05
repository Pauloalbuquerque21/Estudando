pares = impares = quantpares = quantimpares = maior = menor = 0
while True:
    quant += 1
    valores = int(input(f'Digite {c}° número inteiros:'))
    if c == 1:
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