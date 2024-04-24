'''
Trabalho 02 Últimos valores primos - Análise e Projeto de Algoritmos BCC UNIVEM
Danielle Barros Bassetto RA: 62939-1
Prof. Maurício Duarte
'''

n = int(input("Insira um número para ver os dois últimos primos que o antecedem: "))

cont = 0
for i in range(n, 1, -1):  # Contagem regressiva de n até 1
    div = 0
    for j in range(1, n + 1):
        if i % j == 0:
            div += 1
    if div == 2:  # Pois para ser primo ele deve ser divisível (sem resto) apenas por 1 e por ele mesmo, então são apenas 2 divisões!
        print(i)
        cont += 1
        if cont == 2:  # Quando o programa imprimir 2 valores, ele será encerrado, conforme o proposto
            break