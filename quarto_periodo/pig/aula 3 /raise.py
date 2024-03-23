a = int(input('Digite o númerador:'))
b = int(input('digite o denominador:'))

class matematica():
    def __init__(self,num,den):
        self.num = num
        self.den = den
    
    def dividir(self):
        if self.den == 0:
            raise ValueError('digitou 0""""')
        return self.num / self.den
    
    
try:
    resultado = matematica(a,b)
    print(resultado.dividir())