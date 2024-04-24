''' Elabore um programa em Python que leia duas matrizes A (mxn) e B (pxq) e calcule e
mostre a matriz Python que é a soma de A com B (caso a soma seja possível). '''

print("Informe as dimensões da matriz A:")
m = int(input("Linhas  >> "))
n = int(input("Colunas >> "))

print("Informe as dimensões da matriz B:")
p = int(input("Linhas  >> "))
q = int(input("Colunas >> "))

if m == p and n == q:
    print("Informe os elementos da matriz A")
    A = [0] * m
    for i in range(m):
        A[i] = [0] * n
        for j in range(n):
            A[i][j] = int(input(f"[{i}][{j}] >> "))
        print()

    print("Informe os elementos da matriz B")
    B = [0] * p
    for i in range(p):
        B[i] = [0] * q
        for j in range(q):
            B[i][j] = int(input(f"[{i}][{j}] >> "))
        print()

    print('=-' * 10)
    print("Matriz A:")
    for i in range(m):
        for j in range(n):
            print(f"{A[i][j]:02}", end=" ")
        print()

    print('=-' * 10)
    print("Matriz B:")
    for i in range(m):
        for j in range(n):
            print(f"{B[i][j]:02}", end=" ")
        print()

    print('=-' * 10)
    print("Matriz soma:")
    C = [0] * m
    for i in range(m):
        C[i] = [0] * n
        for j in range(n):
            C[i][j] = A[i][j] + B[i][j]
            print(f"{C[i][j]:02}", end=" ")
        print()
else:
    print("Não é possível efetuar a soma com essas dimensões!!")