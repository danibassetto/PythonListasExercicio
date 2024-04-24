from collections import OrderedDict
from operator import itemgetter

dic = {'Beatriz': 15, 'Paulo': 19, 'Carlos': 5, 'Raquel': 12, 'Elisa': 18}
print(dic)
for nome in sorted(dic):
    print (nome,dic[nome])

for nome in sorted(dic, key = dic.get):
    print (nome,dic[nome])

agenda = sorted(dic.items(),key=itemgetter(1), reverse=True)
print(agenda)


d = OrderedDict.fromkeys('abcde')
d.move_to_end('b')
print(''.join(d.keys()))
d.move_to_end('b', last=False)
print(''.join(d.keys()))