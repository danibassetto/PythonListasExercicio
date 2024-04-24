lNotas = []
media = 0
i = 0
while True:
    nota = input('Digite a nota ou FIM para encerrar >> ')
    if nota.upper() == 'FIM':
        break
    lNotas.append(float(nota))
    media += lNotas[i]
    i += 1
print(lNotas)
print(f'Média da sala >> {media/len(lNotas):.2f}')