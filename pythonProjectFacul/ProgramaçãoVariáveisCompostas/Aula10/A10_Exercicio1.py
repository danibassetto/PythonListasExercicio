# 10 valores; mostrando o maior e o menor

a = [0] * 10
print("Digite os valores do vetor: ")
for i in range(10):
    a[i] = int(input())

menor = a[0]
maior = a[0]

for i in range(10):
    if a[i] < menor:
        menor = a[i]
    else:
        if a[i] > maior:
            maior = a[i]
print("Maior =",maior,"Menor =",menor)