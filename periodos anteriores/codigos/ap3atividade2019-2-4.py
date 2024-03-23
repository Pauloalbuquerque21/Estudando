arquivo = input('Qual o nome do arquivo:')
def list_informe(arquivo):
    dados_list = list()
    infor_list = list
    dados = open(arquivo,'r')
    for informacao in dados.readlines():
        infor_list = informacao.strip().split()
        print(infor_list)
        for informacao2 in infor_list:
            dados_list.append(informacao2)
    dados.close
    return dados_list

resultado = list_informe(arquivo)
print(resultado)
dados_float = list()
dados_int = list()
for result in resultado:
    dados2 = float(result)
    dados3 = dados2 // 1
    dados_int.append(dados3)
    dados_float.append(dados2)
print(dados_float)
print(dados_int)


def listas(inteiro,float):
    quantidade = len(inteiro)
    list_inteiros = list()
    list_float = list()
    for elemento in range(0,quantidade):
        if float[elemento] - inteiro[elemento] == 0:
            dado = int(inteiro[elemento])
            list_inteiros.append(dado)
        else:
            list_float.append(float[elemento])
    
    return list_inteiros,list_float

resultado = listas(dados_int,dados_float)
print(resultado)

def escrita(inteiro, float):
    informa_int = open("saida1.txt",'w')
    informa_float = open("saida2.txt",'w')
    for elementos in inteiro:
        informa_int.write(f'{elementos}\n')
    for elementos2 in float:
        informa_float.write(f'{elementos2}\n')

resultado_final = (escrita(resultado[0],resultado[1]))