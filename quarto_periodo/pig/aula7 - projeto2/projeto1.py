
class franc():
    def __init__(self,numerador, denominador):
        self.numerador = numerador
        self.denominador = denominador
    
    def __str__(self):
        return f'{self.numerador}/{self.denominador}'
    
#Função para mmc
    def mmc(valor1,valor2):
        lista = list()
        denominador1 = valor1
        denominador2 = valor2
        for c in range(2,10):
            while True: #parte que pegamos os valores do mmc
                if (denominador1 % c == 0) or (denominador2 % c == 0):
                    if denominador1 % c == 0:
                        denominador1 = denominador1 / c
                    if denominador2 % c == 0:
                        denominador2 = denominador2 / c
                    lista.append(c)
                else:
                    break
        mmc = 1
        for dados in lista:#soma dos valores do mmc
            mmc = mmc * dados
        return mmc
    
#Adição de franções
    def __add__(self,other):
        numerador1 = 0 #criei essa variavel, pois não quero comprometer os valores do self.numerador e other
        numerador2 = 0
        mmc = franc.mmc(self.denominador,other.denominador) 
        numerador1 = self.numerador * (mmc / self.denominador)
        numerador2 = other.numerador * (mmc / other.denominador)
        
        return f'{(numerador1+numerador2)} /{mmc}'
    #def __iadd__(self,other):
    #    self.numerador += other
    #    self.denominador += other
    #    return self

#Função Multiplicação 
    def __mul__(self,other):
        return f'{self.numerador * other.numerador}/{self.denominador * other.denominador}'
    
    def __eq__(self,other):
        return f'{self.numerador == other.numerador and self.denominador == other.denominador}'

    def __sub__(self,other):
        mmc = franc.mmc(self.denominador,other.denominador)
        numerador_sub1 = self.numerador * (mmc / self.denominador)
        numerador_sub2 = other.numerador * (mmc / other.denominador)
        return f'{numerador_sub1 - numerador_sub2} / {mmc}'
    

    
    def __truediv__(self,other):
        numerador_division = self.numerador * other.denominador
        divisor_division = self.denominador *other.numerador
        return numerador_division / divisor_division
    
    
franc1 = franc(5,10)
franc2 = franc(5,4)
franc3 = franc(4,10)


"""
result_soma = franc1 + franc2
#result2 = franction1 + franction2 + franction3
result_mult = franc1 * franc2
result_eq = franc1 == franc2
result_division = franc1 / franc2
result_sub = franc1 - franc2


print(f'soma: {result_soma}')
print(f'multiplicação: {result_mult}')
print(f'igualdade: {result_eq}')
print(f'Divisão: {result_division}')
print(f'MMC: {franc.mmc(4,5)}')
print(f'Subtração: {result_sub}')

"""
