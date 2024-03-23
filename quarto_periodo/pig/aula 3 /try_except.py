try:
    # Código que pode gerar uma exceção
    resultado = 10 / 0  # Divisão por zero, gera uma exceção ZeroDivisionError
except ZeroDivisionError:
    # Código a ser executado se ocorrer uma exceção do tipo ZeroDivisionError
    print("Erro: Divisão por zero!")
except Exception as e:
    # Código a ser executado se ocorrer qualquer outra exceção
    print(f"Erro desconhecido: {e}")