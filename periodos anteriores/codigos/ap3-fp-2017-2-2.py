
while True:
    digitos = 0
    vogais = 0 
    consoantes = 0
    arquivo = input("Digite o nome do arquivo:").lower().strip()
    if arquivo == 'fim':
        break
    else:
        dados_arquivo = open(arquivo,"r")
        for dados in dados_arquivo:
            dado2 = dados.upper().strip().split()
            for dado in dado2:
                for dado3 in dado:
                    if dado3 in "AEIOUÀÁÉÔU":
                        vogais += 1
                    else:
                        if dado3 in '0123456789':
                            digitos +=1
                        else:
                            consoantes += 1

        print(f"Qunatidade de Vogais:{vogais}\nQuantidade de consoantes em xyz:{consoantes}\nQuantidade de dígitos em xyz:{digitos}.")