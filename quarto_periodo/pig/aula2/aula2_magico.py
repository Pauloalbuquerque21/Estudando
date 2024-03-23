class dado():
    def __init__(self,a,b):
        self.a = a
        self.b = b

    def __str__(self): #Sé você quizer fazer um print do objeto
        return f'{self.a},{self.b}'
    
    def __add__(self,other):# se você quizer fazer uma adição entre objetos
        return f'{self.a+other.a}, {self.b + other.b}'
    
    def __mul__(self,other):#Se você quizer fazer multiplicação entre objeto
        return f'{self.a * other.a},{self.b * other.b}'
    
    def __iadd__(self,other):
        self.a+=other
        self.b+=other
        return self.a,self.b

    

p1 = dado(1,2)
p2 = dado(2,3)
p3 = dado(3,4)

resultado = p1 + p2
p1+=3
print(resultado)
print(p1)