''' Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos
dessa progressão. '''

primeiro_termo = int(input("Insira o primeiro termo da PA: "))
razao = int(input("Insira a razão da PA: "))
decimo_termo = primeiro_termo + (10 - 1) * razao  # 10 - 1 para mostrar que sempre será o último menos 1, multiplicado pela razao
for i in range(primeiro_termo, decimo_termo, razao):
    print(i, end=' >> ')
print("ACABOU")
