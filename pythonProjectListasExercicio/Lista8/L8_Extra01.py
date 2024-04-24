'''Faça um programa Python que leia um nome completo e crie uma string com nome no formato de referência
Ex: Renata de Carvalho Paschoal
PASCHOAL, R. C.
'''

nome = input("Informe seu nome completo: ")

ultimonome = nome.rfind(' ') + 1
print(f'{nome[ultimonome:].upper()},', end=' ')

remover = nome[ultimonome:]

nome = nome.upper().split()

iniciais = ''
for palavra in nome:
    if palavra != remover and palavra not in ['DA', 'DE', 'DOS', "D'",'E', 'DI', 'DAS', 'DO']:
        iniciais += palavra[0]
for i in iniciais:
    print(f'{i}.', end=' ')


'''
nome = input("Informe o nome completo >> ")
ln = nome.upper().split()
referencia = ln[-1] + ', '
for n in ln[:-1]:
    if n not in ['DA', 'DE', 'DAS', 'DO', 'DOS', 'DI', 'E']:
        referencia += n[0] + '. '
print(referencia)
'''


