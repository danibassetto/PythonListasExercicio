'''receita para produzir um bolo conta com 2 xicaras de farinha de trigo, 3 ovos e 5 colheres
de leite (estes dados são constantes nesta receita)'''

F = int(input('Quantidade de xícaras de farinha de trigo: '))
O = int(input('Quantidade de ovos: '))
L = int(input('Quantidade de colheres de leite: '))

F //= 2
O //= 3
L //= 5

if F <= O and O <= L:
    print(f"É possivél fazer {F} receita(s)!")
elif O <= F and F <= L:
    print(f"É possível fazer {O} receita(s)!")
elif L <= F and F <= O:
    print(f"É possível fazer {L} receita(s)!")
elif F == 0 or O == 0 or L == 0:
    print("Ingredientes insuficientes!")