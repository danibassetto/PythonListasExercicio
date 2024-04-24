# Faça um programa em Python que leia uma frase e imprima quantas vogais tem esta frase. Considerar minúscula e maiúscula.

frase = input("Informe uma frase: ")
l = list(frase)

count = 0
for i in range(len(l)):
    if l[i] in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:
        count += 1

frasej = ''.join(frase)
print(f"A frase '{frasej}' possui {count} vogais!")

'''
from unidecode import unidecode

frase = input('Entre com uma frase >> ').upper()
c = 0
for v in 'AEIOU':
    c += unidecode(frase).count(v)
print(f'Quantidade de vogais >> {c}')
'''
