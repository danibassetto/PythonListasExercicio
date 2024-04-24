# Limite para pegar empréstimo

nome = input('Qual o seu nome? ')
idade = int(input('Qual sua idade? '))
idade_limite = 18

if idade >= idade_limite:
    print(f'{nome} pode pegar o empréstimo')
else:
    print(f'{nome} NÃO pode pegar o empréstimo')