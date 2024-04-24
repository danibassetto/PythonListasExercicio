while True:
    palavra = str(input("Informe uma palavra (dicionário = {a, b}) ou zero para encerrar: "))
    pilha = []
    entrou_b = False
    contador_letras = 0

    if palavra == '0':
        print("Teste finalizado!")
        break

    for letra in palavra:
        if letra not in ('a', 'b'):
            print("Há caracteres inválidos! Tente novamente.")
            break
        elif palavra.startswith('b') or (entrou_b and letra == 'a'):
            print("Para ser válida, a sequência deve começar com 'a' e terminar com 'b' em uma única sequência, "
                  "sendo que ambas devem estar em igual quantidade. Tente novamente.\n")
            break
        elif letra == 'a':
            pilha.append(letra)
        else:
            entrou_b = True
            try:
                pilha.pop()
            except IndexError:
                print("Para ser válida, a sequência deve começar com 'a' e terminar com 'b' em uma única sequência, "
                      "sendo que ambas devem estar em igual quantidade. Tente novamente.\n")
                break
        contador_letras += 1

    if contador_letras == len(palavra):
        if not pilha and contador_letras != 0:
            print("Palavra válida!\n")
        else:
            print("Para ser válida, a sequência deve começar com 'a' e terminar com 'b' em uma única sequência, "
                  "sendo que ambas devem estar em igual quantidade. Tente novamente.\n")