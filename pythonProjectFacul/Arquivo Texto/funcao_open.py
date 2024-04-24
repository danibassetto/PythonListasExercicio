'''

Função open

Para acessar um arquivo, precisamos abri-lo. Durante a abertura, informamos o nome do arquivo, com o nome da pasta
em que ele se encontra e que operações queremos realizar: leitura e/ou escrita. Em Python, abrimos arquivos com
a função open.

A função open utiliza os parâmetros nome e modo. O nome é o nome do arquivo em si e o modo indica as
operações que vamos realizar.

Modo            Operações
r                leitura
w                escrita, apaga o conteúdo se já existir
a                escrita, mas preserva o conteúdo já existente
b                modo binário
+                atualização (leitura e escrita)

Os modos podem ser combinados (“r+”, “w+”, “a+”, “r+b”, “w+b”, “a+b”.

A função open retorna um objeto do tipo file (arquivo). É esse objeto que vamos utilizar para ler e escrever os dados.

'''

fp = open("numeros.txt","w")
fp = open("e:\\numeros.txt","w")
fp = open("arquivos\\numeros.txt","w")

# Ao tentar abrir um arquivo no modo leitura e o mesmo não existir, o programa gerará um erro.
fp = open("numeros.txt","r")


