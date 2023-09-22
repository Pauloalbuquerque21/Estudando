with open('arquivo1.txt','w') as arquivo_1:
    arquivo_1.write('784 Juca de Oliveira\n555 Anna Joaquina ferreira\n123 Edson Arantes\n10 Maria Auxliadora das Neves\n5 Murilo das Couves')
with open('arquivo2.txt','w') as arquivo_2:
    arquivo_2.write('899 Manuel das FLores\n449 Nirvanna da silva\n200 Lucas Colombo')

with open('arquivo1.txt','r') as dados:
    dados_recebidos_arquivo1 = dados.readlines()

with open('arquivo2.txt','r') as dados:
    dados_recebidos_arquivo2 = dados.readlines()

print(dados_recebidos_arquivo1,dados_recebidos_arquivo2)
dados_recebidos_arquivo1.append(dados_recebidos_arquivo2)
print(dados_recebidos_arquivo1)