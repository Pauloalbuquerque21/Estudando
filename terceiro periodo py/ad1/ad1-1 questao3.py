numeros = maior = menor = impares = pares = quantpares = quantimpares = 0
valores = input('Digite os números:')
#palavra = valores.split()
#quanti = valores.strip()
test = valores.replace(' ','')
print(test)
print(len(test))
for c in range(0,len(test)):
    numeros = int(test[c])
    if len(test) == 1:
        maior = numeros
        menor = numeros
    else:
        if numeros > maior:
            maior = numeros
        if numeros < menor:
            menor = numeros
    if valores % 2 == 0:
        pares = numeros + pares
        quantpares += 1
    else:
        impares = numeros + impares
        quantimpares += 1