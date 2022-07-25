from datetime import date
from time import sleep
print('='*52)
print(' '*11, 'Calculadora de ano Bissexto ', ' '*11)
print('='*52)
sleep(2)
ano = int(input('Digite um ano qualquer, insira 0 caso queira escolher o ano atual: '))
print('-'*52)
print(' '*16, '...Analisando...', ' '*16)
print('-'*52)
sleep(3)
if ano == 0:
    ano = date.today().year
if ano % 4 ==0 and ano % 100 != 0 or ano % 400==0:
    print('O ano {} {} {} É Bissexto. '.format('\033[1;7;40m',ano, '\033[m'))
else:
    print('O ano {} {} {} NÃO É Bissexto. '.format('\033[1:31:44m',ano,'\033[m'))


