# Algoritmo triângulo
a = int(input("Insira o ângulo A >> "))
b = int(input("Insira o ângulo B >> "))
c = int(input("Insira o ângulo C >> "))
print('-' * 50)
if a+b+c == 180 and a != 0 and b != 0 and c != 0:
    if (a == 90 or b == 90 or c == 90):
        print("É um tringulo retângulo")
    else:
        if (a > 90 or b > 90 or c > 90):
            print("É um triângulo obtusângulo")
        else:
            print("É um triângulo acutângulo!")
else:
    print("Valores inválidos! Não é um tringulo!")
print("FIM")