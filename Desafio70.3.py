total = maismil = maisbarato = cont = 0
barato = ''

print('='*54)
print(' '*21, 'LOJAS 250 ')
print('='*54)

while True:
    produto = str(input('Digite o nome do produto: ')).strip().upper()
    preco = float(input('Digite o preço: R$ '))
    cont += 1
    total += preco
    if preco > 1000:
        maismil += 1

    if cont == 1 or preco < maisbarato:
        maisbarato = preco
        barato = produto

    resp = ''
    resp = str(input('Deseja continuar? [S/N] ')).strip().upper()
    if resp == 'N':
        break
    print('-'*54)

print(f'O valor total dos produtos é de R$ {total :.2f}. ')
print(f'Foram encontrados {maismil} produto(s) acima de R$ 1000,00. ')
print(f'O produto mais barato encontrado foi {barato} e custa R$ {maisbarato:.2f}. ')
