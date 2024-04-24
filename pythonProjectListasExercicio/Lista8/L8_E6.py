'''Escreva um programa em Python que leia uma palavra fornecida pelo teclado e em seguida
escreva o caractere presente no meio da palavra, caso esta tenha um número ímpar de
caracteres e os dois do meio caso esta tenha um número par de caracteres. Como exemplo,
considere a palavra SONHO. O caractere a ser impresso será o N'''

palavra = input("Informe uma palavra: ").upper()
l = list(palavra)

if len(palavra) % 2 == 0:
    print(f'{l[len(palavra) // 2 - 1]}{l[len(palavra) // 2]}')
else:
    print(f'{l[len(palavra) // 2]}')

'''
palavra = input('Informe a palavra >> ').upper()
tam = len(palavra)
if tam % 2 == 1:
    print(palavra[tam//2])
else:
    print(palavra[tam//2-1], palavra[tam//2], sep='')
'''