'''Faça um programa em Python que leia uma String e dois caracteres. Troque todas as ocorrências
do primeiro caractere (podendo ser maiúsculo ou minúsculo) pelo segundo e imprima a
quantidade de vezes que o caractere foi substituído'''

string = input("Informe uma string: ")
primeiro_caractere = input("Informe o primeiro caractere: ")
segundo_caractere = input("Informe o segundo caractere: ")

vezes = string.count(primeiro_caractere)
troca = string.replace(primeiro_caractere, segundo_caractere)

print(f"Frase após a troca: '{troca}'")
print(f"Número de trocas: {vezes}")


'''
texto = input("Texto >> ").upper()
old = input("Caractere a ser substituído   >> ").upper()[0]
new = input("Caractere para a substituição >> ").upper()[0]
c = texto.count(old)
texto = texto.replace(old,new)
print(f'Foram realizadas {c} substituições')
print(f'Novo texto >> {texto}')
'''