# Repetir o programa todo
# Faça um programa para verificar se o número é par ou ímpar

resp = 'S'
while resp == 'S':
    num = int(input('Número: '))
    if num % 2 == 0:
        print('Par!')
    else:
        print('Ímpar!')
    resp = input('Deseja testar outro número? [S/N] ').upper()