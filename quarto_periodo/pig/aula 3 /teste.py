

#a = eval(input('teste:'))

#if isinstance(a,str):
#    print('é uma string')
#elif isinstance(a,float):
#    print('É um float')
#else:
#    print('é um int')

#print(a)

try:
    try:
        x = eval(input("Entre com um numero: "))
        print (x)
    finally:
        print ("Fazendo x igual ao valor default None")
        x = 1
except:
    print ("Ocorreu um Erro!" )

print(x)