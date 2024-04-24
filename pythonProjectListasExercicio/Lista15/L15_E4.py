'''
A ACME Inc., uma empresa de 50 funcionários, está tendo problemas de espaço em disco no seu
servidor de arquivos (o HD tem tamanho de 500 Gbytes). As informações de utilização de HD dos
usuários estão no arquivo "usuarios.txt" que possui o seguinte formato (/):

Você deve escrever um programa que lê este arquivo e gera um relatório, chamado "relatório.txt",
no seguinte formato (<nome>/<Mbytes>/<% de disco de uso deste usuário>). No final do arquivo,
escrever o total de espaço de disco ocupado em Megabytes e o % de uso total do disco.
'''

try:
    arqU = open('usuarios.txt', 'r')
    arqR = open('relatorio.txt', 'w')
    totalMega = 0
    for u in arqU:
        dados = u.split()
        mega = int(dados[1])/1000000
        totalMega += mega
        porc = mega / 5000
        arqR.write(f'{dados[0]} / {mega} / {porc:.2f} %\n')
    arqR.write(f'Total de uso: {totalMega} megabytes = {totalMega/5000:.2f} % de uso do total')
    arqU.close()
    arqR.close()
except:
    print('ERRO')