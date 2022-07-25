print('='*54)
print(' '*22, 'TABUADA')
print('='*54)
cont = 0
n = int(input('Digite um número para ver sua tabuada: '))
print('-'*54)
for c in range (1,11):
    cont = cont + 1
    print(f'{n:2} X {cont:2} = {n*c:2}')
print('-'*54)
print(' '*24, 'FIM')
