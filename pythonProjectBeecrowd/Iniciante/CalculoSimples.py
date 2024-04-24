''' Neste problema, deve-se ler o código de uma peça 1, o número de peças 1, o valor unitário de cada peça 1, o código
de uma peça 2, o número de peças 2 e o valor unitário de cada peça 2. Após, calcule e mostre o valor a ser pago.'''

peca1 = input()
peca2 = input()

dados1 = peca1.split()
num1 = int(dados1[1])
valor1 = float(dados1[2])

dados2 = peca2.split()
num2 = int(dados2[1])
valor2 = float(dados2[2])

print(f"VALOR A PAGAR: R$ {(valor1 * num1) + (valor2 * num2):.2f}")