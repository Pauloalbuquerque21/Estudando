class Erro(Exception):
    def __init__(self, mensagem):
        self.mensagem = mensagem
    
    def __str__(self):
        return f'Mensagem personalizada: {self.mensagem}'    

def customization(a):
    if isinstance(a, str):
        raise Erro('Tipo digitado incorreto')

while True:
    try:
        a = input('Digite o primeiro número:')
        customization(a)
        a = int(a)  # Converte para inteiro após verificar se é uma string
    except Erro as erro:
        print(erro)
    except ValueError:
        print('Digite um número válido.')
    else:
        break
