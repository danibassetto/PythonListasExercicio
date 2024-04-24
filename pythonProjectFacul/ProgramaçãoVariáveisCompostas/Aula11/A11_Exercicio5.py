''' Idem ao 5, porem gerando o vetor união de A com B (Todos os elementos de A e somente os elementos de B que não
existem em A). '''

U = []
A = [0] * 10
print("Insira os valores de A: ")
for i in range(10):
    A[i] = int(input())
    U.append(A[i])
print("A =",A)
B = [0] * 10
print("Insira os valores de B: ")
for i in range(10):
    B[i] = int(input())
print("B =",B)

for i in range(10):
    if B[i] not in A:
        U.append(B[i])
print("U =", sorted(U))

