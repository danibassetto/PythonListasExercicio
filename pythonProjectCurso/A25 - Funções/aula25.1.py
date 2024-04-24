'''
Funções (def) em Python - return - Aula 16 (Parte 2)
'''
def funcao(var):
	print(var)

variavel = funcao('Valor que eu quero')
print(variavel)  # sem o return ele printa none, que quer dizer que não há valor

if variavel:
	print(variavel)
else:
	print('Nenhum valor')



def funcao(var):
    return var


if variavel:
    print(variavel)  # retorna o valor de return
else:
    print('Nenhum valor')

# irá executar a função até o return, se tiver código na função abaixo do return ele não executa, como se fosse um break

'''
def divisao(n1, n2):
	if n2 > 0:
		return n1 / n2
'''


def divisao(n1, n2):
    if n2 == 0:
        return  # volta como none

    return n1 / n2


divide = divisao(8, 2)

if divide:
    print(divide)
else:
    print("Conta inválida")


# pode retornar vários tipos

def dumb():
    return 1


print(dumb(), type(dumb()))


# função retornando função

def f(var):
    print(var)


def dumb():
    return f  # está retornando a função sem executá-la


var = dumb()('Colocar o valor que deseja aqui')

var = dumb()  # var virou uma função, igual a f

''' 
def dumb():
	return('Dani', 'Bassetto')  # return recebendo tupla

var = dumb()
print(var[1], var[2]) 
'''
