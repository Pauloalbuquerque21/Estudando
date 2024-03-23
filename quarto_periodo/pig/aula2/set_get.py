class Pessoa:
    def __init__(self, nome,idade):
        self.nome = nome
        self._idade = idade

    def informa(self):
        print(f'Nome {self.nome} e idade {self.get_idade() + 1}.')


    def get_idade(self):
        return self._idade
    
    def set_idade(self,novo_valor):
        if isinstance(novo_valor,str):
            novo_valor = int(novo_valor)
        self._idade = novo_valor


p1 = Pessoa('carlos','15')

p1.informa()