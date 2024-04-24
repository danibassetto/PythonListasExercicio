# Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.

contador = 0
soma_pares = 0
for i in range(1, 7):
    num = int(input("Digite um valor: "))
    if num % 2 == 0:
        soma_pares += num
        contador += 1
print(f"Você informou {contador} números pares e a soma foi {soma_pares}")
