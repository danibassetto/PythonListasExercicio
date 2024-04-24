''' Foi realizada uma pesquisa para saber qual dos candidatos abaixo seria o eleito. Cada pessoa respondeu com o
código do candidato a que votaria. Assim,

Código		Candidato
13				Dilma
45				Aécio
43				Marina
Outros		Nulos

Elabore um algoritmo que totalize os votos que cada candidato recebeu na entrevista, bem como o percentual sobre o
total dos votos lidos,  e ainda, pela pesquisa qual deles seria o eleito. Encerrar o algoritmo quando for digitado 0
para o código.
'''

soma_votos = 0
dilma = 0
aecio = 0
marina = 0

while True:
    voto = int(input("Informe o código do candidato escolhido ou zero para encerrar: "))
    if voto != 0:
        soma_votos += 1
        if voto == 13:
            dilma += 1
        elif voto == 45:
            aecio += 1
        elif voto == 43:
            marina += 1
    else:
        if dilma > aecio and dilma > marina:
            print(f"Total de votos: {soma_votos}\nVotos para Dilma: {dilma}\nVotos para Aécio: {aecio}\nVotos "
              f"para Marina: {marina}\nDILMA GANHOU")
        elif aecio > marina:
            print(f"Total de votos: {soma_votos}\nVotos para Dilma: {dilma}\nVotos para Aécio: {aecio}\nVotos "
              f"para Marina: {marina}\nAÉCIO GANHOU")
        else:
            print(f"Total de votos: {soma_votos}\nVotos para Dilma: {dilma}\nVotos para Aécio: {aecio}\nVotos "
                  f"para Marina: {marina}\nMARINA GANHOU")
        break