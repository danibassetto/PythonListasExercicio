'''
Faça um programa em Python que gere 10 elementos aleatórios (entre 1 e 50) e peça um número ao usuário.
Verifique se este número pertence ou não ao vetor. Imprima o vetor e a mensagem de número encontrado ou não.
'''

import random

n = int(input("Informe um número: "))


L = [0] * 10
for i in range(10):
    L[i] = random.randint(1,50)
print("L =",L)

if n in L:
    print(f"{n} está na lista!")
else:
    print(f"{n} não está na lista!")

'''
OU

achou = False
for i in range(10):
    if L[i] == n:
        print(f'O número {n} está na lista')
        achou = True
        break
if not achou:
    print(f"O número {n} não está na lista")
    
OU

val = 0
for i in L:
    if i == n:
        print("Número encontrado!")
        val = 1
        break
if val != 1:
    print("Número não encontrado")
'''