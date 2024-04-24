# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date  # para pegar a data atual

atual = date.today().year
nascimento = int(input("Ano de nascimento: "))
idade = atual - nascimento
print(f"Quem nasceu em {nascimento} tem {idade} anos em {atual}.")

if idade == 18:
    print("Você tem que se alistar IMEDIATAMENTE!")
elif idade < 18:
    saldo = 18 - idade
    print("Você ainda não tem 18 anos!")
else:
    saldo = idade - 18
    print("Você ja deveria ter se alistado a {saldo} ano(s)!")
