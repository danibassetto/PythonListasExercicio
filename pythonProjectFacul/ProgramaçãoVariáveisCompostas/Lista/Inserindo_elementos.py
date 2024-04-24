# Inserindo elementos na lista

# A inserção de elementos pode ser utilizando o índice desejado, nesse você substitui os 0
L = [0] * 10
for i in range(10):
    L[i] = int(input("{}° valor --> ".format(i+1)))
print(L)

# Ou utilizando a função append(), que insere o elemento passado por parâmetro (dentro dos parênteses) no final da lista.

L = []
for i in range(10):
    valor = int(input("{}° valor -> ".format(i+1)))
    L.append(valor)
print(L)

# Inserindo elementos aleatórios

from random import randint
L=[]
for i in range(5):
    L.append(randint(1,50))
print(L)
