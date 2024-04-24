'''
Faça um programa em Python que leia o nome e duas notas
de N alunos e armazene em um arquivo texto.
Após a leitura faça a impressão de todos os alunos inseridos.
'''
arq = open('notas.txt','w+')
N = int(input('Informe a quantidade de alunos -> '))
for i in range(N):
    nome = input('Nome -> ').upper()
    n1 = float(input('Nota 1 -> '))
    n2 = float(input('Nota 2 -> '))
    arq.write(f'{nome};{n1};{n2}\n')
arq.seek(0)
print('Lista de alunos')
for a in arq:
    dados = a.split(';')
    notas = list(map(float,dados[1:]))
    media = sum(notas) / len(notas)
    print(f'Nome: {dados[0]} Nota 1: {notas[0]:.2f} '
          f'Nota 2: {notas[1]:.2f} Média: {media:.2f}')
arq.close()


