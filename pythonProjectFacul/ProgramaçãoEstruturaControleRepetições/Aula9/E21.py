'''Elabore um algoritmo que leia um número inteiro e retorne com o número primo mais próximo a ele. Veja o exemplo:

Num == 100  número primo mais próximo = 97
'''

n = int(input("Informe um número: "))

for i in range(n, 1, -1):  # Contagem regressiva de n até 1
    div = 0
    cont = 0
    for j in range(1, n + 1):
        if i % j == 0:
            div += 1
    if div == 2:  # Pois para ser primo ele deve ser divisível (sem resto) apenas por 1 e por ele mesmo, então são apenas 2 divisões!
        print(i)
        cont += 1
        if cont == 1:  # Quando o programa imprimir 1 valor, ele será encerrado, conforme o proposto
            break