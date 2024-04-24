''' programa que gere um conjunto de 20 números inteiros aleatórios entre 1 e 50 e mostre
qual foi o maior e o menor '''

import random
cont = 1
maior = 0
menor = 51
while cont <= 20:
    n = random.randint(1,50)
    print(n)
    if n > maior:
        maior = n
    if menor > n:
        menor = n
    cont += 1
print(f'Maior: {maior}\nMenor: {menor}')