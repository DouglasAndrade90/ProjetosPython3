print('='*54)
print(' '*17, 'VALIDADOR DE NÚMEROS')
print('='*54)

n = (int(input('Digite um número: ')),
    int(input('Digite outro número: ')),
    int(input('Digite mais um número: ')),
    int(input('Digite o último número: ')))
print('-'*54)

print(f'Você digitou {n}. ')
c = n.count(9)
if 9 in n:
    print(f'O número 9 foi digitado {c} vez(es). ')
else:
    print('Não foi digitado nenhum número 9. ')
print('-'*54)
if 3 in n:
    print(f'O número 3 apareceu pela primeira vez na posição {n.index(3)+1}. ')
else:
    print('Não foi digitado nenhum número 3. ')
print('-'*54)
print('Os valores pares digitados foram: ')
for c in n:
    if c % 2 == 0:
        print(c, end= ' ')






