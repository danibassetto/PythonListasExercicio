''' Construa um programa que verifique se um número fornecido pelo usuário é primo ou não.
Fazer laço que vai de 2 a metade do número '''

n = int(input('Informe um número para saber se ele é primo: '))
primo = True
if -1 <= n <= 1:
    primo = False
else:
    for div in range(2, n//2+1):  # ou (2, n)
        if n % div == 0:
            primo = False
            break

if primo:  # ou if primo == True
    print(f'{n} é primo!')
else:
    print(f"{n} NÃO é primo!")