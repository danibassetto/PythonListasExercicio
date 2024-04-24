'''
Funções (def) em Python - global e local - Aula 16 (parte 4)
'''

variavel = 'valor'


def func():
    print(variavel)


def func2():
    global variavel
    variavel = 'Outro valor'
    print(variavel)


func()
func2()

print(variavel)

'''
variavl = 'valor'

def func():
	print(variavel)
	variavel = 1234  # erro pois ele aponta que você está tentando utilizar antes de configurá-la
	print(variavel)

func()

# tudo que estiver dentro de uma função só é reconhecido fora dela se estiver como variável global
'''
