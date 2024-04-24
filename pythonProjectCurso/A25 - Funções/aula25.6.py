'''
Funções (def) em Python - *args **kwargs - Aula 16 (parte 3)

def func(a1, a2, a3, a4, a5, nome=None, a6=None):  # todos depois do parâmetro nomeado, devem também ser nomeado, assim como na chamada da função
	print(a1, a2, a3, a4, a5, nome, a6)
	return nome, a6

var = func(1,2,3,4,5, nome='Dani', a6='5')
print(var[0], var[1])
'''


def func(*args):  # quando não sei quantos parâmetros irá informar, lembrando que não conseguimos alterar tupla, para alterar tem que converter em lista
    print(args)
    print(args[0])
    print(args[-1])
    print(len(args))


func(1, 2, 3, 4, 5)


def teste(*args):
    print(args)


lista = [1, 2, 3, 4, 5]
teste(*lista, 10, 20, 30, 40, 50)


def teste2(*args, **kwargs):  # kwargs é para parâmetros nomeados (key words arguments)
    print(args)
    print(kwargs)
    print(kwargs['nome'], kwargs['sobrenome'])

    idade = kwargs.get(
        'idade')  # metodo para verificar se foi inserido tal parâmetro, do modo acima ao inserir ele da erro.
    if idade is not None:
        print(idade)


lista = [1, 2, 3, 4, 5]
lista2 = [10, 20, 30, 40, 50]
func(*lista, *lista2, nome='Dani', sobrenome='Bassetto')  # note que no args não printa os parâmetros nomeados
