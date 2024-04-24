'''Faça um programa em Python que imprima todos os números primos de um intervalo informado
pelo usuário. Utilize o método do exercício 4 para verificar se o número é primo ou não'''


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

'''
def isPrimo(n):
    if -1 <= n <= 1:
        return False
    for div in range(2, n//2+1):
        if n % div == 0:
            return False
    return True

print('Informe o intervalo para saber os números primos')
ini = int(input('Início >> '))
fim = int(input('Final  >> '))
if fim < ini:
    ini, fim = fim, ini
print(f'Lista13 de números primos entre {ini} e {fim}')
for num in range(ini, fim+1):
    if isPrimo(num):
        print(num)'''

intervalo = input("Informe o inicio e fim do intervalo (inicio fim): ").split()
inicio = int(intervalo[0])
fim = int(intervalo[1])

for i in range(inicio, fim+1):
    if primo(i) == "True":
        print(i)