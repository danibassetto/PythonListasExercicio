'''
Leia uma matriz 5 x 10 que se refere respostas de 10 questões de múltipla escolha, referentes a 5 alunos. Leia também um
vetor de 10 posições contendo o gabarito de respostas que podem ser a, b, c ou d. Se preferir, podem ser gerados
aleatoriamente. Seu programa devera comparar as respostas de cada candidato com o gabarito e emitir um vetor denominado
resultado, contendo a pontuação correspondente a cada aluno.
'''

from random import *

alternativas = ['a', 'b', 'c', 'd']
print('Respostas dos alunos')
resposta = []
for i in range(5):
    resposta.append([])
    print(f'Aluno {i + 1} >>', end=' ')
    for j in range(10):
        # resposta[i].append(sample(alternativas,1)[0])
        # resposta[i].append(choice(alternativas))
        resposta[i].append(alternativas[randint(0, 3)])
        print(f'{resposta[i][j]}', end=' ')
    print()

gabarito = []
for i in range(10):
    # gabarito.append(sample(alternativas,1)[0])
    # gabarito.append(choice(alternativas))
    gabarito.append(alternativas[randint(0, 3)])
print('\nGabarito >>', *gabarito)

print('\nAcertos')
acertos = [0] * 5
for i in range(5):
    for j in range(10):
        if resposta[i][j] == gabarito[j]:
            acertos[i] += 1
for i in range(5):
    print(f'Aluno {i + 1} >>', acertos[i])
