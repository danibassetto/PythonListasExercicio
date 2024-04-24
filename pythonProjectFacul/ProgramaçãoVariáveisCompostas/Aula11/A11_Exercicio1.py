'''Elabore um algoritmo que leia um vetor com 20 elementos. A seguir, troque o primeiro elemento com o décimo primeiro,
o segundo com o décimo segundo, etc., e mostre o vetor assim modificado'''

a = [0] * 20
print("Informe os valores de A: ")
for i in range(20):
    a[i] = int(input())
for i in range(10):
    a[i], a[i + 10] = a[i + 10], a[i]  # Troca
print(a)