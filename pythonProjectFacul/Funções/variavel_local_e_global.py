'''
Variáveis locais e globais

Quando usamos funções, começamos a trabalhar com variáveis internas ou locais e com variáveis externas ou globais. A
diferença entre elas é a visibilidade ou escopo.

Uma variável local a uma função existe apenas dentro dela, sendo normalmente inicializada a cada chamada. Assim, não
podemos acessar o valor de uma variável local fora da função que a criou e, por isso, passamos parâmetros e
retornamos valores nas funções, de forma a possibilitar a troca de dados no programa.

Se quiser modificar uma variável global dentro de uma função, deve-se informar que se está usando uma variável global
antes de inicializá-la, na primeira linha da função, utilizando a instrução global.

'''

EMPRESA = "Unidos Venceremos Ltda"


def imprime_cabecalho():
    print(EMPRESA)
    print("-" * len(EMPRESA))


imprime_cabecalho()

a = 5


def altera():
    a = 7


print("valor de a dentro da função >> {}".format(a))
print("valor de a antes de chamar a função >> {}".format(a))
altera()
print("valor de a após chamar a função >> {}".format(a))

b = 5


def altera():
    global b
    b = 7


print("valor de a dentro da função >> {}".format(b))
print("valor de a antes de chamar a função >> {}".format(b))
altera()
print("valor de a após chamar a função >> {}".format(b))
