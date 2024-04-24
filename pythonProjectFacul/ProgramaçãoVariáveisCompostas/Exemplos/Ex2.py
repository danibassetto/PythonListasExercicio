# Algoritmo para ler um vetor de 50 notas e calcular e mostrar a média entre elas

notas = [ ]
s = 0
print("Digite a nota dos alunos:")
for i in range(50):
	notas.insert(i, float(input()))

for i in range(50):
	s += notas[i]

med = s/50
print("A media das notas é: ", med)



