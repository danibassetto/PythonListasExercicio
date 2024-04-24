''' Exercício Python 22: Crie um programa que leia o nome completo de uma pessoa e mostre:

– O nome com todas as letras maiúsculas e minúsculas.

– Quantas letras ao todo (sem considerar espaços).

– Quantas letras tem o primeiro nome. '''

nome = str(input("Insira seu nome: ")).strip()
print("Analisando seu nome...")
print(f"Nome em maiúsculo: {nome.upper()}")
print(f"Nome em minúsculo: {nome.lower()}")
print(f"Quantidade de letras: {len(nome) - nome.count(' ')}")

if (nome.find(' ')) == -1:
    print(f"Esse é seu primeiro nome?")
else:
    print(f"Seu primeiro nome tem {nome.find(' ')} letras")
# OU
separa = nome.split()
print(f"Seu primeiro nome é: {separa[0]} e tem {len(separa[0])} letras")