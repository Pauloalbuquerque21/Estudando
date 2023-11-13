valor_inicial = float(input())
taxa_juros = float(input())
periodo = int(input())

valor_final = valor_inicial

# Iterar, baseado no período em anos, para calculo do valorFinal com os juros.

def juros_compostos(inicio,taxa,periodo):
  
  for ano in range(periodo):
    taxa_valor = inicio * taxa
    inicio = inicio + taxa_valor
  return inicio

valor_final = juros_compostos(valor_inicial,taxa_juros,periodo)

print("Valor final do investimento: R$", valor_final)