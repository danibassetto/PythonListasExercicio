# Expressão condicional OR com booleans

nome = input('Qual seu nome? ')

'''
if nome:
    print(nome)
else:
    print('Você não digitou nada =(')
'''

print(nome or 'Você não digitou nada!')

a = 0
b = None
c = False
d = []
e = {}
f = 22
g = 'Luiz'

variavel = a or b or c or d or e or f or g
print(variavel)  # printa 22 pois é a primeira verdadeira, as de cima retornam falso!

'''
if a: 
    variavel = a
elif b:
    variavel = b
...
'''
