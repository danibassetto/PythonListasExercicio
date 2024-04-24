''' Elabore um programa em Python que declare uma matriz quadrada de 10 linhas por 10
colunas e verifique se a matriz é simétrica em relação à diagonal principal.

     1 2 3 4
     2 1 5 6
     3 5 1 7
     4 6 7 1
'''


print("Informe os números da matriz")
A = [0] * 4
for i in range(4):
    A[i] = [0] * 4
    for j in range(4):
        A[i][j] = int(input(f"[{i}][{j}] >> "))
    print()
print('=-' * 10)
print("Matriz informada:")
for i in range(4):
    for j in range(4):
       print(f"{A[i][j]:2}",end=" ")
    print()

MS = [0] * 4
for i in range(4):
    MS[i] = [0] * 4
    for j in range(4):
        MS[i][j] = A[j][i]

if A == MS:
    print("Matriz SIMÉTRICA em relação a Diagonal Principal!!")
else:
    print("Matriz NÃO SIMÉTRICA em relação a Diagonal Principal!!")