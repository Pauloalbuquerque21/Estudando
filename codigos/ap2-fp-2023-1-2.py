frase = input('Digite a frase:')
frase_dividida = frase.split()
print('A frase sem espaço é ',end='')
for palavras in frase_dividida:
    print(f'{palavras}',end='')
print('\n')

print(frase_dividida)
def cosoante_vogais(lista):
    cosoantes = 0 
    vogais = 0 
    for palavra in lista:
        for letra in palavra.upper():
            if letra in 'ÁÀÉÍÔU' or 'AEIOU':
                vogais +=1
            else:
                cosoantes += 1
    return vogais,cosoantes

resultado = cosoante_vogais(frase_dividida)
print(resultado)
