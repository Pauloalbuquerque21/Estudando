
class Erro(Exception):
    def __init__(self,mensagem):
        self.mensagem = mensagem
    
    def __str__(self):
        return f'Mensagem personalizada: {self.mensagem}'    

def customization(a):
    if isinstance(a, str):
        raise Erro('Tipo digitado incorreto')





while True:
    try:
        a = int(input('Digite o primeiro número:'))
        b = int(input('Digite um outro valor:'))
        c = a / b
    except(ZeroDivisionError):
        print('Digitou número zero')
    else:
        break