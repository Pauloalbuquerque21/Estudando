permutacao = list()
dado = list()
test = 1
inf = quant = 0
def recebe(tamanho): # subprogama que cria a permutação com o números digitado
    quant = 0
    while True:
        inf = int(input(f'Digite o {quant + 1}° valor:'))
        if inf in dado:
            print('Valor digitádo já existe na permutação, favor tente novamente!')
        elif inf > tamanho:
            print('número muito alto')
        elif inf == 0:
            print('Favor não digite zero')
        else:
            dado.append(inf)
            quant += 1
        if quant == tamanho:
            break
    return dado
recebe(int(input('Digite o tamanho da permutação:')))
print(f'Números digitados :{dado}')

while True:
    if len(permutacao) == 0:
        permutacao.append(1)
        permutacao.append(dado[0])
    elif test == len(permutacao):
        if dado[test] in permutacao:
            if (test + 1) == len(dado):
                break
            else:
                test = test + 1
        permutacao.append(dado[test])
    else:
        test = test + 1
        inf = permutacao[test-1]
        if dado[inf-1] in permutacao:
            test = 2 + quant
            quant = quant + 1
        else:
            permutacao.append(dado[inf-1])
    if len(permutacao) == len(dado):
        break
print(f'Permutação:{permutacao}')
