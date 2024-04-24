'''
Faça um programa em Python que gere 10 elementos aleatórios (entre 1 e 50) armazenando em uma lista e uma opção.
Se a opção for 1, mostrar o vetor na ordem direta, se a opção for 2, mostrar o vetor na ordem inversa.
'''
import random

L = [0] * 10
for i in range(10):
    L[i] = random.randint(1,50)
print("L =",L)

opcao = int(input("Digite '1' para mostrar o vetor em ordem direta e '2' para mostrar o vetor na ordem indireta: "))

if opcao == 1:
    print(L)
elif opcao == 2:
    L.reverse()
    print(L)

    '''
    OU
    L2 = L[::-1]
    print(L2)
    '''
