'''
map() é uma função que serve para aplicarmos uma função a cada elemento de uma lista, retornando uma nova lista contendo
os elementos resultantes da aplicação da função.

Ao chamar a função map(math.sqrt, lista1), estamos solicitando ao interpretador para que execute a função
math.sqrt, usando como entrada cada um dos elementos de lista1, e inserindo o resultado na lista retornada
como resultado da função map().

É uma forma bem interessante e expressiva de denotar a aplicação de uma função a cada elemento de uma lista
(ou sequência). Mas, podemos facilmente substituir uma chamada a map() por
list comprehensions. O código recém listado poderia ser substituído por:

map retorna um objeto mas podemos converter novamente em lista com list(map())
'''

import math
lista1 = [1, 4, 9, 16, 25]
lista2 = list(map(math.sqrt, lista1))
print(lista2)

lista1 = [1, 4, 9, 16, 25]
lista2 = [math.sqrt(x) for x in lista1]
print(lista2)

'''
Uma função builtin de Python é uma função que é implementada diretamente no interpretador Python, podendo ser utilizada
sem a importação de um módulo específico.

map() é uma função builtin

reduce() é outra função builtin do Python (deixou de ser builtin e passou a estar disponível no módulo functools a 
partir da versão 3), que foi retirada do conjunto de builtins de Python, em parte devido à obscuridade que pode acabar
gerando.

Devido a fácil substituição de filter por list comprehensions, filter() também já esteve na mira para ser retirada do
conjunto de builtins, embora tenha acabado permanecendo.
'''