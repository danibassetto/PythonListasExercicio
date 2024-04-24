'''Elabore um algoritmo que leia um vetor capaz de armazenar 20 valores inteiros e, em seguida, gere outros dois
vetores, um formado  pelos valores pares e o outro pelos valores ímpares'''

print("Informe os valores de A: ")
a = [0] * 20
for i in range(20):
    a[i] = int(input())
b = []
c = []
for i in range(20):
    if a[i] % 2 == 0:
        b.append(a[i])
    else:
        c.append(a[i])
print("A:",a)
print("PARES:",b)
print("ÍMPARES:",c)