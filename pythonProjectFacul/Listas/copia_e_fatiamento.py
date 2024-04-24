'''
Podemos copiar listas, mas cuidado, uma lista em Python é um objeto e, quando atribuímos um objeto a outro, estamos
apenas copiando a mesma referência da lista, e não seus dados em si.
'''

L = [1,2,3,4,5]
V = L
print("L -> ",L)
print("V -> ",V)
V[0] = 6
print("L -> ",L)
print("V -> ",V)

'''
Para criar uma cópia independente de uma lista, devemos usar L[:], assim estaremos nos referindo a uma nova cópia de L. 
L e V se referem a áreas diferentes na memória.
'''

L = [1,2,3,4,5]
V = L[:]
print("L -> ",L)
print("V -> ",V)
V[0] = 6
print("L -> ",L)
print("V -> ",V)

'''
Podemos fatiar uma lista, veja alguns exemplos:
'''

L = [1,2,3,4,5]
print("L -> ",L[0:5])
print("L -> ",L[:5])
print("L -> ",L[:-1])
print("L -> ",L[1:3])
print("L -> ",L[1:4])
print("L -> ",L[3:])
print("L -> ",L[:3])
print("L -> ",L[-1])
print("L -> ",L[-2])

'''
Saídas

L ->  [1, 2, 3, 4, 5]
L ->  [1, 2, 3, 4, 5]
L ->  [1, 2, 3, 4]
L ->  [2, 3]
L ->  [2, 3, 4]
L ->  [4, 5]
L ->  [1, 2, 3]
L ->  5
L ->  4]

'''

'''
Tamanho da lista:
Podemos usar a função len com listas. O valor retornado é igual ao números de elementos da lista.
'''

L = [1,2,3,4,5]
print(len(L))
