'''
Bate Papo

Policarpo adora matar o tempo nas redes sociais. Uma página com uma lista de bate-papo em sua rede favorita é feita para que, quando uma mensagem é enviada a algum amigo, o bate-papo do amigo sobe para o topo da página. A ordem relativa dos outros bate-papos não muda. Se não houve nenhum bate-papo com esse amigo antes, um novo bate-papo é simplesmente inserido no topo da lista.
Supondo que a lista de bate-papo esteja inicialmente vazia, dada a sequência de mensagens de Policarpo, faça uma lista de bate-papos após o processamento de todas as suas mensagens. Suponha que nenhum amigo tenha escrito nenhuma mensagem para Policarpo.

Entrada
A primeira linha contém o inteiro n - o número de mensagens de Policarpo. As próximas n linhas listam os destinatários da mensagem na ordem em que as mensagens foram enviadas.

Resultado
Imprima todos os destinatários com quem Policarpo falou na ordem dos bate-papos com eles, de cima para baixo.

 
Exemplos

entrada
4
alex
ivan
romano
Ivan
resultado
ivan
romano
alex

entrada
8
alina
maria
ekaterina
darya
darya
ekaterina
maria
alina
resultado
alina
maria
ekaterina
darya

Nota
No primeiro caso de teste, Policarpo escreve primeiro para um amigo pelo nome " alex ", e a lista é a seguinte:
1.	alex
Em seguida, Policarpo escreve para um amigo pelo nome " ivan " e a lista é a seguinte:
1.	ivan
2.	alex
Policarpo escreve a terceira mensagem para um amigo pelo nome " romano " e a lista é a seguinte:
1.	romano
2.	ivan
3.	alex
Policarpo escreve a quarta mensagem para o amigo de nome " ivan ", para quem já enviou uma mensagem, então a lista de chats muda da seguinte forma:
1.	ivan
2.	romano
3.	alex


'''
from collections import OrderedDict
totalMessages = int(input())
authors = list([(input(), True) for message in range(totalMessages)])
print(authors)
authors = authors[::-1]
for author in OrderedDict(authors).keys():
    print(author)
'''
n = int(input('Informe o número de mensagens: '))
d = []
for i in range(n):
    dest = input("Informe o nome do destinatário da mensagem: ")
    if dest in d:
        d.remove(dest)
    d.insert(0,dest)
print(*d,sep="\n")
'''