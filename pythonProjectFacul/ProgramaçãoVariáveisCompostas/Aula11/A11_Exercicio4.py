''' Elabore um algoritmo que leia dois (A e B) vetores de 10 elementos inteiros cada. Calcule um terceiro vetor formado
pela intersecção ( C ) dos vetores lidos. (Elementos que existem em ambos os vetores A e B, não importando
suas posições). '''

A = [0] * 10
print("Insira os valores de A: ")
for i in range(10):
    A[i] = int(input())
print("A =",A)
B = [0] * 10
print("Insira os valores de B: ")
for i in range(10):
    B[i] = int(input())
print("B =",B)
C = []
for i in range(10):
    if A[i] in B:
        C.append(A[i])

if len(C) == 0:
    print("Intersecção vazia")
else:
    print("Intersecção =",C)