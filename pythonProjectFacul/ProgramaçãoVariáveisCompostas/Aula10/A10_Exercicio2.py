# um vetor mais o outro resultando em outro vetor

a = [0] * 10
print("Digite os valores do vetor A: ")
for i in range(10):
    a[i] = int(input())

b = [0] * 10
print("Digite os valores do vetor B: ")
for i in range(10):
    b[i] = int(input())

c = [0] * 10
for i in range(10):
    c[i] = a[i] + b[i]
for i in range(10):
    print(a[i],'+',b[i],'=',c[i])
