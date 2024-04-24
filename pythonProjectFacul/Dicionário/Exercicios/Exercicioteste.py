dicionario = {}
def ptbreng(ling):
    if ling == 2:
        palavra_pt = input("Palavra em ingles: ").upper()
        palavra_eng = input("Palavra Traduzida pro portugues: ").upper()
    else:
        palavra_pt = input("Palavra em portugues: ").upper()
        palavra_eng = input("Palavra Traduzida pro ingles: ").upper()
    if palavra_pt in dicionario.items():
        print("Essa palavra (em portugues) ja foi inserida no dicionario")
    elif palavra_eng in dicionario.items():
        print("Essa palavra (em ingles) ja foi inserida no dicionario")
    else:
        dicionario[palavra_pt] = palavra_eng
def traducao(ling):
    if ling == 4:
        palavra_eng = input("Digite a palavra que voce quer pesquisar em ingles ").upper()
        if palavra_eng in dicionario.values():
            i = list(dicionario.values()).index(palavra_eng)
            print(f"{palavra_eng} significa {list(dicionario.keys())[i]} em portugues")
        else:
            print("essa palavra nao foi cadastrada no dicionario")
    else:
        palavra_pt = input("Digite a palavra que voce quer pesquisar em portugues ").upper()
        if palavra_pt in dicionario:
            print(f"{palavra_pt} significa {dicionario[palavra_pt]} em portugues")
        else:
            print("essa palavra nao foi cadastrada no dicionario")
while True:
    print("="*50)
    print("Tradutor")
    print("="*50)
    op = int(input("1. Cadastrar uma palavra do Português para Inglês"
                   "\n2.Cadastrar uma palavra do Inglês para Português"
                   "\n3.Traducao de uma palavra do Português para Inglês"
                   "\n4.Traducao de uma palavra do Inglês para Português"
                   "\n5. Encerrar"
                   "\nOpção -> "))
    if op == 5:
        break
    elif op == 1:
        ptbreng(op)
    elif op == 2:
        ptbreng(op)
    elif op == 3:
        traducao(op)
    elif op == 4:
        traducao(op)
    else:
        print("Opção inválida!!")