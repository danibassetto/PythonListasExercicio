'''Elabore um programa que leia um vetor capaz de armazenar 10 números e em seguida, leia um valor e verifique se este
valor existe ou não no vetor lido. Caso ele exista, indique quantas vezes ele aparece no vetor'''

a = [0] * 10
print("Informe os valores de A: ")
for i in range(10):
    a[i] = int(input())
print(a)
n = int(input("Insira um número para saber se ele está em 'A': "))
if n in a:
    cont = 0
    for i in range(10):
        # cont = a.count(n)
        if n == a[i]:
            cont += 1
    print("O valor apareceu",cont,"vezes")
else:
    print("O valor não existe na lista")