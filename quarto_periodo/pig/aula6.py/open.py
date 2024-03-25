#Você ler o arquivo e transforma em uma lista os caractéres 
arquivo = open('teste.txt','r')
dado = arquivo.readlines()
print(dado)
arquivo.close()

#Você ler só a primeira linha do arquivo
arquivo = open('teste.txt','r')
dado = arquivo.readline()
print(dado)
arquivo.close()

#ler o arquivo
arquivo = open('teste.txt','r')
dado = arquivo.read()
print(dado)
arquivo.close()

#Você escreve alguma coisa no arquivo, apagando qualquer conteúdo existente
arquivo = open('teste.txt','w')
arquivo.write('Oi!')
arquivo.close()

#adicionar conteúdo, sem apagar o conteúdo já existente o arquivo
arquivo = open('teste.txt','ab')
arquivo.write(b'\nOi!')
arquivo.close()

