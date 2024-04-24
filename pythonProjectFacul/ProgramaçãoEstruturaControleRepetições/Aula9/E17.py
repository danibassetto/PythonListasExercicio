'''O número 3025 tem a seguinte característica:
30 + 25 = 55
55^2 = 3025
Elabore um programa para mostrar todos os números  de 4 algarismos que possuem esta mesma característica.'''


cont = 1000
while cont < 9999:
    cont1 = cont // 100
    cont2 = cont % 100

    soma = cont1 + cont2

    if soma**2 == cont:
        print(cont)
    cont += 1