''' Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor
valor digitado e as suas respectivas posições na lista. '''

lista = []
maior = menor = 0
for c in range(0,5):
    lista.append(int(input(f"Digite um valor para a posição {c}: ")))
    if c == 0:
        menor = maior = lista[c]
    else:
        if lista[c] > maior:
            maior = lista[c]
        if lista[c] < menor:
            menor = lista[c]

print("Lista =", lista)

print("Maior valor =", maior, "digitado na(s) posição(es)", end=' ')
for i, v in enumerate(lista):
    if v == maior:
        print(f"{i}", end='...')

print("\nMenor valor =", menor, "digitado na(s) posição(es)", end=' ')
for i, v in enumerate(lista):
    if v == menor:
        print(f"{i}", end='...')