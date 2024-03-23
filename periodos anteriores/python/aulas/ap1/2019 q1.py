quant = 0
valor = 0
v0=v1=v2=v3=v4=v5=v6=v7=v8=v9=0

while True:
    candidato = str(input('Qual é seu candidato:'))
    valor = len(candidato)
    quant = quant + 1 
    if  valor == 0:
        if quant == 1:
            print('Nenhum voto ocorreu!!')
            break
        if quant >= 1:
            break
    else:
        if candidato == '0':
            v0=v0+1
        if candidato =='1':
            v1=v1+1
        if candidato == '2':
            v2=v2+1
        if candidato == '3':
            v3=v3+1
        if candidato == '4':
            v4=v4+1
        if candidato == '5':
            v5=v5+1
        if candidato == '6':
            v6=v6+1
        if candidato == '7':
            v7=v7+1
        if candidato == '8':
            v8=v8+1
        if candidato == '9':
            v9=v9+1
if candidato == '0' and v0 != 0:
    print(f'Candidato 0 obteve {v0}') 
if candidato == '1' and v0 != 0:
    print(f'Candidato 1 obteve {v1}')
if candidato == '2' and v0 != 0:
    print(f'Candidato 2 obteve {v2}')
if candidato == '3' and v0 != 0:
    print(f'Candidato 3 obteve {v3}')
if candidato == '4' and v0 != 0:
    print(f'Candidato 4 obteve {v4}')
if candidato == '5' and v0 != 0:
    print(f'Candidato 5 obteve {v5}')
if candidato == '6' and v0 != 0:
    print(f'Candidato 6 obteve {v6}')
if candidato == '7' and v0 != 0:
    print(f'Candidato 7 obteve {v7}')
if candidato == '8' and v0 != 0:
    print(f'Candidato 8 obteve {v8}')
if candidato == '9' and v0 != 0:
    print(f'Candidato 9 obteve {v9}')
    

#print(f'Candidato 0 obteve {v0}\nCandidato 1 obteve {v1}\nCandidato 2 obteve {v2}\nCandidato 3 obteve {v3}\nCandidato 4 obteve {v4}\nCandidato 5 obteve {v5}\nCandidato 6 obteve {v7}\nCandidato 7 obteve {v7}\nCandidato 8 obteve {v8}\nCandidato 9 obteve {v9}\n')

        
