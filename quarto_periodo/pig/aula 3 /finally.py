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