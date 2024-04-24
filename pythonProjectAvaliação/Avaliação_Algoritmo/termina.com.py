'''
Trabalho Termina.com - Análise e Projeto de Algoritmos BCC UNIVEM
Danielle Barros Bassetto RA: 62939-1
Prof. Maurício Duarte
'''

A = int(input('Insira um número inteiro: '))
B = int(input('Insira outro número inteiro: '))

conta = 0
b = B # variável 'neutra' para armazenar B

if A >= B:
    while b != 0:
        conta = conta + 1  # Calculando a quantidade de números que há em B
        b = b // 10
    terminacao = A % (10**conta)

    if terminacao == B:
        print(f'{A} termina com {B}')
    else:
        print(f'{A} não termina com {B}')
else:
    print(f'{A} não termina com {B}')