def incluirNovoNome():
    novonome = input("Informe o nome que deseja adicionar: ").title()
    agenda[novonome] = []


def incluirTelefone():
    novotelefone = input("Informe o telefone que deseja adicionar: ")
    nome = input("Informe o nome do proprietário deste telefone: ")
    if nome not in agenda:
        resp = input("O nome não existe na agenda, deseja adicionar? [S/N] ").upper()
        if resp == 'S':
            incluirNovoNome()
        else:
            pass
    else:
        agenda[nome].append(novotelefone)


def excluirNome():
    nome = input("Informe o nome que deseja excluir: ").title()
    del agenda[nome]


def consultarTelefone():
    consulta = input("Informe o nome do proprietário do telefone: ")
    print(f'{consulta} >>> {agenda[consulta]}')


def exibirAgenda():
    for n, t in agenda.items():
        print(f'{n} >>> {t}')


def sair():
    print("Processo finalizado!")


agenda = {}
while True:
    print("-=-=-=-=-=- AGENDA TELEFÔNICA =-=-=-=-==-=")
    opcao = int(input("Informe qual operação deseja realizar:"
                      "\n1. Incluir novo nome"
                      "\n2. Incluir novo telefone"
                      "\n3. Excluir nome"
                      "\n4. Consultar telefone"
                      "\n5. Exibir agenda"
                      "\n6. Sair"
                      "\n>>> "))

    if opcao == 1:
        incluirNovoNome()
    elif opcao == 2:
        incluirTelefone()
    elif opcao == 3:
        excluirNome()
    elif opcao == 4:
        consultarTelefone()
    elif opcao == 5:
        exibirAgenda()
    elif opcao == 6:
        sair()
        break
