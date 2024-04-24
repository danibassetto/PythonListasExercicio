'''João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho.
Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo
(50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça um algoritmo que leia a
variável P (peso de peixes) e verifique se há excesso. Se houver, calcular quanto foi o excesso e qual será o valor da
multa que João deverá pagar.   '''

P = float(input("Insira o quilo de peixe: "))

if P > 50:
    excesso = P - 50
    multa = excesso * 4
    print(f"João deve pagar R${multa:.2f} pelos {excesso} kg excedentes")
else:
    print("Quantidade adequada! Sem multas a pagar!")