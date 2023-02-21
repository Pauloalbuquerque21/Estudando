entrada = 0
escola = 0
while True:
    try:
        entrada = int(input('Digite um número:'))
        letras = str(entrada)
        if  len(letras) == 0:
            print('Linha vazia lida')
    except ValueError:
        print('Linha vazia2')
        if escola == 0:
            break



        