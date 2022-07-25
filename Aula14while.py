'''r = 'S'
while r  == 'S':
    n = int(input('Digite um número: '))
    r = str(input('Deseja continuar? [S/N]. ')).strip().upper()
print('Fim')'''
print('='*54)
print(' '*21,'TABUADA' )
print('='*54)
c = 1
n = int(input('Digite um número para ver sua tabuada: '))
while c < 11:
    print(f'{n:2} X {c:2} = {n*c:3} ')
    c += 1
print('-'*22 , 'FIM', '-'*22)
