'''Escreva um programa em Python que contenha uma função que retorne True caso o argumento
passado seja primo e False caso contrário. O argumento será sempre um valor inteiro. Peça um
número, chame o método e imprima se o mesmo é número primo ou não.'''


def primo(n):
    nprimo = True
    if -1 <= n <= 1:
        nprimo = False
    else:
        for div in range(2, n // 2 + 1):
            if n % div == 0:
                nprimo = False
                break
    if nprimo:
        return "True"
    else:
        return "False"


n = int(input("Informe um número: "))
print(f"Primo: {primo(n)}")

'''
def isPrimo(n):
    if -1 <= n <= 1:
        return False
    for div in range(2, n//2+1):
        if n % div == 0:
            return False
    return True

numero = int(input('Digite um número >> '))
if isPrimo(numero):
    print(f'{numero} é primo')
else:
    print(f'{numero} não é primo')
'''