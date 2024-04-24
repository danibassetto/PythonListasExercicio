'''
Seja uma lista de games de uma locadora de games
(código, título, situação).
Faça um programa em Python que realize as
seguintes operações, utilizando funções.
Exiba um menu com as opções:
•	Entrar com os dados – para a situação atribua o
    valor inicial “D” (disponível).
•	Locação – solicitar o código do game e localizar
    o seu registro. Verificar se a situação é “D”
    (disponível) e alterar para “A” (alugado).
    Se o game não estiver disponível exibir uma mensagem. Exibir a mensagem de game não cadastro se não encontra-lo na lista.
•	Devolução – solicitar o código do game e
    localizar o seu registro. Verificar se a situação
    é “A” (alugado) e alterar para “D” (disponível).
    Se o game não estiver disponível exibir uma mensagem. Exibir a mensagem de game não cadastro se não encontra-lo na lista.
•	Listagem – Exibir uma listagem de todos os games
    com o código, título e a situação
    (se for D – escrever “disponível” e A “alugado”).
'''

locadora = []
game = {}

def cadastrar():
    faixa("CADASTRO")
    game.clear()
    print("Entre com os dados do game")
    game['codigo'] = input("Código -> ").upper()
    game['titulo'] = input("Título -> ").upper()
    game['situacao'] = 'D'
    locadora.append(game.copy())

def alugar():
    faixa("LOCAÇÃO")
    cod = input("Informe o código do game para locação -> ").upper()
    achou = False
    for g in locadora:
        if g['codigo'] == cod:
            achou = True
            if g['situacao'] == 'A':
                print("Game já alugado!!")
            else:
                g['situacao'] = 'A'
                print("Locação efetuada!!")
            break
    if not achou:
        print("Game não cadastrado!!!")


def devolver():
    faixa("DEVOLUÇÃO")
    cod = input("Informe o código do game para devolução -> ").upper()
    achou = False
    for g in locadora:
        if g['codigo'] == cod:
            achou = True
            if g['situacao'] == 'D':
                print("Game já disponível!!")
            else:
                g['situacao'] = 'D'
                print("Devolução efetuada!!")
            break
    if not achou:
        print("Game não cadastrado!!!")

def listagem():
    faixa("Listagem")
    for g in locadora:
        if g['situacao'] == 'A':
            sit = 'Alugado'
        else:
            sit = 'Disponível'
        print(f"{g['titulo']} ({g['codigo']}) - {sit}")

def faixa(texto):
    print('~' * 50)
    print(texto)
    print('~' * 50)

while True:
    faixa("LOCAÇÃO DE GAMES")
    op = int(input("1. Cadastro"
                   "\n2. Locação"
                   "\n3. Devolução"
                   "\n4. Listagem"
                   "\n5. Sair"
                   "\nOpção -> "))
    if op == 5:
        break
    elif op == 1:
        cadastrar()
    elif op == 2:
        alugar()
    elif op == 3:
        devolver()
    elif op == 4:
        listagem()
    else:
        print("Opção inválida!!")