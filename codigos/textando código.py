def dobrar(numero):
    return numero * 2

numeros = [1, 2, 3, 4, 5]

resultado = map(dobrar, numeros)
resultado2 = list(resultado)
print(resultado2)

map