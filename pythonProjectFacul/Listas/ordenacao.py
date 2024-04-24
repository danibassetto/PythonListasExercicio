'''
O método sort(), ordena a lista, ela será feita em ordem crescente para números e em ordem lexicográfica para strings,
ou seja, na forma como são ordenadas no dicionário
'''

L = [5,3,1,2,4]
print(L)
L.sort()
print(L)

'''
O método reverse() inverte a ordem dos elementos.
'''

L = [5,3,1,2,4]
print(L)
L.reverse()
print(L)

'''
O método count() retorna o número de ocorrências de determinado objeto, passado como parâmetro, em uma lista.
'''

L = [1,2,3,4,5,1,2,1]
print(L)
print(L.count(1))
