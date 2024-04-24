'''
Como o próprio nome já deixa claro, filter() filtra os elementos de uma sequência. O processo de filtragem é definido a
partir de uma função que o programador passa como primeiro argumento da função. Assim, filter() só “deixa passar” para
a sequência resultante aqueles elementos para os quais a chamada da função que o usuário passou retornar True. Vejamos
um exemplo:

'''


def maior_que_zero(x):
    return x > 0


valores = [10, 4, -1, 3, 5, -9, -11]
print(list(filter(maior_que_zero, valores)))

'''
No exemplo acima, filter() chamou a função maior_que_zero para cada um dos elementos contidos em
valores. Se a função retornar True, o elemento é inserido na lista de resultado. Caso contrário, não o é. Ou seja, é 
feita a filtragem e só passam aqueles elementos que são maiores que zero. Assim, como no exemplo da
função map(), aqui também podemos escrever com facilidade uma comprehension com a mesma funcionalidade:
'''

valores = [10, 4, -1, 3, 5, -9, -11]
print([x for x in valores if x > 0])

