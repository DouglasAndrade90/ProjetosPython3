print('='*54)
print(' '*17, 'VALIDADOR DE NÚMEROS')
print('='*54)

num = (int(input('Digite o primeiro número: ')),
       int(input('Digite o segundo número: ')),
       int(input('Digite o terceiro número: ')),
       int(input('Digite o último número: ')))
print(f'Você inseriu:\n{num}. ')
print('-'*54)
if 9 in num:
    print(f'Foram inseridos {num.count(9)} número(s) 9 nessa rodada. ')
else:
    print('Não foi inserido nenhum número 9. ')
print('-'*54)
if 3 in num:
    print(f'O primeiro número 3 foi inserido na posição {num.index(3)+1}. ')
else:
    print('Não foram localizados número(s) 3 nessa rodada. ')
print('-'*54)
print('Os valores pares digitados foram : ')
for n in num:
    if n % 2 == 0:
        print(n, end= ' ')

