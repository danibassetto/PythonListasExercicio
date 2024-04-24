'''Um tipo de dados bastante usado no dia a dia são as strings, ou cadeias de caracteres
O tipo de dados string, possui várias operações úteis associadas a ele.
Essas operações tornam Python uma linguagem bastante propícia para manipulação de textos.
'''

# Imprimindo uma string.
s = "Olá, mundo!"
print(s)

# Tamanho de uma string.
len(s)

# Concatenação
print("Meu Brasil " + "brasileiro")

S = "COMPUTADOR"

print(S[0])
print(S[4])

# É possível acessar, buscar ou trocar subtrings (fatias) de um string.
S = "COMPUTADOR"
print(S[ 1:3] )
# Sairá na tela: “OM”

# Se omitirmos o índice de início da fatia ou o de final (ou ambos), o início e o final da string serão considerados,
# respectivamente. Veja os exemplos:

print(S[:4])
print(S[4:])
# Sairá na tela: “COMP”   e “UTADOR”

'''
A técnica slicing permite acessar os elementos de um String segundo algum critério.
Sintaxe:
	STR [início:fim:salto], onde:

início é o primeiro índice a ser considerado (o primeiro caracter da string é considerado caso este valor seja omitido);

fim - 1 é o último índice a ser considerado (o último caracter da string é considerado caso este valor seja omitido); 

salto indica quantos caracteres devem ser saltados em cada etapa 

(o valor -1é considerado por padrão, e um sinal de menos deve ser usado para percorrer a string em ordem reversa).
'''

A = "COMPUTADOR"
print(A[::2])
print(A[1::2])

Inv = A[::-1]
print(Inv)

# A função list, transforma um string em uma lista de caracrteres.

L = list("SISTEMAS")  # L =[‘S’,’I’,’S’,’S’,’T’,’E’,’M’,’A’,’S’]

# A função join, faz o processo ao contrário... Faz a lista de caracteres se tornar um string. Veja:
str ="".join(L)

# O operador in retorna True caso a palavra pertença ao string.
str = "Análise de Sistemas"
if ("Análise" in str):
        print(str)

# O método count retorna com a quantidade de vezes que determinado caractere ou substring aparece no string.
print(str.count("e"))

# O método find retorna a posição da  primeira ocorrência quando encontra uma substring dentro de outra, retornando -1
# caso não encontre.

str ="Análise de Sistemas"
print(str.find("Sis"))

# O método split quebra um string a partir de um caractere passado como parâmetro, retornando uma lista com as substrings
# já separadas.

frase = "No meio do caminho tinha uma pedra"
L = frase.split(" ")

''' O método starswith verifica os primeiros caracteres da string e o método endswith verifica os últimos, retornado True 
caso sejam iguais ou False, caso contrário '''

nome = "João da Silva"
nome.startswith("João")
nome.startswith("joão")
nome.endswith("Silva")

''' O método lower retorna uma cópia da string com todos os caracteres minúsculo, e o método upper retorna uma cópia com
todos os caracteres maiúsculos. '''

nome = "João da Silva"
nome=nome.lower()
print(nome)
nome=nome.upper()
print(nome)

# O operador in retorna True caso a palavra pertence a uma string e False caso contrário.

nome = "João da Silva"
if "João" in nome:
        print("Pertence")
else:
        print("Não pertence")

''' O método find retorna a posição da primeira ocorrência quando encontra uma string dentro de outra, retornando -1 caso 
não encontre. '''

s = "Alô Mundo"
print(s.find("Mun"))
print(s.find("ok"))

''' O método rfind é semelhante ao método find, a diferença é que a busca é feita da direita para a esquerda.
Tanto find quanto rfind suportam duas opções adicionais: início e fim. Se for especificado o início, a pesquisa começará
 a partir dessa posição. Se for especificado o fim, a pesquisa utilizará essa posição como último caractere a ser 
considerado. '''

s = "Um dia de sol"
print(s.rfind("d"))
print(s.find("d"))

t = "um tigre, dois tigres, três tigres"
print(t.find("tigres"))
print(t.find("tigres",20))
                  #início=20
print(t.find("tigres",0,10))
          #início=0 e fim=10

''' O método split quebra uma string a partir de um caractere passado como parâmetro, retornando uma lista com as
substrings já separadas. '''

t = "um tigre, dois tigres, três tigres"
l=t.split(",")
print(l)
l=t.split(" ")
print(l)
l=t.split()
print(l)

''' Com o método replace, o primeiro parâmetro é a string a substituir; e o segundo, o conteúdo que a substituirá. 
Opcionalmente, podemos passar um terceiro parâmetro que limita quantas vezes queremos realizar a repetição.'''

t = "um tigre, dois tigres, três tigres"
l=t.replace("tigre", "gato")
print(l)
l=t.replace("tigre", "gato", 1)
print(l)
l=t.replace("tigre", "")
print(l)
l=t.replace("", "-")
print(l)

''' O método strip é utilizado para remover espaços em branco do início ou fim da string. Já os métodos lstrip e rstrip 
removem apenas os caracteres em branco à esquerda ou à direita, respectivamente. '''

t = "   Olá   "
print("**"+t.strip()+"**")
print("**"+t.lstrip()+"**")
print("**"+t.rstrip()+"**")

# Se passar um parâmetro tanto para strip quanto para lstrip ou rstrip, este será utilizado como caractere a remover:

t = "...///Olá///..."
print(t.strip("."))
print(t.lstrip("."))
print(t.rstrip("."))
print(t.strip("./"))

''' isalnum, verifica se todos os caracteres são letras e/ou números.
isalpha, verifica se todos os caracteres são letras.
isdigit, verifica se todos os caracteres são números.
isupper, verifica se todos os caracteres são letras maiúsculas.
islower, verifica se todos os caracteres são letras minúsculas'''
