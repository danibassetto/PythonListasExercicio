''' Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços. Exemplos de
palíndromos: APOS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA. (lê de
frente pra tras e de tras pra frente) '''

frase = str(input("Digite uma frase: ")).strip().upper()  # tira os espaços
palavras = frase.split()  # separa por palavras
junto = ''.join(palavras)  # juntando as palavras
inverso = ''  # OU inverso[::-1]
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
print(f"Inverso de {junto} é {inverso}")
if inverso == junto:
    print("Temos um palíndromo!")
else:
    print("Não temos um palíndromo!")
