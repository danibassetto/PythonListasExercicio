'''
Danielle Barros Bassetto - 629391
Cesar Augusto de Almeida - 626848
Joao Vitor Adonis - 590428
'''

txt = open('amigo-secreto.txt', 'w')
while True:
    menu = input("1. Adminstrador\n"
                 "2. Participante\n"
                 "0. Sair\n"
                 ">>> ")

    if menu == '1':
        senhaAdm = input("\nInforme a senha de administrador para prosseguir: ")
        if senhaAdm == 'admin123':
            while True:
                submenu = input("\n1. Listar\n"
                                "2. Consultar\n"
                                "3. Gerar sorteio\n"
                                "0. Voltar\n"
                                ">>> ")

                if submenu == '1':
                    print("\n========== LISTAGEM =========")
                    cont = 1
                    for linha in (open('amigo-secreto.txt', 'r')):
                        print(f"\nParticipante {cont}")
                        conteudo = linha.split(';')
                        print(f'Nome: {conteudo[0]}\nEmail: {conteudo[1]}\nSenha: {conteudo[2]}')
                        if conteudo[3] != "\n":
                            print(f'{conteudo[3]}')
                        cont += 1

                if submenu == '2':
                    consulta = input("\nInforme o nome do participante que deseja consultar: ").title()
                    for linha in (open('amigo-secreto.txt', 'r')):
                        conteudo = linha.split(';')
                        if consulta == conteudo[0]:
                            print(f'Nome: {conteudo[0]}\nEmail: {conteudo[1]}\nSenha: {conteudo[2]}')
                            if conteudo[3] != "\n":
                                print(f'{conteudo[3]}')
                            break

                if submenu == '3':
                    listaNomes = []
                    listaConteudo = []
                    sorteio = []
                    for linha in (open('amigo-secreto.txt', 'r')):
                        conteudo = linha.split(';')
                        listaNomes.append(conteudo[0])
                        listaConteudo.append(f'{conteudo[0]};{conteudo[1]};{conteudo[2]};')
                    primeiro = listaNomes[0]
                    listaNomes.remove(primeiro)
                    listaNomes.append(primeiro)  # transferindo o 1º nome para a última posição, para que fique cíclico
                    for i in range(len(listaNomes)):
                        nova_linha = f'{listaConteudo[i]}' + f'Amigo Secreto >>> {listaNomes[i]}\n'
                        sorteio.append(nova_linha)
                    txt = open('amigo-secreto.txt', 'w+')
                    txt.writelines(sorteio)
                    txt.close()
                    print("Sorteio realizado com sucesso!")

                if submenu == '0':
                    print()
                    break
        else:
            print("Senha incorreta.")

    if menu == '2':
        while True:
            submenu = input("\n1. Cadastrar\n"
                            "2. Consultar amigo secreto\n"
                            "0. Sair\n"
                            ">>> ")

            if submenu == '1':
                nome = input("\nInforme seu nome: ").title()
                email = input("Informe seu e-mail: ").lower()
                senha = input("Informe uma senha: ")
                amigo = ""
                with open('amigo-secreto.txt', 'a') as txt:
                    txt.write(f'{nome};{email};{senha};{amigo}\n')
                print(f"Participante {nome} cadastrado(a) com sucesso!")

            if submenu == '2':
                nome = input("\nInforme seu nome: ").title()
                achouNome = False
                for linha in (open('amigo-secreto.txt', 'r')):
                    conteudo = linha.split(';')
                    nomeP = conteudo[0]
                    senhaP = conteudo[2]
                    amigoP = conteudo[3]
                    if nome == nomeP:
                        senha = input("Informe sua senha: ")
                        achouNome = True
                        if senha == senhaP:
                            if amigoP != "\n":
                                print(f"\n{amigoP}")
                            else:
                                print("\nSorteio ainda não realizado!")
                            break
                        else:
                            print("\nSenha incorreta.")
                if not achouNome:
                    print("Nome inválido!")

            if submenu == '0':
                print()
                break

    if menu == '0':
        print("Amigo secreto encerrado!")
