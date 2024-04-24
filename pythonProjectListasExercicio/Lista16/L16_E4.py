'''
Faça um programa em Python que tenha uma função que receba duas palavras e retorne True se
as duas strings são palíndromas mútuas, ou seja, se uma é igual à outra quando lida de traz para
frente e retorne False caso não sejam.
No programa principal, leia as duas strings e chame a função. Imprima se as duas strings são ou
não palíndromas mútuas.
'''


def palMutua(str1, str2):
    if str1.upper() == str2[::-1].upper():
        return True
    return False


p1 = input('Informe a 1ª palavra >> ')
p2 = input('Informe a 2ª palavra >> ')
if palMutua(p1, p2):
    print('São palíndromas mútuas')
else:
    print('Não são palíndromas mútuas')
