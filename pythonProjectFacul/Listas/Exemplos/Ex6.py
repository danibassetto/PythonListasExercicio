from random import randint
L = []
for i in range(10):
    L.append(randint(1,20))
print(L)
x = randint(1,20)
print(f'Há {L.count(x)} números {x} na lista')
if x in L:
    print(f'A posição na lista do 1º número {x} é {L.index(x)}')