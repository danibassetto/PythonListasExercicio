from tabulate import tabulate

alfabeto = []
quantidade_estados = None
tabela = []
estados_finais = None


def criar_afd():
    try:
        alfabeto = input("Informe o alfabeto (separando os caracteres por espaço): ").split()
        quantidade_estados = int(input("Informe a quantidade de estados: "))
        estados_finais = input("Informe o(s) estado(s) final(is) (separando por espaço): ").split()
        estados_finais = [int(estado) for estado in estados_finais]

        tabela = [[None] * len(alfabeto) for _ in range(quantidade_estados)]

        for estado in range(quantidade_estados):
            for idx, letra in enumerate(alfabeto):
                try:
                    proximo_estado = input(f"\nEstado atual: q{estado}"
                                           f"\nEntrada: {letra}"
                                           f"\nPróximo estado: q")
                    tabela[estado][idx] = int(proximo_estado)
                except ValueError:
                    print("Entrada inválida. Certifique-se de que você inseriu um número inteiro.")
                    return [], [], []

        print()
        visualizar_tabela(tabela, alfabeto, estados_finais)
        return alfabeto, tabela, estados_finais
    except Exception as e:
        print(f"Ocorreu um erro ao criar o AFD: {str(e)}")
        return [], [], []


def testar_palavra(alfabeto, tabela, estados_finais):
    if not tabela or not estados_finais:
        print("\nVocê deve criar a tabela do AFD e definir os estados finais primeiro!\n")
    else:
        palavra = input("Informe uma palavra: ")
        estado_atual = 0

        for letra in palavra:
            if letra not in alfabeto:
                print(f"\nHá letra(s) inválidas informadas. Tente novamente.\n")
                break
            idx = alfabeto.index(letra)
            proximo_estado = tabela[estado_atual][idx]
            if proximo_estado is None:
                print("Palavra inválida\n")
                break
            estado_atual = proximo_estado
        else:
            if estado_atual in estados_finais:
                print("Palavra válida\n")
            else:
                print("Palavra inválida\n")


def visualizar_tabela(tabela, alfabeto, estados_finais):
    print("TABELA DO AUTÔMATO FINITO DETERMINÍSTICO")
    headers = ["Estado"] + [f"{letra}" for letra in alfabeto]
    tabela_completa = []
    estado_final = False
    for estado, transicoes in enumerate(tabela):
        if estado in estados_finais:
            linha = [f"q{estado}*"]
        else:
            linha = [f"q{estado}"]
        for transicao in transicoes:
            if transicao in estados_finais:
                linha.append(f"q{transicao}*")
            else:
                linha.append(f"q{transicao}")
        tabela_completa.append(linha)

    print(tabulate(tabela_completa, headers, tablefmt="grid"))


def sobre():
    print("\nEste é um algoritmo para teste de validação de palavras utilizando autômatos finitos deterministicos "
          "\nConsiderações: "
          "\n- Os estados iniciam no q0 e o estado final é definido pelo usuário. Sendo que é possível informar 1 ou mais estados finais."
          "\n- Uma palavra é válida somente se após a execução de todo o autômato ela termine o teste no estado final"
          "\n- Ao criar uma autômato/tabela e depois criar novamente, a anterior será sobrescrita"
          "\n- O '*' indica que o estado é final"
          "\n")


while True:
    try:
        menu = int(input("=========================================\n"
                         "AUTÔMATOS FINITOS DETERMINÍSTICOS (AFD)\n"
                         "========================================="
                         "\n1 - Criar"
                         "\n2 - Testar"
                         "\n3 - Sobre o Algoritmo"
                         "\n4 - Visualizar tabela do AFD"
                         "\n5 - Sair"
                         "\n>>> "))

        match menu:
            case 1:
                alfabeto, tabela, estados_finais = criar_afd()
            case 2:
                testar_palavra(alfabeto, tabela, estados_finais)
            case 3:
                sobre()
            case 4:
                if not tabela or not estados_finais:
                    print("\nVocê deve criar a tabela do AFD e definir os estados finais primeiro!\n")
                    continue
                else:
                    visualizar_tabela(tabela, alfabeto, estados_finais)
            case 5:
                break
            case _:
                print("Opção inválida!\n")
    except ValueError:
        print("Opção inválida. Por favor, insira um número válido.")
