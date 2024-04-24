'''
Parâmetro é uma variável declarada no cabeçalho da função e tem uso exclusivo dentro do bloco de instrução da mesma.
A definição dos parâmetros que uma função deve receber obriga o envio dos valores todas as vezes em que a mesma for
invocada, do contrário, a função não é invocada.

Nomeando parâmetros
Quando especificamos o nome do parâmetro, podemos passa-los em qualquer ordem, caso contrário os parâmetros devem ser
passados na mesma ordem em que foram definidos.


'''


def soma(a, b):
    print(a + b)


soma(2, 9)
soma(7, 8)
soma(10, 15)


def retangulo(largura, altura, caractere="*"):
    linha = caractere * largura
    for i in range(altura):
        print(linha)


retangulo(3, 4)
retangulo(altura=5, largura=6)
