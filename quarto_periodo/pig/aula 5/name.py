def minha_funcao():
    print("Executando minha_funcao()")

print("O nome do módulo é:", __name__)

if __name__ == "__main__":
    print("Este módulo está sendo executado como o programa principal")
    minha_funcao()
else:
    print("Este módulo está sendo importado por outro módulo")