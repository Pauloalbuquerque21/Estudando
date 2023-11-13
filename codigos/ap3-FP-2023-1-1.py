

lista_informacao = list()

for quantidade in range(0,3):
    informacao = int(input('Digite o números:'))
    lista_informacao.append(informacao)

def dados_lista(i,j,k):
    lista_elementos = [j,k]
    inf = 1
    while len(lista_elementos) < i:
        dado_novo = lista_elementos[inf-1] + lista_elementos[inf]
        lista_elementos.append(dado_novo)
        inf += 1
    print(f'Os {i} elementos da sequência são {lista_elementos}')
    return lista_elementos

def pares(elementos):
    lista_pares = list()
    for dados in elementos:
        if dados % 2 == 0:
            lista_pares.append(dados)
    if len(lista_pares) == 0:
        print('Não há elementos pares na sequência até a posição 2.')
    else:
        print(f'Os elementos pares da sequência são {lista_pares}.',end='')
    return lista_pares

def perfeito(dados):
    lista_perfeitos = list()
    for dado in dados:
        etapa1 = (dado**(1/2))
        etapa2 = int(etapa1)
        etapa3 = etapa1 - etapa2
        if etapa3 ==0:
            lista_perfeitos.append(dado)
    if len(lista_perfeitos) == 0:
        print('Não há elemento par quadrado perfeito.')
    else:
        print(f'\nDentre esses, os que são quadrados perfeitos são{lista_perfeitos}')


elementos = dados_lista(lista_informacao[0],lista_informacao[1],lista_informacao[2])
pares_elementos = pares(elementos)
perfeito(pares_elementos)


