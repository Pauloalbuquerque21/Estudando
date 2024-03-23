class B():
    n = 2
    def f(self,x):
        return B.n*x
    
class C(B):
    def f(self,x):
        return B.f(self,x)**2

p1 = B()
p2 = C()
print(p2.f(3))
print(p1.f(2))

#erro
#Erro, pois tem que usar o self
class D(B):
    def f(slef,x):
        return B.f(x)**2

p3 = D()
print(p3.f(3))
    
