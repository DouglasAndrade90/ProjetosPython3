print('='*54)
print(' '*21, 'DESAFIO 51')
print('='*54)
p = int(input('Digite o primeiro termo da progressão aritmética: '))
r = int(input('Digite a razão da progressão aritmética: '))
d = p + (10 - 1) * r
for c in range (p, d + 1, r):
    print(f'{c}', end= ' → ')
print('FIM')


