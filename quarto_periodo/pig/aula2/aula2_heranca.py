class B:
    def __init__(self,nome):
        self.__nome = nome
    
    def transforme(self,dado):
        dado = int(dado)
        print(f'Seu nome {self.__nome} numero somado com 1: {dado +1}')

class A:
    def __init__(self,idade):
        self.__idade = idade
    
    def soma(self,x):
        resul = self.__idade + x
        print(f'resultado {resul}')
class C(B,A):
    def __init__(self,nome,idade):
        B.__init__(self,nome)
        A.__init__(self,idade)



p1 = C('carlos',15)
#p1.transforme('5')
#p2 = C('Matheus')
p1.transforme('6')
p1.soma(2)

p1.nome = 'Matheus'

p1.transforme('6')