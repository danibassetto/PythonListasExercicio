''' Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra “A”, em que posição ela
aparece a primeira vez e em que posição ela aparece a última vez.'''

frase = str(input("Digite uma frase: ")).lower().strip()
print(f"A letra A aparece {frase.count('a')} vezes")
print(f"A primeira letra A aparece na posição {frase.find('a') + 1}")
print(f"A última letra A aparece na posição {frase.rfind('a') + 1}")