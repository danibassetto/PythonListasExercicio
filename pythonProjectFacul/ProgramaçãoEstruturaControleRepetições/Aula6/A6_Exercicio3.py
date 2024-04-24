''' Considerando uma classe com 60 alunos, elabore um algoritmo que leia duas notas de cada aluno,
calcule a média e verifique se aluno foi aprovado ou reprovado. Para estar aprovado a média deverá ser maior
ou igual a 6. Determine também a média geral da classe e a quantidade de alunos aprovados e reprovados da turma.'''

n = int(input('Informe a quantidade de alunos: '))
print('-' * 50)
cont = 1
alunos_aprovados = 0
alunos_reprovados = 0
media_geral = 0

while(cont <= n):
    nome = input('Digite o nome do aluno: ')
    n1 = float(input(f'Insira a primeira nota do aluno {cont}: '))
    n2 = float(input(f'Insira a segunda nota do aluno {cont}: '))
    med = (n1 + n2) / 2
    media_geral = media_geral + med / n
    print('-' * 50)
    if med >= 6:
        print(f'Aluno(a): {nome}\nSituação: aprovado(a) com média {med}!')
        alunos_aprovados += 1
    else:
        print(f'Aluno(a): {nome}\nSituação: reprovado com média {med}!')
        alunos_reprovados += 1
    
    cont += 1
    print('-' * 50)
    print()
print(f'Média geral: {media_geral}\nAlunos reprovados: {alunos_reprovados}\nAlunos aprovados: {alunos_aprovados}')
