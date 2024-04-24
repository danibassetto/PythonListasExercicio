from termcolor import colored
def incluirNovoNome(nome, telefones):
    if nome in agenda:
        print(colored('Nome já cadastrado!!','red'))
        return False
    agenda[nome] = telefones
    return True

def incluirTelefone(nome, telefone):
    if nome in agenda:
        if telefone not in agenda[nome]:
            agenda[nome].append(telefone)
            return True
        print(colored(f'{telefone} já cadastrado para {nome}','red'))
        return False
    resp = input(f'{nome} não consta na agenda, deseja cadastrar? [S/N] -> ').upper()[0]
    if resp == 'S':
        incluirNovoNome(nome, [telefone])
        return True
    return False

def excluirTelefone(nome):
    if nome in agenda:
        print(f'Telefones de {nome}:', *agenda[nome])
        if len(agenda[nome]) == 1:
            res = input('Esse contato tem apenas 1 telefone, deseja excluir o contato? [S/N] -> ').upper()[0]
            if res == 'S':
                excluirNome(nome)
                return True
            return False
        else:
            tel = input('Informe o nº de telefone que deseja excluir -> ')
            if tel not in agenda[nome]:
                print(colored('Esse número não consta na lista desse contato','red'))
                return False
            agenda[nome].remove(tel)
            return True
    print(colored(f'{nome} não consta na agenda','red'))
    return False

def excluirNome(nome):
    if nome in agenda:
        print('Telefone(s):', *agenda[nome])
        resp = input('Deseja realmente excluir? [S/N] -> ').upper()[0]
        if resp == 'S':
            del agenda[nome]
            return True
        return False
    print(colored(f'{nome} não consta na agenda','red'))
    return False

def consultarTelefones(nome):
    if nome in agenda:
        print('Telefone(s):',*agenda[nome])
    else:
        print(colored(f'{nome} não consta na agenda','red'))

def listarTelefones():
    for n, t in agenda.items():
        print(f'Nome: {n} Telefone(s):',*t)

def menu():
    return input('1. Incluir novo nome\n'
                 '2. Incluir telefone\n'
                 '3. Excluir telefone\n'
                 '4. Excluir nome\n'
                 '5. Consultar telefones\n'
                 '6. Listar telefones\n'
                 '7. Sair\n'
                 'Opção -> ')

def faixa(texto):
    print('=' * 40)
    print(texto.upper().center(40))
    print('=' * 40)

agenda = {}
while True:
    faixa('Menu de opções')
    op = menu()
    if op == '1':
        faixa('Inclusão de novo nome')
        nome = input('Nome -> ').upper()
        telefones = []
        while True:
            tel = input('Telefone ou 0 para encerrar -> ')
            if tel in telefones:
                print(colored('Telefone já cadastrado par esse contato!!','red'))
                continue
            else:
                if tel == '0':
                    break
                telefones.append(tel)
        if incluirNovoNome(nome,telefones):
            print(colored('Inclusão efetuada com sucesso!!','blue'))
        else:
            print(colored('Inclusão não realizada!!','red'))
    elif op == '2':
        faixa('Inclusão de Telefone')
        nome = input('Nome -> ').upper()
        tel = input('Telefone -> ')
        if incluirTelefone(nome, tel):
            print(colored('Inclusão efetuada com sucesso!!','blue'))
        else:
            print(colored('Inclusão não realizada!!','red'))
    elif op == '3':
        faixa('Exclusão de Telefone')
        nome = input('Nome -> ').upper()
        if excluirTelefone(nome):
            print(colored('Exclusão realizada com sucesso!!','blue'))
        else:
            print(colored('Exclusão não realizada!!','red'))
    elif op == '4':
        faixa('Exclusão de Nome')
        nome = input('Nome -> ').upper()
        if excluirNome(nome):
            print(colored('Exclusão realizada com sucesso!!','blue'))
        else:
            print(colored('Exclusão não realizada!!','red'))
    elif op == '5':
        faixa('Consulta por Nome')
        nome = input('Nome -> ').upper()
        consultarTelefones(nome)
    elif op == '6':
        faixa('Lista de Telefones')
        listarTelefones()
    elif op == '7':
        break
    else:
        print(colored('Opção inválida!!','red'))