'''
Uma variável é dita composta quando ela pode armazenar mais do que um valor ao mesmo tempo;

Dizemos que a variável é composta e homogênea, quando todos os valores nela armazenados são do mesmo tipo.

VETORES

--> Contém espaço para armazenar diversos valores e, o que diferencia um valor do outro é a posição que ele ocupa

--> Uma mesma variável guarda ao mesmo tempo múltiplos valores
	Exemplo: x = [1, 2, 3, 4, 5, ...]

Para acessar uma posição do vetor, basta informar a posição (índice) entre colchetes.

Antes de usar um vetor, ele precisa ser criado (declarado). Assim:

<identificador> = [ ];

Ex:
	a = [];  	// a é uma variável que pode armazenar diversos valores  (a é um vetor)

Na declaração:
<identificador> = [VALOR1, VALOR2, …, VALORN]
Ex:
a = [3,43,76,9]

Após a declaração:
<identificador>.inserir(INDICE, VALOR)
Ex:
a = [ ]
a.inserir(0, 3)
a.inserir(1,43)
a.inserir(2, 76)

O método inserir, faz a inserção de um elemento na estrutura na posição indicada.


'''