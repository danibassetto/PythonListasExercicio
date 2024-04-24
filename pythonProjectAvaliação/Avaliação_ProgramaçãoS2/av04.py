""""
    CESAR AUGUSTO DE ALMEIDA - RA: 626848
    DANIELLE BARROS BASSETTO  - RA: 629391
    GABRIEL BARROS DE MELO AMORIM  - RA: 574015
    JOÃO VITOR ADONIS - RA: 590428
    MARLLON SILVA ARAUJO COELHO  - RA: 627021
    MATHEUS HENRIQUE DE LIMA - RA: 626732
"""

N = int(input())

for i in range(N):

    P1=[int(i) for i in input().split()]
    P2=[int(i) for i in input().split()]

    somaQuadrados = []  #Soma os quadrados de cada posição da Tentativa
    somaVermelhos = 0  # Esse soma todos os Pontos em vermelhos de cada Posição
    pontuacao = []  #Pontos vermelhos de cada Tentativa

    somaQuadradosInvertida = []
    somaVermelhosInvertida = 0
    pontuacaoInvertida = []


    if len(P1) <= len(P2):
        for j in range((len(P2) - len(P1)) + 1):  #Pula uma posição a cada tentativa

            P1Invertida = P1[::-1]

            for k in range(len(P1)):  #Soma os quadrados de todas as posições de P1 sob P2
                soma = P1[k] + P2[j]
                somaQuadrados.append(soma)

                somaInvertida = P1Invertida[k] + P2[j]
                somaQuadradosInvertida.append(somaInvertida)

                soma = 0
                somaInvertida = 0
                j += 1

            maior = max(somaQuadrados, key=int)
            somaQuadrados.pop(somaQuadrados.index(maior))

            maiorInvertida = max(somaQuadradosInvertida, key=int)
            somaQuadradosInvertida.pop(somaQuadradosInvertida.index(maiorInvertida))

            for k in range(len(somaQuadrados) - 1):  #Soma do total dos quadrados em vermelhos de cada Tentativa
                dif = maior - somaQuadrados[k]  #Pega a quantidade de vermelhos de cada posição
                somaVermelhos += dif

                difInvertida = maiorInvertida - somaQuadradosInvertida[k]
                somaVermelhosInvertida += difInvertida

            pontuacao.append(somaVermelhos)  #Adicionando o total de quadrados vermelhos da tentativa na lista
            pontuacaoInvertida.append(somaVermelhosInvertida)

            somaVermelhos = 0  #Zera para repetir na próxima tentativa
            somaVermelhosInvertida = 0

            somaQuadrados.clear()  #Limpa para repetir na próxima tentativa
            somaQuadradosInvertida.clear()

        pontuacaoCrescente = pontuacao.copy()
        pontuacaoCrescente.sort()  # Coloco em ordem crescente para pegar a Menor pontuação (Encaixe)

        pontuacaoCrescenteInvertida = pontuacaoInvertida.copy()
        pontuacaoCrescenteInvertida.sort()

        if (pontuacaoCrescente[0] == 0):
            print(f"\nEncaixe perfeito!\n"
                  f"Posição de Encaixe: {pontuacao.index(pontuacaoCrescente[0]) + 1}\n"
                  f"Peça: Normal\n")

        elif (pontuacaoCrescenteInvertida[0] == 0):
            print(f"\nEncaixe perfeito!\n"
                  f"Posição de Encaixe: {pontuacaoInvertida.index(pontuacaoCrescenteInvertida[0]) + 1}\n"
                  f"Peça: Invertida\n")

        elif (int(min(pontuacaoInvertida, key=int)) < int(min(pontuacaoInvertida, key=int))):
            print(f"\nEncaixe perfeito!\n"
                  f"Posição de Encaixe: {pontuacaoInvertida.index(pontuacaoCrescenteInvertida[0]) + 1}\n"
                  f"Peça: Invertida\n")

        elif (int(min(pontuacao, key=int)) <= int(min(pontuacaoInvertida, key=int))):
            print(f"\nPontuacao: {pontuacaoCrescente[0] + 1} \n"
                  f"Posição de Encaixe: {pontuacao.index(pontuacaoCrescente[0])}\n"
                  f"Peça: Normal\n")
    else:
        print("INVALIDO! P1 maior que P2.")