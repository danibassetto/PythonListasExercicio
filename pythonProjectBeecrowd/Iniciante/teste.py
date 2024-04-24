valor = float(input("Digite o valor a ser decomposito: R$ "))
notas = [100, 50, 20, 10, 5, 2]
moedas = [1, 0.50, 0.25, 0.10, 0.05, 0.01]

print("NOTAS:")
for nota in notas:
    qtde_notas = int(valor / nota)
    valor = round(valor % nota, 2)
    print(f"{qtde_notas} nota(s) de R$ {nota:.2f}")

print("MOEDAS:")
for moeda in moedas:
    qtde_moedas = int(valor / moeda)
    valor = round(valor % moeda, 2)
    print(f"{qtde_moedas} moeda(s) de R$ {moeda:.2f}")