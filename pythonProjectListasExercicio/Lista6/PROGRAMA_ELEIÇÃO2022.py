''' O TSE fornecerá para o seu programa a seguinte entrada:
• Uma linha com a ;
• Uma , sendo um nome por linha;
• Uma lista com n+2 valores inteiros, um por linha, sendo que a i-ésima linha representa a
quantidade de votos recebidos pelo i-ésimo candidato, seguindo a ordem de leitura da
lista de nomes. Os últimos dois valores representam a quantidade de votos brancos e
nulos, respectivamente.

Você pode assumir que todos os candidatos receberam uma quantidade distinta de votos. '''

n = int(input())
l1 = []
l2 = []
for i in range(n):
    l1.append(input())
totalVotos = 0
votosValidos = 0
for i in range(n+2):
    l2.append(int(input()))
    if i < n:
        votosValidos += l2[i]
    totalVotos += l2[i]

media = votosValidos/2

maxVotos = 0
posMaxVotos = 0
for i in range(n):
    if l2[i] > maxVotos:
        maxVotos = l2[i]
        posMaxVotos = i
if maxVotos > media:
    print(l1[posMaxVotos], "foi o vencedor da eleição")
else:
    print("Haverá segundo turno entre:")
    print(l1[posMaxVotos])
    segMaxVotos = 0
    posSegMaxVotos = 0
    for i in range(n):
        if l2[i] > segMaxVotos and l2[i] != maxVotos:
            segMaxVotos = l2[i]
            posSegMaxVotos = i
    print(l1[posSegMaxVotos])
print("Total de votos:", totalVotos)
print("Votos válidos:", votosValidos)

