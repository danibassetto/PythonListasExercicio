# peça a Nota 1 (N1) e a Nota 2 (N2) de 10 alunos e a cada aluno mostre a média M, onde M=(N1+N2)/2

cont = 1
while cont <= 10:
    Aluno = input('Digite o nome do aluno: ')
    N1 = float(input(f'Insira a nota 1 de {Aluno}: '))
    N2 = float(input(f'Insira a nota 2 de {Aluno}: '))
    M = (N1 + N2) / 2
    print(f'Média de {Aluno}: {M}')

    print(50 * '-')
    cont += 1