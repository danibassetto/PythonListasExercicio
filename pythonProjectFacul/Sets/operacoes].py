'''
Para a diferença entre conjuntos, utiliza-se o operador –, para a união utiliza-se o operador | e para a interseção
utiliza-se o operador &.
'''

A = {1,2,3,4,5}
B = {2,3}
C = {3,4,5,6,7}
print("A -> ",A)
print("B -> ",B)
print("C -> ",C)
print("A - B -> ",A-B)
print("A + C -> ",A|C)
print("A ∩ B -> ",A&C)

'''
Conjuntos também possuem outras propriedades, como tamanho, que pode ser obtido com o uso da função len
'''

C = {1,2,3,4,5}
print(C)
print(len(C))
