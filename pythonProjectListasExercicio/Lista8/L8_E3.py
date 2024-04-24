''' Faça um programa em Python que leia uma String e um caractere. Informe a quantidade de
vezes que o caractere aparece na string (podendo ser maiúscula ou minúscula)'''

string = input("Informe uma string: ")
caractere = input("Informe um caractere: ")

print(f"A string '{string}' possui {string.count(caractere)} caracteres '{caractere}'")


'''
texto = input("Texto >> ").upper()
carac = input("Caractere a ser localizado >> ").upper()[0]
print(f'Há {texto.count(carac)} caracteres "{carac}" no texto')
'''