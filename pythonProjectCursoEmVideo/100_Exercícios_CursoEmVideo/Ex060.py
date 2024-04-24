# Faça um programa que leia um número qualquer e mostre o seu fatorial.

n = int(input("Digite um número para calcular seu fatorial: "))
num = n
fat = 1
print(f'Calculando {n}!')
while num > 0:
    print(f'{num}', end=' ')
    print('x' if num > 1 else '=', end=' ')
    fat *= num
    num -= 1
print(fat)
