'''
List Comprehension é uma forma concisa de criar e manipular listas.
[expr for item in lista]

'''

L = []
for item in range(5):
    L.append(item)
    print(L)

#ou

L = [item for item in range(5)]
print(L)

'''
List Comprehensions com if, vários if’s e if .. else
'''

L = [numero for numero in range(20) if numero % 2 == 0]
print(L)
L = [numero for numero in range(100) if numero % 5 == 0 if numero % 6 == 0]
print(L)
L = [1 if numero % 5 == 0 else 0 for numero in range(11)]
print(L)

'''
List Comprehensions (Utilizando conversão)
'''

entrada = "12345"
L = list(entrada)
print(L)
L = [int(elem) for elem in L]
print(L)
