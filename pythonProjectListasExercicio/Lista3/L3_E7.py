dist = float(input('Digite a distância em Km: '))
d = float(input("Insira o desempenho em km/l que o veículo apresenta: "))
consumo_de_combustivel = dist / d

if consumo_de_combustivel < 8:
    print('Venda o carro!')
else:
    if consumo_de_combustivel > 8 and consumo_de_combustivel < 14:
        print('Econômico!')
    else:
        print('Super econômico')