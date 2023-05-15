# r -> read -> ler o arquivo
# w -> write -> escrever 
# a -> append -> adicionar


#with open(nome do arquivo,o que você quer fazer) as tranforma essa ação para a variavel "arquivo"
with open('email.txt','r') as arquivo:
    arquivo.read()