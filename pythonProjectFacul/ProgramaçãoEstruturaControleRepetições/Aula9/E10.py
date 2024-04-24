'''Elabore um algoritmo que leia as 50 médias dos alunos matriculados na disciplina de algoritmos.
Mostre qual foi a maior e qual foi a menor média atingida pelos alunos. Considere notas válidas (>=0  e <=10).
'''

maior = 0
menor = 10
for i in range(1, 51):
    med = float(input(f"Insira a média do aluno {i}: "))
    if med < 0 or med > 10:
        print("Média inválida!")
    else:
        if med > maior:
            maior = med
        if med < menor:
            menor = med
print(f"Maior média: {maior}\nMenor média: {menor}")