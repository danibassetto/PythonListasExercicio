'''
Desempacotamento de listas
'''

lista = ['Luiz', 'João','Maria',1,2,3,4,5,6,7,9,100]

n1, n2, *outralista, ultimo = lista  # o *outralista coloca o restante dos elementos em outra lista
print(n1, n2, outralista, ultimo)
