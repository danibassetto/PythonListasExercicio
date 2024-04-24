notas = input().split()

n1, n2, n3, n4 = notas
n1 = float(n1)
n2 = float(n2)
n3 = float(n3)
n4 = float(n4)

media = ((2 * n1) + (3 * n2) + (4 * n3) + (1 * n4)) / 10
print(f"Media: {media:.1f}")

if media >= 7.0:
    print("Aluno aprovado.")
elif media < 5:
    print("Aluno reprovado.")
elif 5 <= media <= 6.9:
    print("Aluno em exame.")
    nota_exame = float(input())
    print(f"Nota do exame: {nota_exame:.1f}")
    nova_media = (media + nota_exame) / 2
    if nova_media >= 5:
        print("Aluno aprovado.")
    else:
        print("Aluno reprovado.")
    print(f"Media final: {nova_media:.1f}")


