import math

def ler_pontos_arquivo(nome_arquivo):
    pontos = []
    with open(nome_arquivo, 'r') as arquivo:
        for linha in arquivo:
            linha = linha.strip()
            if linha:
                coordenadas = list(map(int, linha.split()))
                pontos.append(coordenadas)
    return pontos

def pontos_dentro_da_esfera(pontos, centro, raio):
    pontos_dentro = []
    for ponto in pontos:

        distancia = math.sqrt((ponto[0] - centro[0])**2 + (ponto[1] - centro[1])**2 + (ponto[2] - centro[2])**2)
        if distancia <= raio:
            pontos_dentro.append(ponto)
    return pontos_dentro
nome_arquivo = input("Digite o nome do arquivo: ")

pontos = ler_pontos_arquivo(nome_arquivo)

if not pontos:
    print("Nenhum ponto foi lido - O arquivo não foi encontrado ou está vazio!")
else:
    centro = list(map(int, input("Digite as coordenadas do centro da esfera (x y z): ").split()))
    raio = int(input("Digite o raio da esfera: "))
    pontos_dentro = pontos_dentro_da_esfera(pontos, centro, raio)
    print("Listagem de pontos lidos:")
    for ponto in pontos:
        print(ponto)
    print("Listagem de pontos dentro da esfera:")
    for ponto in pontos_dentro:
        print(ponto)