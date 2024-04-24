'''Faça um programa que leia uma palavra e some 1 no valor ASCII de cada caractere da palavra.
Imprima a string resultante '''

palavra = input("Informe uma palavra: ")
l = list(palavra)

for i in l:
    print(f'{chr(ord(i) +1)}', end='')

'''
palavra = input("Entre com a palavra >> ")
palavraR = ''
for letra in palavra:
    palavraR += chr(ord(letra) + 1)
print(palavraR)
'''