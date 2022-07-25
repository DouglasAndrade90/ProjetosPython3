print('=' * 54)
print(' ' * 17, ' ANALISE DE VALORES')
print('=' * 54)

valores = [[], []]

for c in range(1, 8):
    n = int(input('Digite o {c}º número: '))
    if n % 2 == 0:
        valores[0].append(n)
    else:
        valores[1].append(n)
print('-' * 54)
print(f'Os números pares inseridos foram {sorted(valores[0])}. ')
print(f'Os valores ímpares inseridos foram {sorted(valores[1])}. ')
print('-' * 54)
print(' ' * 21, 'FINALIZADO')