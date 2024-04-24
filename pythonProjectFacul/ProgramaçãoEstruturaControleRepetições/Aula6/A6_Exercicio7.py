# Transformar binário para decimal
bin = int(input('Digite o número binário a ser convertido: '))
dec = 0
exp = 0
while bin > 0:
    dec = dec + (bin % 10) * (2**exp)
    exp += 1
    bin //= 10
print('Valor em decimal =',dec)