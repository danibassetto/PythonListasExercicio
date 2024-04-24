'''
Valores mínimos, máximos e soma
O Python oferece as funções min(), max() e sum(), através das quais é possível encontrar, respectivamente,
o menor valor, o maior valor ou ainda realizar a soma de todos os elementos da lista.

'''

L = [1,2,3,4,5]
print("Menor número:",min(L))
print("Maior número:",max(L))
print("Soma dos números:",sum(L))


'''
O método append() tem por objetivo adicionar um novo elemento no final da lista.

'''
L = [1,2,3,4,5]
print(L)
L.append(6)
print(L)

''' 
Outra forma de adicionarmos a uma lista é com adição de listas usando +.
'''

L = [1,2,3,4,5]
print(L)
L = L + [6]
print(L)
L += [7]
print(L)
L += [8,9,10]
print(L)

'''
O método extend() adiciona os elementos de uma lista a outra. O método extend() sequer aceita parâmetros que não 
sejam listas.

Se você utilizar o método append() com uma lista como parâmetro, em vez de adicionar os elementos no fim da lista, 
append adicionará a lista inteira, mas como apenas um novo elemento. Teremos então listas dentro de listas.

'''

L = [1,2,3,4,5]
print(L)
L.append(6)
L.extend([7])
L.append([8,9])
L.extend([10,11])
print(L)

'''
Caso desejemos fazer uma inserção em uma posição específica, podemos utilizar o método insert() que, além do elemento a
ser inserido, recebe também o índice que ele deve assumir.
'''

L = [1,2,3,4,5]
print(L)
L.insert(0,6)
print(L)


