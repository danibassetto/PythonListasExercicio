''' Elabore um algoritmo que gere um vetor contendo os n primeiros valores da série de Fibonacci: '''

F = [1, 1]
n = int(input("Insira o número de valores de fibonacci que deseja mostrar: "))
for i in range(2, n):
    F.insert(i, F[i-1] + F[i-2])

print(F)