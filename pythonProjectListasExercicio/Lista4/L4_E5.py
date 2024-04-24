# ler 10 números do usuário e calcular a soma dos números pares e a soma dos números ímpares

cont = 1
soma_pares = 0
soma_impar = 0
while cont <= 10:
    n = int(input("Digite um número inteiro: "))
    if n % 2 == 0:
        soma_pares = soma_pares + n
    else:
        soma_impar = soma_impar + n
    cont += 1
print(f'Soma dos pares: {soma_pares}\nSoma dos ímpares: {soma_impar}')