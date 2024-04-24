''' Elabore um algoritmo que leia um vetor de 10 caracteres (a, b, c, d ou e) que é o gabarito de uma prova de múltipla
escolha aplicada a vários candidatos. Em seguida leia o vetor resposta de cada candidato (também um vetor de 10
caracteres) e mostre a nota resultante do candidato (0 a 10).  Repita o processo enquanto existir candidato para ser
avaliado. '''


g = [0] * 10
print("Insira o gabarito correto: ")
for i in range(10):
    g[i] = input()

while True:
    r = [0] * 10
    print("Digite as respostas do aluno: ")
    for i in range(10):
        r[i] = input()

    nota = 0
    for i in range(10):
        if (r[i] == g[i]):
            nota += 1
    print("Nota:",nota)
    resp = input("Deseja corrigir outra prova? [S/N] ")
    if resp == 'N':
        break

