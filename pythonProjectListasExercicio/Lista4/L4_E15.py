'''''
Crie um programa em que peça um número inteiro ao usuário, e imprima a seguinte tabela:
1
2 4
3 6 9
4 8 12 16
...
'''

n = int(input("Informe a quantidade de linhas: "))

for i in range(1, n + 1):  # Mais um porque ele não imprimiria o n
    for j in range(i, i**2+1, i):
        print(j, end=' ')
    print()

