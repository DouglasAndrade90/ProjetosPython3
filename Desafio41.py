from datetime import datetime
from datetime import date
datetime.now().time()
time = str(datetime.now().time())[:8]
print(date.today())
print(time)
print('='*54)
print(' '*9, 'CONFEDERAÇÃO NACIONAL DE NATAÇÃO')
print('='*54)
nome = str(input('Digite seu nome: '))
nasc = int(input('Digite o ano de seu nascimento: '))
anos = date.today().year - nasc
idade = date.today().year - nasc
if idade <= 9:
    idade = 'MIRIM'
elif idade > 9 and idade < 14:
    idade = 'INFANTIL'
elif idade > 14 and idade <= 19:
    idade = 'JUNIOR'
elif idade == 20:
    idade = 'SÊNIOR'
else:
    idade = 'MASTER'
print(f'{nome} você tem \033[1:33m{anos}\033[m ano(s) e se encaixa na categoria \033[1;33m{idade}\033[m. ')



