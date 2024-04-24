'''
GRUPO 11 - TRABALHO 03
Danielle Barros Bassetto RA: 629391
Cesar Augusto de Almeida  RA: 626848
João Vítor Adonis  RA: 590428
'''

num_jornalistas = int(input())
pont = [6,4,3,2,1]
voto = {}
for i in range(num_jornalistas):
    for j in range(5):
        nome = input()
        voto[nome] = voto.get(nome,0) + pont[j]
    print()

for chave in sorted(voto, key=voto.get,reverse=True):
    print(f'{chave}: {voto[chave]}')