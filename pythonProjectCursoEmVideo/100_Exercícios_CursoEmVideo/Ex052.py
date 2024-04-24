# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

num = int(input("Digite um número: "))
div = 0
for i in range(1, num + 1):
    if num % i == 0:
        print('\033[31m', end='')
        div += 1
    else:
        print('\033[36m', end='')
    print(i, end='')
print(f"\n\033[mO número {num} foi divisível {div} vezes")
if div == 2:
    print("Portanto, ele é primo!")
else:
    print("Portanto, não é primo!")
