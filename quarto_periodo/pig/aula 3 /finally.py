#caso 1

try:
    try:
        x = int(input("Entre com um numero: "))
        print (x)
    finally:
        print ("Fazendo x igual ao valor default None")
        x = 1
except:
    print ("Ocorreu um Erro!" )

print(x)

#caso 2 
#Finally tem como função executar mesmo se nãi tiver o erro.
try:
    a = 10
    b = 2

    resultado = a / b
except ZeroDivisionError as a:
    print('Você tentou dividir por zero')

finally:
    print('Digisão concluida')

print(resultado)