ista = list(range(1,11))

#imprimindo a lista com print
print(lista)
print(*lista)

#imprimindo a lista usando while
i = 0
while i < len(lista):
    print(f'{lista[i]:02}',end=' ')
    i += 1
print()
#imprimindo a lista usando for
for i in range(len(lista)):
    print(f'{lista[i]:02}', end=' ')
print()
#imprimindo a lista usando for in
for n in lista:
    print(f'{n:02}', end=' ')