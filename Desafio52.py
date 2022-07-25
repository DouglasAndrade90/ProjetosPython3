#print('='*53)
#print(' '*21, 'DESAFIO 52')
#print('='*53)
#m = 0
#n = int(input('Digite um número qualquer: '))
#for c in range (2,n):
#    if n % c == 0:
#        print(f'{n} é múltiplo de: {c}. ')
#        m += 1
#if m == 0:
#    print(f'{n} \033[1:34mÉ\033[mum número primo. ')
#else:
#    print(f'{n} \033[1:31mNÃO É \033[m um número primo. ')

cont = 0
n = int(input('Digite um número qualquer: '))
for c in range (1, n + 1):
    if n % c == 0:
        print('\033[1:31m', end= ' ')
        cont += 1
    else:
        print('\033[1:36m', end=' ')
    print(c)
print(f'\033[mO número {n} foi divisível {cont} vezes. ')
if cont == 2:
    print(f'\033[1;34mE por isso, {n} É um número primo. \033[m')
else:
    print(f'\033[1;31mE por isso, {n} NÃO É um número primo. \033[m')



