'''Exercício Python 080: Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma
lista, já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.'''

lista = []
for i in range(0, 5):
    n = int(input("Digite um valor: ")) # 3 possibilidades: ser o primeiro, último ou intermediário
    if i == 0 or n > lista[len(lista)-1]:  # Verificando se é o primeiro valor ou se é maior que o último (lista[-1])
        lista.append(n)  # append adiciona no último
    else:  # Descobrir a posição que deve adicionar
        pos = 0
        while pos < len(lista):  # Varrendo o vetor
            if n <= lista[pos]:  # verificando se n é maior, se for ele entra na posição
                lista.insert(pos, n)
                break
            pos += 1

print("Lista =",lista)

