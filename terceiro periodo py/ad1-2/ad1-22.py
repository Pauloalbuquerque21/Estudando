permutacao = dado = list()
test = 0
def recebe(tamanho):
    quant = 0
    while True:
        inf = int(input(f'Digite o {quant + 1}° valor:'))
        if inf in dado:
            print('Valor digitádo já existe na permutação, favor tente novamente!')
        else:
            dado.append(inf)
            quant += 1
        if quant == tamanho:
            break
    return dado


recebe(int(input('Digite o valor da permutação')))
print(dado)
while True:
    if len(permutacao) == 0:
        permutacao.append(dado[0])
    else:
        test = len(permutacao)
        permutacao.append(dado[test])
    if len(permutacao) == tamanho:
        break
print(f'{dado} e \n{permutacao}')