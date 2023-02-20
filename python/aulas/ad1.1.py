entrada = 0
while True:
    try:
        entrada = int(input('Digite um número:'))
        letras = str(entrada)
        if  len(letras) == 0:
            break
        print('Linha vazia lida')
    except ValueError:
        print('Linha vazia')



        