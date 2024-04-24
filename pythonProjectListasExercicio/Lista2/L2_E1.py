''' Programa que leia um número de 3 algarismos, faça a validação para aceitar apenas  números  menores
que  1000) e imprima  se  ele  é  ascendente (se seus algarismos estão em ordem crescente, exemplo: 258)'''

num = int(input('Insira um número de 3 algarismos >> '))
if num < 100 or num > 999:
    print('Número inválido!')
else:
    c = num // 100
    d = num % 100 // 10
    u = num % 10
    if c < d < u:
        print(f'O número {num} é ascendente')
    else:
        print(f'O número {num} não é ascendente')