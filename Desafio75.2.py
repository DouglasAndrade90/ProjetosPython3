print('='*54)
print(' '*16, 'VALIDADOR DE NÚMEROS')
print('='*54)

num = (int(input('Digite o primeiro número: ')),
       int(input('Digite o segundo número: ')),
       int(input('Digite o terceiro número: ')),
       int(input('Digite o último número: ')))
print(num)
print('-'*54)

if 9 in num:
       print(f'Foram digitados {num.count(9)} número(s) 9 nesta rodada. ')
else:
       print('Não foram inseridos número(s) 9 nesta rodada. ')
print('-'*54)
if 3 in num:
       print(f'O primeiro número 3 aparece na posição {num.index(3)+1}. ')
else:
       print('Não foram inseridos números 3 nesta rodada. ')
print('='*54)
print('Os números pares encontrados foram: ')
for n in num:
       if n % 2 == 0:
              print(n, end= ' ')

