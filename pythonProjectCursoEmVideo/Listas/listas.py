'''
LISTAS
# o que as diferencia das tuplas é que elas são mutáveis (podemos adicionar, remover, mudar...), representadas por []

# Criando lista vazia
lista = []
lista = list()

# Adicionando
lista.append(elemento)  # adicionando elemento no final
lista.insert(posição, elemento)  # adicionando elemento em determinada posição

# Removendo pela posição
del lanche[3]  # removendo o elemento da posiçaõ 3
lanche.pop(3)  # normalmente o pop é para eliminar o último
# Removendo pelo elemento
lanche.remove(elemento)  # Elimina o elemento e reposiciona a lista

# Criar listas a partir de range
valores = list(range(4,11))
valores.sort()  # ordenando em ordem crescente
valores.sort(reverse=True)  # ordenando em ordem inversa

# Quantidade de elementos
len(valores)
'''

num = [2, 5, 9, 1]
num[2] = 3
num.append(7)
num.insert(2, 2)
if 4 in num:
    num.remove(4)
else:
    print("Não achei o número 5")
print(num)
print(f'Essa lista tem {len(num)} elementos!')

valores = []
for c, v in enumerate(valores):
    print(f"Na posição {c} encontrei o valor {v}!")
for cont in range(0, 5):
    valores.append(int(input("Informe os valores da lista: ")))

# Ligando uma lista na outra (qualquer alteração em uma é replicada na outra)
a = [1, 2, 3, 4]
b = a
b[2] = 8
print(f"Lista A: {a}")
print(f"Lista B: {b}")

# Fazendo uma cópia de uma lista
b = a[:]
b[2] = 1
print(f"Lista B: {b}")


# Matrizes
dados = ['Pedro', 25]
pessoas = list()
pessoas.append(dados[:])  # Dados virou um elemento de pessoas
print(pessoas)
print(pessoas[0][0])  # printa o elemento 0 do elemento 0

teste = []
teste.append("Danielle")
teste.append(40)
print(teste)

galera = []
galera.append(teste[:])
teste[0] = "Maria"
teste[1] = 22
galera.append(teste[:])
print(galera)

galera = [['João', 19], ["Ana", 33], ['Joaquim', 13]]
print(galera[0])
print(galera[0][0])
print(galera[2][1])
for p in galera:
    print(p)

for p in galera:
    print(p[0])

for p in galera:
    print(f"{p[0]} tem {p[1]} anos.")

galeris = []
dado = []
for i in range(0, 5):
    dado.append(str(input("Nome: ")))
    dado.append(int(input("Idade: ")))
    galera.append(dado[:])
    dado.clear()  # Excluindo dado
print(galera)
