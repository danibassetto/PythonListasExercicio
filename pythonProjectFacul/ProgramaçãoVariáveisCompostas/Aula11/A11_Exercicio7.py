''' Idem ao 6) para o algoritmo  Select Sort. '''

A = [0] * 10
print("Insira os valores de A: ")
for i in range(10):
    A[i] = int(input())
for i in range(10):
    menor = A[i]
    pos = i
    for j in range(i+1, 10):
        menor = A[j]
        pos = j
    A[i], A[pos] = A[pos], A[i]
print(A)
