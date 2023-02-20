while True:
    try:
        entrada = int(input('Digite um número:'))
        if  len(str(entrada)) == 0:
            break
        print('Linha vazia lida')
    except ValueError:
        print('Linha vazia')



        