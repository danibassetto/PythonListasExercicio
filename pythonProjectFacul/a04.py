p1 = input()
p1 = p1.split()

p2 = input()
p2 = p2.split()

somaPosicao = []
pontuacao = []
somaDif = 0

if len(p1) <= len(p2):
    for z in range((len(p2) - len(p1)) + 1):

        for i in range(len(p1)):
            soma = int(p1[i]) + int(p2[z])
            somaPosicao.append(soma)
            soma = 0
            z += 1

        print(f"Soma: {somaPosicao}")
        copy = somaPosicao.copy()
        copy.pop(copy.index(max(copy, key=int)))
        for i in range(len(somaPosicao) - 1):
            dif = int(max(somaPosicao, key=int)) - int(copy[i])
            somaDif += dif

        pontuacao.append(somaDif)
        somaDif = 0
        somaDif2 = 0
        somaPosicao.clear()
        print(f"Pontuação: {pontuacao}")

    crescente = pontuacao.copy()
    crescente.sort()
    if crescente[0] == 0:
        print(f"\nEncaixe perfeito!\n"
              f"Posição de Encaixe: {pontuacao.index(crescente[0]) + 1}\n"
              f"Peça: Normal\n")
    else:
        print(f"\nPontuação: {crescente[0]} \n"
              f"Posição de Encaixe: {pontuacao.index(crescente[0]) + 1}\n"
              f"Peça: Normal\n")
else:
    print("INVALIDO! P1 maior que P2.")
