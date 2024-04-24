'''Fazer um programa em Python para verificar se uma determinada String é palíndromo.
Exs.: ANA - MUSSUM – OVO'''

string = input("Informe uma string: ")
p = string[::-1]
if string == p:
    print("É palindromo!")
else:
    print("Não é palindromo!")

'''
palavra = input('Palavra >> ')
print(f'Palavra informada >> {palavra}')
print(f'Palavra invertida >> {palavra[::-1]}')
if palavra == palavra[::-1]:
    print('É palíndromo')
else:
    print('Não é palíndromo')
'''