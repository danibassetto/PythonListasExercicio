'''
Split, Join, Enumerate em Python
* Split - dividir uma str # str
* Join - JUnta uma lista # str
* Enumerate - enumera elementos da lista # iteráveis
'''

# Split
string = "O Brasil é o país do futebol, o Brasil é penta."
lista1 = string.split(' ')  # separa por espaço
print(lista1)

lista2 = string.split(',')  # separa por vírgula
print(lista2)

for valor in lista1:
    print(f"A palavra {valor} apareceu {lista1.count(valor)}X na frase")

# O que eu colocar entre as aspas do split é o critério que irá dividir a str

palavra = ''
contagem  = 0
for valor in lista1:
    qtd_vezes = lista1.count(valor)
    if qtd_vezes > contagem:
        contagem = qtd_vezes
        palavra = valor
print(f"A palavra que apareceu mais vezes é {palavra} ({contagem}X)")

# Join
lista3 = ["Testando","o","join"]
string2 = ' '.join(lista3)  # o que eu coloco entre as aspas irá separar os termos
print(string2)
# OU
print(''.join(lista3))

# Enumeate

string = 'O Brasil é penta.'
lista = string.split(" ")

for indice, valor in enumerate(lista):
    print(indice,valor)

