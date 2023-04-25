import math

def ler_pontos_arquivo(nome_arquivo):
    """
    Função para ler as coordenadas dos pontos de um arquivo
    """
    pontos = []
    with open(nome_arquivo, 'r') as arquivo:
        for linha in arquivo:
            linha = linha.strip()
            if linha:
                # Caso a linha não esteja vazia, converte a linha em uma lista de inteiros
                # e adiciona à lista de pontos
                coordenadas = list(map(int, linha.split()))
                pontos.append(coordenadas)
    return pontos

def pontos_dentro_da_esfera(pontos, centro, raio):
    """
    Função para verificar quais pontos estão dentro da esfera definida
    """
    pontos_dentro = []
    for ponto in pontos:
        # Calcula a distância do ponto ao centro da esfera usando a fórmula da distância entre dois pontos em 3D
        distancia = math.sqrt((ponto[0] - centro[0])**2 + (ponto[1] - centro[1])**2 + (ponto[2] - centro[2])**2)
        if distancia <= raio:
            # Se a distância for menor ou igual ao raio, o ponto está dentro da esfera
            pontos_dentro.append(ponto)
    return pontos_dentro

# Nome do arquivo a ser lido
nome_arquivo = input("Digite o nome do arquivo (com extensão .txt): ")

# Lê os pontos do arquivo
pontos = ler_pontos_arquivo(nome_arquivo)

if not pontos:
    # Se a lista de pontos estiver vazia, significa que o arquivo não foi encontrado ou está vazio
    print("Nenhum ponto foi lido - O arquivo não foi encontrado ou está vazio!")
else:
    # Caso contrário, lê as coordenadas do centro e o raio da esfera
    centro = list(map(int, input("Digite as coordenadas do centro da esfera (x y z): ").split()))
    raio = int(input("Digite o raio da esfera: "))

    # Chama a função para verificar quais pontos estão dentro da esfera
    pontos_dentro = pontos_dentro_da_esfera(pontos, centro, raio)

    # Mostra a listagem de pontos lidos e a listagem dos pontos dentro da esfera
    print("Listagem de pontos lidos:")
    for ponto in pontos:
        print(ponto)
    print("Listagem de pontos dentro da esfera:")
    for ponto in pontos_dentro:
        print(ponto)