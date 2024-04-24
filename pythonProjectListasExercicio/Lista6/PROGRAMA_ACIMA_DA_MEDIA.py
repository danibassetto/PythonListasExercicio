''' A entrada contém muitos casos de teste. A primeira linha da entrada contém um inteiro C,
indicando o número de casos de teste. Seguem C casos de teste ou instâncias. Cada caso de teste
inicia com um inteiro N, que é o número de pessoas de uma turma (1 ≤ N ≤ 1000). Seguem N
inteiros, separados por espaços, cada um indicando a média final (um inteiro entre 0 e 100) de
cada um dos estudantes desta turma.
Saída
Para cada caso de teste imprima uma linha dando o percentual de estudantes que estão acima
da média da turma, com o valor arredondado e com 3 casas decimais '''

C = int(input())
for i in range(C):
    L = input().split()
    soma = 0
    for i in range(len(L)):
        L[i] = int(L[i])  # Transformando de string para int e somando
        soma += L[i]
    soma -= L[0]  # subtraindo o primeiro valor
    N = L[0]
    media = soma/N
    acima = 0  # Calculando quantos estão acima
    for i in range(1,len(L)):
        if L[i] > media:
            acima += 1
    per = (acima / N) * 100
    print(f'{per:.3f}%')