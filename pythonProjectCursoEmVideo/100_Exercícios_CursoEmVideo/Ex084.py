'''Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves. '''

lista = []
prin = []
maior = menor = 0
while True:
    lista.append(str(input("Nome: ")))
    lista.append(float(input("Peso: ")))
    if len(prin) == 0:
        maior = menor = lista[1]
    else:
        if lista[1] > maior:
            maior = lista[1]
        if lista[1] < menor:
            menor = lista[1]
    prin.append(lista[:])
    lista.clear()
    resp = str(input("Deseja continuar? [S/N] "))
    if resp in "Nn":
        break

print("Os dados foram:", prin)
print(f"Ao todo você cadastrou {len(prin)} pessoas.")
print(f"Maior peso =", maior, "Kg: ", end='')
for p in prin:
    if p[1] == maior:
        print(f"{p[0]}", end=' ')
print()

print(f"Menor peso =", menor, "Kg: ", end='')
for p in prin:
    if p[1] == menor:
        print(f"{p[0]}", end=' ')
print()

