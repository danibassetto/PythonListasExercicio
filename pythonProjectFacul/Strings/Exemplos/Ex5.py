data = input('Informe a data no formato dd/mm/aaaa >> ')
if data.replace('/','').isdigit():
    d, m, a = data.split('/')
    print('ok')
else:
    print('digite apenas números')