class dado():
    def __init__(self,a,b):
        self.a = a
        self.b = b

    def __lt__(self,other): # obs: o valor self.a < other.a  tomarar os valores dependendo do "<" ex: (3 < 10), nesse caso other será o 10, mas se for (3>10) other será o 3.
        print(f'{self.a} e {other.a}')
        return self.a < other.a
        
    
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
print(p1 < p2)

resultado = p1 + p2
p1+=3
print(resultado)
print(p1)