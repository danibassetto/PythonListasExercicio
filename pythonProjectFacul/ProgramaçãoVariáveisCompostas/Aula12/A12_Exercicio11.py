mes = ["janeiro","fevereiro","março","abril","maio","junho","julho","agosto","setembro","outubro","novembro","dezembro"]

a = [0] * 4
for i in range(4):
    a[i] = [0] * 12
    for j in range(12):
        a[i][j] = int(input())

for i in range(4):
    print(a[i])

ta = 0
maior = 0
for j in range(12):
    tm = 0
    for i in range(4):
        tm += a[i][j]
        if a[i][j] > maior:
            maior = a[i][j]
            m = j
            s = i + 1
    ta += tm
    print("Total de peças em",mes[j],"=",tm)
print("Produção anual:",ta)
print("Maior produção semanal foi de:",maior)
print("Ocorreu na",s,"° semana do mês de",mes[m])