'''
O objetivo de toda função é o processamento de alguma informação e o retorno do dado processado. Desta forma, temos
que toda função pode, por definição, retornar valores.

A palavra-chave return é utilizada para declarar a informação a ser retornada pela função. A mesma funciona também
para finalizar a execução do bloco de instrução da função, retornado assim, o valor que estiver a sua frente. Então, a
instrução return é utilizada tanto para o retorno de valores pelas funções, como também, para finalizar a execução
da função
'''


def soma(a, b):
    return a + b


print(soma(2, 9))
print(soma(7, 8))
print(soma(10, 15))
