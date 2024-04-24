'''
João quer montar um painel de leds contendo diversos números. Ele não possui muitos leds, e não
tem certeza se conseguirá montar o número desejado. Considerando a configuração dos leds dos
números abaixo, faça um algoritmo que ajude João a descobrir a quantidade de leds necessário para
montar o valor

Entrada
A entrada contém um inteiro N, (1 ≤ N ≤ 1000) correspondente ao número de casos de teste,
seguido de N linhas, cada linha contendo um número (1 ≤ V ≤ 10100) correspondente ao valor que
João quer montar com os leds.

Saída
Para cada caso de teste, imprima uma linha contendo o número de leds que João precisa para
montar o valor desejado, seguido da palavra "leds"
'''

L = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]

n = int(input())

while n > 0:
    somaled = 0
    x = input()
    for i in x:
        somaled += L[int(i)]
    print(somaled, "leds")
    n -= 1


'''
def contaLeds(n):
    leds = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]
    l = 0
    for d in str(n):
        l += leds[int(d)]
    return l

N = int(input())
for i in range(N):
    V = int(input())
    print(f'{contaLeds(V)} leds')
'''