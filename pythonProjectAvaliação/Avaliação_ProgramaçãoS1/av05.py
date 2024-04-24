'''
AVALIAÇÃO 05 - TRIÂNGULO DE PASCAL

Gabriel Barros de Melo Amorim - RA: 574015
Cesar Augusto de Almeida - RA: 626848
Danielle Barros Bassetto - RA: 629391
João Vitor Adonis - RA: 590428
Marllon Silva Araujo Coelho - RA: 627021
Matheus Henrique de Lima - RA: 626732


n = int(input())

t = []
for i in range(n):
    t.append([])
    for j in range(i+1):
        if j == 0 or i == j:
            t[i].append(1)
        else:
            t[i].append(t[i-1][j-1] + t[i-1][j])

for i in range(n):
    for j in range(i+1):
        print(f"{(t[i][j]):2}", end=" ")
    print()
'''

N = int(input('Informe o tamanho do triângulo >> '))
M = []
for i in range(N):
    c = 1
    M.append([])
    for j in range(i+1):
        M[i].append(c)
        c = c * ((i+1) - (j+1)) // (j+1)

for i in range(N):
    linha = ''
    for j in range(i+1):
        linha += f'{M[i][j]:3} '
    print(linha.center(4*N))

#outra solução
M = []
for i in range(N):
    M.append([])
    linha = ''
    for j in range(i + 1):
        if i == j or j == 0:
            M[i].append(1)
        else:
            M[i].append(M[i - 1][j - 1] + M[i - 1][j])
        linha += f'{M[i][j]:2}  '
    print(linha.center(N*4))

#outra solução
for i in range(N):
    print(f'{M[i]}'.center(N*4))

