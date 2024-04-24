'''Programa que peça ao usuário para digitar um número inteiro positivo, informe se este número
é par ou ímpar. Caso o usuário digite um número não inteiro, deve informar que não é
um número inteiro'''

numero_inteiro = input('Digite um número inteiro positivo: ')
if numero_inteiro.isdigit():
    numero_inteiro = int(numero_inteiro)
    if numero_inteiro % 2 == 0:
        print(f'{numero_inteiro} é par!')
    else:
        print(f'{numero_inteiro} é ímpar')
else:
    print('ERRO: Isso não é um número inteiro!')

