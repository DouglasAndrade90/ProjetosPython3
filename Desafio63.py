print('='*54)
print(' '*15, 'SEQUÊNCIA DE FIBONACCI ')
print('='*54)

pt = 0
se = 1

n = int(input('Digite a quantidade de termos que deseja mostrar: '))
print(f'{pt} → {se} →', end=' ')
cont = 3
while cont <= n:
    te = se + pt
    print(f'{te}', end= ' → ')
    pt = se
    se = te
    cont += 1
print('FIM')
