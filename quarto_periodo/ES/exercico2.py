l1 = [1,2,3,4,5]
l2 = [5,6,7,8,9]
elementos = list()

tamanho_l2=len(l2)

def Buscar(x):
    i = 0
    resultado = -1 
    while i < tamanho_l2:
        if l2[i] != x:
            resultado = i
            break
        else:
            i = i + 1 
    return resultado

for c in l1:
    valores = Buscar(c)
    if valores != -1:    
        l2.append(l1[valores])
    elementos.append(valores)
    
print(elementos)

print(l2)