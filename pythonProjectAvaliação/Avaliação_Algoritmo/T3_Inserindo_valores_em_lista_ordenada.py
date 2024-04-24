'''
Trabalho 3 - Inserindo valores em lista ordenada - Análise e Projeto de Algoritmos BCC UNIVEM
Danielle Barros Bassetto RA: 62939-1
Prof. Maurício Duarte
'''

a = []  # Declarando na letra 'a' a lista a ser formada
while True:  # Vai inserir números até que seja encerrado o programa com '#'
    pos = 0
    n = input("Informe o número que deseja inserir ou '#' para encerrar: ")  # Inserindo os números na lista
    if n == '#':
        if len(a) == 0:  # Caso a pessoa encerre o programa sem digitar nada, a lista continuará vazia
            print("LISTA VAZIA!")
        else:
            print(f"LISTA ENCERRADA!\nLista = {a}")
        break
    elif len(a) == 0:  # Inserindo o primeiro número informado
        a.append(int(n))
        print(a)
    else:
        if int(n) <= a[0]:  # Inserindo o menor número informado na posição inicial
            a.insert(0, int(n))
            print(a)
        elif int(n) >= a[-1]:  # Inserindo o maior número informado na posição final
            a.append(int(n))
            print(a)
        else:
            while a[pos] < int(n):  # Inserindo os números intermediários em suas devidas posições em ordem crescente
                pos += 1
            a.insert(pos, int(n))
            print(a)