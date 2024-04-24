'''Escreva uma função que retorne o maior de dois números, recebidos por parâmetro.'''

def maior(a,b):
    if a>b:
        return a
    return b

x = int(input())
y = int(input())
print("O maior número entre {} e {} é {}".format(x,y,maior(x,y)))
