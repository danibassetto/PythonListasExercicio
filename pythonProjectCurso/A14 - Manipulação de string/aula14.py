'''
Manipulando strings
* String indices
* Fatiamento de strings [inicio:fim:passo]
* Funções built-in len, abs, type, print etc...
Essas funções podem ser usadas diretamente em cada tipo.

https://docs.python.org/3/library/stdtypes.html (tipos built-in)
https://docs.python.org/3/library/functions.html (funções built-in)
'''

# positivos       [012345678]
texto         =   'Python_s2'
# negativos      -[987654321]

print(texto[2])
print(texto[8])
print(texto[6])

url = 'www.google.com.br/'
print(url[:-1])

nova_string = texto[0:5]  # Inicio:fim (não aparece o ultimo, por isso tem que por um a mais)
# vai do 0 ao 4
print(nova_string)

nova_string1 = texto[-9:-3]
print(nova_string1)

nova_string2 = texto[0:6:2]
print(nova_string2)

nova_string3 = texto[0::3]
print(nova_string3)

nova_string4 = texto[:]
print(nova_string4)

print(len(texto))
