print('='*54)
print(' '*21,'LOJAS 250')
print('='*54)

lista = (str(input('Digite o nome do produto: ')), float(input('Digite o valor do produto: R$ ')),
    str(input('Digite o nome do produto: ')), float(input('Digite o preço do produto: R$ ')),
    str(input('Digite o nome do produto: ')), float(input('Digite o preço do produto: R$ ')),
    str(input('Digite o nome do produto: ')), float(input('Digite o preço do produto: R$ ')),
    str(input('Digite o nome do produto: ')), float(input('Digite o preço do produto: R$ ')))

print('='*54)
print(' '*17, 'LISTAGEM DE PREÇOS')
print('='*54)

for pos in range(0, len(lista)):
    if pos % 2 == 0:
        print(f'{lista[pos]:.<40}', end=' ')
    else:
        print(f'R${lista[pos]:>14.2f}')
print('-'*54)
