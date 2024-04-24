'''
Recursão é um método de resolução de problemas que envolve quebrar um problema em subproblemas menores e menores até
chegar a um problema pequeno o suficiente para que ele possa ser resolvido trivialmente. Normalmente recursão envolve
uma função que chama a si mesma. Embora possa não parecer muito, a recursão nos permite escrever soluções elegantes para
problemas que, de outra forma, podem ser muito difíceis de programar.

Vamos começar a nossa investigação com um problema simples que você já sabe como resolver sem o uso de recursão. Suponha
que você deseje calcular a soma de uma lista de números, tais como: [1,3,5,7,9]. A função usa uma variável acumuladora
(theSum) para calcular o total de todos os números da lista iniciando com 0 e somando cada número da lista.


def listsum(numList):
    theSum = 0
    for i in numList:
        theSum = theSum + i
    return theSum
print(listsum([1,3,5,7,9]))

Calculando a soma de uma lista de números
Imaginem por um minuto que você não tem laços while ou for. Como você calcularia a soma de uma lista de números? Se
você fosse um matemático poderia começar a recordar que a adição é uma função definida para dois parâmetros, um par de
números. Para redefinir o problema da adição de uma lista para a adição de pares de números, podemos reescrever a lista
como uma  expressão totalmente entre parênteses. Tal expressão poderia ser algo como:
((((1+3)+5)+7)+9)
Poderíamos também colocar os parênteses na ordem reversa, (1+(3+(5+(7+9)))) Observe que o par de parênteses mais
interno, (7+9), é um problema que podemos resolver sem um laço ou qualquer construção especial.

Calculando a soma de uma lista de números
Na verdade, pode-se utilizar a sequência de simplificações, mostradas ao lado, para calcular uma soma final.
total= (1+(3+(5+(7+9))))
total= (1+(3+(5+16)))
total= (1+(3+21))
total= (1+24)
total= 25

Calculando a soma de uma lista de números
Como podemos usar essa ideia e transformá-la em um programa Python? Em primeiro lugar, vamos reformular o problema soma
em termos de listas de Python. Poderíamos dizer que a soma da lista numList é a soma do primeiro elemento da lista
(numList [0]), com a soma dos números no resto da lista (numList [1:]).

def listsum(numList):
    if len(numList) == 1:
        return numList[0]
    else:
        return numList[0] + listsum(numList[1:])
print(listsum([1,3,5,7,9]))

Existem algumas ideias-chave nesse programa para se estudar. Em primeiro lugar, na linha 2 estamos verificando se a
lista possui apenas um elemento. Esse teste é fundamental e é a nossa cláusula de escape da função. A soma de uma lista
de comprimento 1 é trivial; ela é o número na lista. Em segundo lugar, na linha 5, nossa função chama a si mesma! Esta
é a razão pela qual chamamos listsum de algoritmo recursivo. Uma função recursiva é uma função que chama a si mesma.


Quando uma função chama a si mesma, ocorre as seguintes situações:
    - novos parâmetros e variáveis locais são alocados na pilha;
    - o código da função é executado com essas novas variáveis;
    - não é feito uma nova cópia da função; apenas os argumentos são novos.

Quando cada função recursiva retorna, ocorre:
    - as variáveis locais e os parâmetros são removidos da pilha;
    - a execução recomeça do ponto da chamada à função dentro da função.

A maioria das funções recursivas não minimiza significativamente o tamanho do código, nem melhora a utilização da
memória;

As versões recursivas da maioria das rotinas podem ser executadas um pouco mais lentamente que suas equivalentes
iterativas devido às repetidas chamadas à função;

Muitas chamadas recursivas a uma função podem provocar um estouro de pilha;

A principal vantagem das funções recursivas é que podem ser usadas para criar versões mais claras e simples de
vários algoritmos;

Ao escrever funções recursivas, deve haver uma instrução condicional que limite a quantidade de chamadas recursivas,
por exemplo, uma instrução if, em algum lugar para forçar a função a retornar sem que a chamada recursiva seja
executada. Se não o fizer, a função nunca retornará quando chamada.

Alguns algoritmos são tão naturalmente adaptados a uma estrutura recursiva, que submetê-los a uma forma não-recursiva
simplesmente não faz sentido.

Alguns exemplos:
    - Algoritmo QuickSort, um algoritmo para ordenação de dados, que é muito difícil de implementar numa forma iterativa;
    - Algoritmos para manipulação de árvores, que são estruturas completamente recursivas;
    - Algoritmo que avalia uma expressão matemática armazenada em uma cadeia.


'''
