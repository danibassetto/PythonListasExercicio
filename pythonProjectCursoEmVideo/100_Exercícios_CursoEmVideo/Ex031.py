''' Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50
por Km para viagens de até 200Km e R$0,45 parta viagens mais longas. '''

d = float(input("Insira a distância da viagem: "))
if d <= 200:
    pp = 0.5 * d
    print("Preço da passagem: R${pp:2f}")
else:
    pp = 0.45 * d
    print("Preço da passagem: R${pp:2f}")
