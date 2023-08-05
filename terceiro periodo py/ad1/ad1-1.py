pares = impares = quantpares = quantimpares = 0
quant = int(input('Quantos número o senhor digitará:'))
for c in range(1,quant+1):
    valores = int(input(f'Digite {c}° número inteiros:'))
    if valores % 2 == 0:
        pares = valores + pares
        quantpares += 1
    else:
        impares = valores + impares
        quantimpares += 1

print(f'Média dos pares:{pares/quantpares:.2f}\nMédia dos impares:{impares/quantimpares:.3f}')