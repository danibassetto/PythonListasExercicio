'''
Listas em Python
fatiamento
append, insert, pop, del, clear, extend, +
min, max
range
'''

#         0    1         2    3    4    5
lista = ['A', 'Bacana', 'C', 'D', 'E', 10.5]
#         -6      -5   -4   -3   -2   -1

string = 'ABCDE'
print(string[1])
print(lista[-1])
print(lista[0:6:2])
print()

lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
lista3 = lista1 + lista2
print(lista3)

print()

# OU função extend
lista1.extend(lista2)
print(lista1)
print(lista2)
lista1.extend('a')
print((lista1))

# append insere um valor no final da lista
lista2.append('b')
print(lista2)

# insert insere em qualquer indice
lista2.insert(0, 'banana')
print(lista2)

# pop remove o ultimo valor
lista2.pop()
print(lista2)

#         0  1  2  3  4  5  6  7  8
# del = deleta
lista4 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(lista4)
del(lista4[3:5])
print(lista4)

# max mostra o maior número e min o menor
print(max(lista4))
print(min(lista4))