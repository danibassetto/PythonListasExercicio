# Algoritmo triângulo
a=float(input("Insira a medida A >> "))
b=float(input("Insira a medida de B >> "))
c=float(input("Insira a medida de C >> "))
if (a<b+c and b<c+a and c<b+a):
    print("É um tringulo", end=' ')
    if (a==b and a==c):
        print("equilátero (todos os lados iguais)!")
    else:
        if (a==b or a==c or b==c):
                print("isósceles (apenas um lado diferente)!")
        else:
               print("escaleno (todos os lados diferentes)!")
else:
    print("Não é um tringulo!")
print("FIM")