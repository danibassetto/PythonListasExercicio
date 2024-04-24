'''
Elabore  um  programa  que  calcule  N!  (fatorial  de  N),  sendo  que  o  valor  inteiro  de
N  é fornecido pelo usuário.
'''

n = int(input('Informe o número que deseja exibir o fatorial: '))

cont = 1
fat = 1

while cont <= n:
    fat *= cont
    cont += 1
print(f'Fatorial de {n}: {fat}')