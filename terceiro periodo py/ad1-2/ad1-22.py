permutacao = list()
dado = list()
test = 1
inf = quant = 0
def recebe(tamanho):
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
print(f'{dado}')

while True:
    if len(permutacao) == 0:
        permutacao.append(1)
        permutacao.append(dado[0])
        print(permutacao)
    else:
        print(permutacao)
        test = test + 1
        print(f'test: {test}')
        inf = permutacao[test-1]
        print(f'inf: {inf}')
        if dado[inf-1] in permutacao:
            test = 1 + quant
            quant = quant + 1
        else:
            permutacao.append(dado[inf-1])
    if len(permutacao) == len(dado):
        break
print(f'{dado} e \n{permutacao}')
