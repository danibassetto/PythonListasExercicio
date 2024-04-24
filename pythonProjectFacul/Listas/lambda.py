'''
No exemplo da função filter(), tivemos que definir uma nova função (chamada maior_que_zero) para usar somente dentro da
função filter(), sendo chamada uma vez para cada elemento. Ao invés de definir uma nova função dessa forma, poderíamos
definir uma função válida somente enquanto durar a execução do filter. Não é necessário nem dar um nome a tal função,
sendo portanto chamada de função anônima ou função lambda. Considere o exemplo abaixo:
'''

valores = [10, 4, -1, 3, 5, -9, -11]
print(list(filter(lambda x: x > 0, valores)))

'''
Definimos uma função anônima (portanto, não tem nome), que recebe uma entrada (a variável x) e retorna o resultado da 
operação x > 0, True ou False.

Poderíamos também usar uma função lambda no exemplo da função reduce():
'''

from functools import reduce
valores = [1, 2, 3, 4, 5]
soma = reduce(lambda x, y: x + y, valores)
print (soma)

'''
No código acima, definimos uma função anônima que recebe duas entradas e retorna a soma dessas entradas.
'''
