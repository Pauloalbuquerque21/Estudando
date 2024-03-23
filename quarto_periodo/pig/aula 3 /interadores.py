class dados:
    def __init__(self,limite):
        self.limite = limite
        self.init = 0

    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.init < self.limite:
            self.init += 1
            return self.init
        else:
            raise StopIteration
        

teste = dados(10)

for c in teste  :
    print(c)


