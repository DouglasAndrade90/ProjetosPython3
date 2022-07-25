cont = 0
s = 0
print('='*53)
print(' '*21, 'DESAFIO 50')
print('='*53)
for c in range (0, 6):
    n = int(input('Digite um número: '))
    if n % 2 == 0:
        cont = cont + 1
        s = s + n
print('-'*53)
print(f'Foram encontrados {cont} itens que totaliza {s}.')
print('-'*54)
print(' '*22, 'FIM')


