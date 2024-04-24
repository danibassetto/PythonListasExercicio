# Algoritmo para ler letras até que seja pressionada a letra ‘z’

letra = ''
while True:
    letra = input('Digite uma letra ou Z para encerrar: ').upper()
    if letra != 'Z':
        print('Você inseriu a letra:',letra)
    else:
        break