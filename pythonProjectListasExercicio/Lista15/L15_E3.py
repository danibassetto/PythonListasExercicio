'''
Um professor armazena em um arquivo texto “classe.txt” o número e o nome de cada aluno da turma
da disciplina sob sua responsabilidade. Por questão de segurança, ele prefere armazenar as notas
obtidas pelos alunos em cada prova em um outro arquivo texto (notas.txt), onde cada linha contém
o número do aluno e os valores das notas de 4 provas. Escreva um programa que permita consultar
as notas de cada aluno a partir do seu nome ou do seu número. Seu programa deve receber o nome
ou número como entrada e buscar e imprimir a linha correspondente ao nome no arquivo “notas.txt”.

'''


def consultaNumero():
    numero = input('Informe o número do aluno -> ')
    notas.seek(0)
    achou = False
    for a in notas:
        num, *n = a.split()
        if num == numero:
            print('Notas ->',*n,'\n')
            achou = True
            break
    if not achou:
        print('Não há aluno com esse número\n')

def consultaNome():
    nome = input('Informe o nome do aluno -> ')
    classe.seek(0)
    achou = False
    pos = 0
    for a in classe:
        num, n = a.split()
        if n == nome:
            notas.seek(0)
            geral = notas.readlines()
            print('Notas ->', geral[pos][2:])
            achou = True
            break
        pos += 1
    if not achou:
        print('Não há aluno com esse nome\n')

try:
    classe = open('classe.txt', 'r')
    notas = open('notas.txt', 'r')
    while True:
        op = input('Escolha a opção\n'
                   '1. Consultar pelo número\n'
                   '2. Consultar pelo nome\n'
                   '3. Sair\n'
                   '=> ')
        if op == '1':
            consultaNumero()
        elif op == '2':
            consultaNome()
        elif op == '3':
            break
        else:
            print('Opção inválida')
    classe.close()
    notas.close()
except:
    print('ERRO')