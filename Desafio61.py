print('='*54)
print(' '*15, 'PROGRESSÃO ARITMÉTICA')
print('='*54)

pt = int(input('Digite o primeiro termo da progressão aritmética: '))
r = int(input('Digite a razão da progressão aritmética: '))
d = pt + (10-1) * r

while pt < d:
    pt += r
    print(pt, end= ' ')
    print('-' if pt < d else ' ', end=' ')




