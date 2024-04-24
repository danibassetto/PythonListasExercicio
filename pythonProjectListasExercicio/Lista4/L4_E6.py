# Igual ao exercício anterior, mas pedir antes do laço a quantidade de números a serem lidos

cont = 1
soma_pares = 0
soma_impar = 0
qn = int(input('Digite quantos números você deseja somar: '))
while cont <= qn:
    n = int(input("Digite um número inteiro: "))
    if n % 2 == 0:
        soma_pares = soma_pares + n
    else:
        soma_impar = soma_impar + n
    cont += 1
print(f'Soma dos pares: {soma_pares}\nSoma dos ímpares: {soma_impar}')