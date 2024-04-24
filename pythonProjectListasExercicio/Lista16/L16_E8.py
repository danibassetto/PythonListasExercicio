'''
Crie um programa que leia nome e o telefone de várias pessoas, guardando os dados de cada
pessoa em um dicionário, sendo o nome como key e o telefone como value. No final, mostre:
a. A lista das pessoas cadastradas
b. Uma lista de todas as pessoas que tenham o nome com uma determinada inicial. Peça a
letra.
'''


def inserir():
    print('Inserção de contatos')
    nome = input('Nome -> ').upper()
    if nome not in agenda:
        telefone = input('Telefone -> ')
        agenda[nome] = telefone
    else:
        print('Nome já cadastrado!!')


def listagemGeral():
    print('Listagem geral de contatos')
    for nome, numero in sorted(agenda.items()):
        print(f'Nome: {nome} - Telefone: {numero}')


def listagemLetra():
    print('Listagem de contatos por letra')
    letra = input('Informe a letra para consulta -> ').upper()[0]
    for nome, numero in sorted(agenda.items()):
        if nome[0] == letra:
            print(f'Nome: {nome} - Telefone: {numero}')


agenda = {}
while True:
    op = input('1. Inserir\n'
               '2. Listar\n'
               '3. Listar por letra\n'
               '4. Sair\n'
               '=> ')
    if op == '1':
        inserir()
    elif op == '2':
        listagemGeral()
    elif op == '3':
        listagemLetra()
    elif op == '4':
        break
    else:
        print('Opção inválida!!')
