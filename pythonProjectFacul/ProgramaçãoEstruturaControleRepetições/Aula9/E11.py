'''Elabore um algoritmo que leia um conjunto de idades e calcule e mostre a maior entre elas.
Encerrar o algoritmo quando for digitado 0 para a idade.
'''

maior = 0
print("Informe a idade ou 0 para encerrar: ")
while True:
    idade = int(input())
    if idade != 0:
        if idade > maior:
            maior = idade
    else:
        print(f"Maior idade: {maior}")
        break


