pares = impares = maior = menor = quantpares = quantimpares = 0
quant = int(input('Quantos números o senhor digitará:'))
for c in range(1,quant+1):
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
print(f'{quantpares} e {quantimpares}')
print(f'Menor:{menor}\nMaior:{maior}')
if quantpares >= 1:
    print(f'Media dos pares:{pares/quantpares:.2f}')
else:
    print(f'Media dos pares:{pares:.2f}')
if quantimpares >= 1:
    print(f'Media dos pares:{impares/quantimpares:.3f}')
else:
    print(f'Media dos impares:{impares:.3f}')
