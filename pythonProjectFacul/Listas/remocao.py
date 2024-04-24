'''
A instrução del é utilizada para remover elementos da lista.
'''

L = [1,2,3,4,5]
print(L)
del L[0]
print(L)

'''
Podemos também apagar fatias inteiras de uma só vez.
'''

L = list(range(11))
print(L)
del L[1:9]
print(L)

'''
Um método importante é o pop(), que remove um item (de uma determinada posição) da lista e o retorna como resultado da
operação. Se não passar a posição, o padrão é remover o útlimo elemento.

'''

L = [1,2,3,4,5]
print(L)
n=L.pop()
print(L)
print("Número removido: ",n)

'''
Temos também o método remove(), que remove o item a partir do seu valor
'''

L = [1,2,3,4,5]
print(L)
L.remove(5)
print(L)

'''
O método clear() remove todos os itens da lista.
'''

L = [1,2,3,4,5]
print(L)
L.clear()
print(L)

