import math

def ler_pontos():
    pontos = []
    while True:
        linha = input().strip()
        if not linha:
            return pontos
        else:
            coordenadas = list(map(int, linha.split()))
            pontos.append(coordenadas)

def pontos_dentro_da_esfera(pontos, centro, raio):
    pontos_dentro = []
    for ponto in pontos:
        distancia = math.sqrt((ponto[0] - centro[0])**2 + (ponto[1] - centro[1])**2 + (ponto[2] - centro[2])**2)
        if distancia <= raio:
            pontos_dentro.append(ponto)
    return pontos_dentro
print("Digite as coordenadas dos pontos (x y z), uma linha por vez. Pressione Enter para encerrar:")
pontos = ler_pontos()

if not pontos:
    print("Nenhum ponto foi lido - A primeira linha lida estava vazia!!!")
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