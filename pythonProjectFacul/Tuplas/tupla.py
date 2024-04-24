'''
Tuplas podem ser vistas como listas em Python, com a grande diferença de serem imutáveis. Tuplas são ideias para
representar listas de valores constantes e para realizar operações de empacotamento e desempacotamento de valores.
Para criar uma tupla em Python, podemos fazer assim:
				T = ( )
				X = ("a","b","c")
A tupla T é uma tupla vazia e a tupla X foi criada com três elementos.

Tuplas são criadas de forma semelhante às listas, mas utilizamos parênteses em vez de colchetes.
Os parênteses são opcionais, porém sua utilização aumenta a clareza da expressão em si.

'''

T = ()
print(T)
T = ("a","b","c")
print(T)
T = 1,2,3
print(T)

'''
Sintaticamente, uma tupla é uma lista de valores separados por vírgulas:

t = 'a', 'b', 'c', 'd', 'e' 

Embora não seja sempre necessário, é comum colocar tuplas entre parênteses:

t = ('a', 'b', 'c', 'd', 'e') 

Outra forma de criar uma tupla é com a função integrada tuple. Sem argumentos, cria uma tupla vazia:

t = tuple()

Se os argumentos forem uma sequência (string, lista ou tupla), o resultado é uma tupla com os elementos da sequência:

>>> t = tuple('lupins') 
>>> t 
('l', 'u', 'p', 'i', 'n', 's') 

Criando tuplas com apenas 1 elemento

'''

T = (1)
print(T)
T = (1,)
print(T)
T = 1,
print(T)

'''
Tuplas também podem ser criadas a partir de listas, utilizando-se a função tuple:
'''

L = [1,2,3]
print(L)
T = tuple(L)
print(T)

'''
Se uma tupla contiver uma lista ou outro objeto que pode ser alterado, este continuará a funcionar normalmente.

'''

T = ("a",["b","c","d"])
print(T)
print(len(T))
print(T[1])
T[1].append("e")
print(T)
print(len(T))

'''
Tuplas suportam a maior parte das operações de lista, como fatiamento e indexação:

'''

T = ("a","b","c")
print(T)
print(T[0])
print(T[1:])
T = T*2
print(T)
print(len(T))

'''
Como tuplas são imutáveis, você não pode alterar os elementos, mas pode substituir uma tupla por outra:

>>> t = 'a', 'b', 'c', 'd', 'e' 
>>> t = ('A',) + t[1:]
>>> t 
('A', 'b', 'c', 'd', 'e') 

Essa instrução faz uma nova tupla e então a atribui a t.

Os operadores relacionais funcionam com tuplas e outras sequências; o Python começa comparando o primeiro elemento de 
cada sequência. Se forem iguais, vai para os próximos elementos, e assim por diante, até que encontre elementos que 
sejam diferentes. Os elementos subsequentes não são considerados (mesmo se forem muito grandes).

>>> (0, 1, 2) < (0, 3, 4) 
True 
>>> (0, 1, 2000000) < (0, 3, 4) 
True 
'''

'''
Tuplas como valores de retorno

Falando estritamente, uma função só pode retornar um valor, mas se o valor for uma tupla, o efeito é o mesmo que 
retornar valores múltiplos. Por exemplo, se você quiser dividir dois números inteiros e calcular o quociente e resto, 
não é eficiente calcular x/y e depois x%y. É melhor calcular ambos ao mesmo tempo.

A função integrada divmod toma dois argumentos e devolve uma tupla de dois valores: o quociente e o resto. Você pode 
guardar o resultado como uma tupla:

>>> t = divmod(7, 3) 
>>> t 
(2, 1) 

Ou usar a atribuição de tuplas para guardar os elementos separadamente:
>>> quot, rem = divmod(7, 3) 
>>> quot 
2 
>>> 
rem 1 

'''

'''
Tuplas com argumentos de comprimento variável

As funções podem receber um número variável de argumentos. Um nome de parâmetro que comece com * reúne vários 
argumentos em uma tupla. Por exemplo, printall recebe qualquer número de argumentos e os exibe:

def printall(*args):  
    print(args) 

O parâmetro com o prefixo * pode ter qualquer nome que você goste, mas args é o convencional. É assim que a função 
funciona:

>>> printall(1, 2.0, '3') 
(1, 2.0, '3') 

'''

'''
Tuplas com argumentos de comprimento variável
O complemento de reunir é espalhar. Se você tiver uma sequência de valores e quiser passá-la a uma função como 
argumentos múltiplos, pode usar o operador *. Por exemplo, o divmod recebe exatamente dois argumentos; ele não funciona
com uma tupla:

>>> t = (7, 3) 
>>> divmod(t) 
TypeError:expected 2 arguments, got 1 

No entanto, se você espalhar a tupla, aí funciona:

>>> divmod(*t)
(2, 1) 

Tuplas com argumentos de comprimento variável
Muitas das funções integradas usam tuplas com argumentos de comprimento variável. Por exemplo, max e min podem receber
qualquer número de argumentos:

>>> max(1, 2, 3) 
3 

Mas sum não:
>>> sum(1, 2, 3) 
TypeError:expected at most 2 arguments, got 3 

'''