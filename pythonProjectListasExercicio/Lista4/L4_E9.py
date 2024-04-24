''' programa  para  mostrar  a  sequência  dos  N  primeiro  números  da  série  de Fibonacci:
1   1   2   3   5   8   13   21   34   55   89 ....
Sempre o próximo elemento é a soma dos dois anteriores, assim, no exemplo o próximo é 144. '''


print('Sequência de Fibonacci')
print(50 * '-')
n = int(input('Quantos termos deseja mostrar? '))
t1 = 0
t2 = 1
print('{} -> {}'.format(t1,t2), end='')
cont = 3  # Pois ja mostrei o primeiro e segundo
while cont <= n:
    t3 = t1 + t2
    print(' -> {}'.format(t3),end='')
    t1 = t2
    t2 = t3
    cont += 1

