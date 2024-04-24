'''
For in em Python
Iterando strings com for
Função range(start=0, stop, step=1)
'''

# continue - pula para o próximo laço
# break - termina o laço (para de executar)

texto = 'Python'
nova_string = ''

for letra in texto:
    if letra == 't':
        nova_string = nova_string + letra.upper()
    elif letra == 'h':
        nova_string += letra.upper()
    else:
        nova_string += letra
print(nova_string)


'''
c = 0
while c < len(texto):
    print(texto[c])
    c += 1
'''


for n, letra in enumerate(texto):
    print(n, letra)

print()

for n in range(5, 10, 1):  # Inicio, fim e tipo de repetição
    print(n)

print()

for n in range(0, 100, 8):
    print(n)

print()

for n in range(100):
    if n % 4 == 0:
        print(n)



