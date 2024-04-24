'''
Formatando valores com modificadores

:s - Texto (strings)
:d - Inteiros (int)
:f - Números de ponto flutuante (float)
:.(NÚMERO)f - Quantidade de casas decimais (float)
:(CARACTERE)(> ou < ou ^) (QUANTIDADE)(TIPO - s, d ou f)

> - Esquerda
< - Direita
^ - Centro
'''

num_1 = 10
num_2 = 3
div = num_1 / num_2
print('{:.2f}'.format(div))
print(f'{div:.2f}')

nome = 'Dani'
print(f'{nome:s}')

num_10 = 1
print(f'{num_10:0>10}')
num_3 = 1150
print(f'{num_3:0<10}')
print(f'{num_3:0>10.2f}')  # Conta o ponto e as casas decimais
print(f'{num_3:.2f}')

nome = 'Danielle Bassetto'
print((50 - len(nome)))  # Número de # que ele vai adicionar (pois subtrai o número de caracteres do nome)
print(f'{nome:#^50}')

nome_formatado = '{:@>20}'.format(nome)
print(nome_formatado)

print(nome.lower())  # Tudo minúsculo
print(nome.upper())  # Tudo maiúsculo
print(nome.title())  # Primeiras letras maiusculas

