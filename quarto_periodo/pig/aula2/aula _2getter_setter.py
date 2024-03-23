class pessoa:
    def __init__(self, nome,idade):
        self.nome = nome
        self.idade = idade

    def informa(self):
        print(f'Nome {self.nome} e idade {self.idade+1}.')


    @property
    def idade(self):
        return self._idade
    
    @idade.setter
    def idade(self,errado):
        if isinstance(errado,str):
            errado = int(errado)
        self._idade = errado


p1 = pessoa('carlos','15')
p1.informa()