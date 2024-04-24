''' Lista é um tipo de variável que permite o armazenamento de vários valores, acessados por um índice. Uma lista pode conter zero ou mais elementos de um mesmo tipo ou de tipos diversos, podendo inclusive conter outras listas. O tamanho de uma lista é igual à quantidade de elementos que ela contém.
Para criar uma lista em Python, podemos fazer assim:
				L = [ ]
				Z = [15, 8, 9]
A lista L é uma lista vazia e a lista Z foi criada com três elementos.

Formas de criar uma lista
L = [ ]
L = [0] * 5
L = [0,0,0,0,0,]
L = [1,2,3,4,5]
L = [‘a’,’b’]
L = list()

Para acessar um elemento da lista, basta utilizar a sintaxe:
<nome da Lista>[índice]
As listas são mutáveis, ou seja, é permitido alterar o conteúdo do que está armazenado em cada posição da lista.

'''

L = []
print(L)
L = [0]*5
print(L)
L = [1,2,3,4,5]
print(L)
L = list()
print(L)
num = "456"
L = list(num)
print(L)

'''
Saídas
[]
[0, 0, 0, 0, 0]
[1, 2, 3, 4, 5]
[]
['4', '5', '6']
'''

Z = [15, 8, 9]
print(Z[0])
Z[0] = 7
print(Z[0])
