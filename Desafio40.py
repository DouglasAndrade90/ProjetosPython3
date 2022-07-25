from datetime import datetime
from datetime import date
from time import sleep
datetime.now().time()
time = str(datetime.now().time())[:8]
print('='*54)
print(' '*9, 'ESCOLA ESTADUAL TAMANDUÁ BANDEIRA ')
print('='*54)
print(date.today())
print(time)
print('-'*54)
print(' '*18, 'DADOS DO ALUNO ')
print('-'*54)
nome = str(input('Digite o nome do aluno: ')).strip()
n1 = float(input('Digite a primeira nota do aluno: '))
n2 = float(input('Digite a segunda nota do aluno: '))
print('-'*54)
print(' '*16, ' CALCULANDO MÉDIA ')
print('-'*54)
sleep(2)
media = (n1 + n2) / 2
total = media
if media >= 7:
    media = '\033[1;34mAPROVADO\033[m'
elif media >= 5 and media < 6.9:
    media = '\033[1;33mEM RECUPERAÇÃO\033[m'
else:
    media = '\033[1;31mREPROVADO\033[m'
print(f'O aluno {nome} teve média {total}\033[m e está {media}. ')

