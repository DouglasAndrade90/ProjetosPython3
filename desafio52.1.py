print('='*54)
print(' '*13, 'VALIDADOR DE NÚMERO PRIMO')
print('='*54)
cont = 0
n = int(input('Digite um número qualquer: '))
for c in range (1,n+1):
    if n % c == 0:
        print(f'\033[1;33m', end=' ')
        cont += 1
    else:
        print(f'\033[1;36m',end=' ')
    print(f'{c}', end = '')
print('\033[m\n','-'*54)
if cont == 2:
    print(f'\033[mO número {n} foi dividido apenas {cont} vezes e por isso \033[1;36mÉ UM NÚMERO PRIMO.\033[m ')
else:
    print(f'\033[mO número {n} foi dividido {cont} vezes e por isso \033[1;31mNÃO É UM NÚMERO PRIMO.\033[m ')
print('-'*22, 'FINALIZADO', '-'*21)