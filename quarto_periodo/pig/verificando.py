from funções import ola
"""
class dado():
    __h = 1
    __l = 2
    def __init__(self,a = []):
        self.a = a
    def f(self, l, h):
        self.a = [l,h]
        return dado(self.a)
    def __repr__(self):
        return (str(self.a))
    def f(self, l, h):
        self.a = [l,h]
        return dado(self.a)
    def g(self, l, h):
        self.a = [l,h]
        return self.a
    

a = dado()
b = a.g(1,2)

print(a)
print(b)

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    def __repr__(self):
        return f'Pessoa("{self.nome}", {self.idade})'

pessoa = Pessoa("João", 30)
print(pessoa)  # Saída: Pessoa("João", 30)

"""
"""
lista = [1,2,3,4,5]
a = lista.index(5)
print(a)
print(lista[1:])
"""
#ola('calos')
"""
class C():
    def __init__(self,a,b):
        self.a = a 
        self.b = b
    
    def __add__(self,c):
        print(c.b,c.a,self)
        return C(c.b[2]+c.b[1]+c.b[0]+self.a[2]+self.a[1]+self.a[0],self.b+c.b)
    def __repr__(self):
        return self.a + self.b

p1 = C("ABC","DEF")
p2 = C("foo","bar")

print(p1 + p2)

"""

"""
def g(a,b):
    if len(a)<b:
        return [a]
    return [a[:b]]+g(a[b:],b+3)

print(g(list(range(10)),3))

"""

#dicionario = {'b':2,'a':1,'c':5}
#chaves_ordenadas = sorted(dicionario)
#print(chaves_ordenadas)
"""
lista = [1,2,3,4,5]
soma = sum(lista,10)
print(soma)
soma2 = []
casa = {"casa1":4,"casa2":6,"casa3":10}
for c,valor in casa.items():
    print(valor)
    soma2.append(valor)

print(sum(soma2))
"""
"""
class C:
    a = 1
    def __init__(self,x=[]):
        self.x = x
    def g(self,a):
        self.x += [a]
        self.a += 1
        return C(self.x)
    def __repr__(self):
        print(self.a)
        return (str(self.x*self.a))



p1 = C()
obj = p1.g(1)
print(f'primeira soma {p1.a}')
print(obj.g(3))
print(f'Segunda soma {p1.a}')
print(obj.g(2))
"""