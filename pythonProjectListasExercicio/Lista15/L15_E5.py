'''
Uma pesquisa foi feita e cada pessoa respondeu ao seguinte questionário:
Sexo: ( )M ( )F
Idade: ____ anos
Você é um zumbi: ( )S ( )N
Você é vegetariano: ( )S ( )N
Considere um arquivo que contém as respostas de todas as pessoas entrevistadas. Considere que as
respostas foram armazenadas da seguinte forma, um entrevistado por linha e suas respostas
separadas por vírgulas: sexo (um caractere, podendo ser ‘M’,‘F’), idade, zumbi (um caractere,
podendo ser ‘S’ ou ‘N’), vegetariano (um caractere, podendo ser ‘S’ ou ‘N’). Faça um programa que
leia este arquivo e devolva as seguintes informações:
• Qual é o percentual de zumbis em relação ao número total de pessoas entrevistadas?
• Qual é o percentual de homens não zumbificados abaixo de 40 anos em relação ao número total de
homens entrevistados?
• Qual é o percentual de mulheres zumbificadas acima de 40 anos, que são vegetarianas, em relação
ao número total de mulheres entrevistadas?
'''

try:
    enquete = open('enquete.txt','r')
    totalZumbis = 0
    totalPessoas = 0
    totalHomens = 0
    totalNZumbisH = 0
    totalMulheres = 0
    totalZumbisM = 0
    for e in enquete:
        dados = e.strip('\n').split(',')
        totalPessoas += 1
        if dados[2] == 'S':
            totalZumbis += 1
        if dados[0] == 'M':
            totalHomens += 1
            if int(dados[1]) < 40 and dados[2] == 'N':
                totalNZumbisH += 1
        if dados[0] == 'F':
            totalMulheres += 1
            if int(dados[1]) > 40 and dados[2] == 'S' and dados[3] == 'S':
                totalZumbisM += 1
    enquete.close()
    print('Resultado da enquete')
    print('Qual é o percentual de zumbis em relação ao número total de pessoas entrevistadas?')
    print(f'R: {totalZumbis / totalPessoas * 100:.2f} %')
    print('Qual é o percentual de homens não zumbificados abaixo de 40 anos em relação ao número total de homens entrevistados?')
    print(f'R: {totalNZumbisH / totalHomens * 100:.2f} %')
    print('Qual é o percentual de mulheres zumbificadas acima de 40 anos, que são vegetarianas, em relação ao número total de mulheres entrevistadas?')
    print(f'R: {totalZumbisM / totalMulheres * 100:.2f} %')
except:
    print('ERRO')