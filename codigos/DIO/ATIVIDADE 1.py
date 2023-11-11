saldo_atual = float(input('Digite o saldo atual:'))
valor_deposito = float(input('Digite o valor que irá depositar:'))
valor_retirada = float(input('Digite o valor que irá retirá:'))

#TODO: Calcular o saldo atualizado de acordo com a descrição deste desafio.
saldo_atual = (saldo_atual + valor_deposito) - valor_retirada
#TODO: Imprimir o a saída de conforme a tabela de exemplos (uma casa decimal).
print(f'Saldo atual igual {saldo_atual:.2f}')