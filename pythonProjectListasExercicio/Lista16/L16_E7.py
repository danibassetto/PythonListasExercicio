'''
Escreva um programa em Python com uma função que receba uma string por parâmetro e retorne
a string com o caractere ”#” no início, no meio e no final dela. Por exemplo, se a entrada for ”abcd”,
o retorno deve ser ”#ab#cd#”. Outro exemplo: se receber ”abcde”, a função deve retornar
”#ab#cde#
No programa principal, peça a string e chame a função e imprima a strings alterada
'''


def insereHashTag(string):
    meio = len(string) // 2
    return '#' + string[:meio] + '#' + string[meio:] + '#'


# Outra forma
def insereCE(string):
    meio = len(string) // 2 + 1
    lista = list(string)
    lista.insert(0, '#')
    lista.insert(meio, '#')
    lista.append('#')
    string = ''.join(lista)
    return string


palavra = input('Informe uma palavra >> ')
print(f'Palavra com # >> {insereCE(palavra)}')
