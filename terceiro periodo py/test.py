dado = inf1 = inf2 = quant =resultx = resulty = 0
x1 = y1 = dado2 = list()
while True:
    dado = input('Digite os números separados com espaço:')
    dado2 =dado.split()
    inf1 = float(dado2[0])
    print(f'{inf1}')
    inf2 = float(dado2[1])
    print(f'{inf2}')
    if len(dado2) != 2 :
        print('Digite segundo as orientações.')
        dado2.clear
    elif inf1 == 0 and inf2 == 0:
        if quant ==0:
            print('Não existem pontos!')
        else:
            break
    else:
        x1.append(inf1)
        y1.append(inf2)
        quant = quant + 1
        dado2.clear()

for c in range(0,len(x1)):
    resultx = resultx + x1[c]
    resulty = resulty + y1[c]
print(f'{x1} {y1}')
print(f'{resultx/len(x1)} e {resulty/len(y1)}')