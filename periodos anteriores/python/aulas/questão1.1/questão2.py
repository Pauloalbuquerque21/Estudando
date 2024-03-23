frase = str(input('Digite uma frase:')).lower()
a1 = frase.count('a')
e1 = frase.count('e')
i1 = frase.count('i')
o1 = frase.count('o')
u1 = frase.count('u')

soma = a1+e1+i1+o1+u1
if soma>0:
    print(f"No total há {soma} vogais na entrada {frase}\nHá {a1}A's, {e1}E's, {i1}I's, {o1}O's, {u1}U's")