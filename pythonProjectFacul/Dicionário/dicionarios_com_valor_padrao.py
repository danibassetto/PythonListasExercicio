'''
Dicionários com valor padrão
Uma operação muito comum com dicionários é a de recuperar o valor de uma chave e, caso não exista, utilizar um valor
padrão. Vejamos um exemplo em que utilizaremos um dicionário para contar o número de ocorrências de uma letra em uma
string.
'''

d = {}
for letra in "abracadabra":
    if letra in d:
        d[letra] = d[letra] + 1
    else:
        d[letra] = 1
print(d)

'''
Simplificando o código anterior, utilizando o método get().
'''

d = {}
for letra in "abracadabra":
    d[letra] = d.get(letra,0) + 1
print(d)
