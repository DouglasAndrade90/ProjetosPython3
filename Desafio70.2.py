resp = barato = ''
maisbarato = cont = total = maismil = 0
print('='*54)
print(' '*20,'LOJAS 250 ')
print('='*54)


while True:
    if resp == 'N':
        break
    produto = str(input('Digite o nome do produto: ')).strip().upper()
    preco = float(input('Digite o preço do produto: R$ '))
    cont += 1
    total += preco

    if preco > 1000:
        maismil += 1

    if cont == 1:
        maisbarato = preco
        barato = produto
    else:
        if preco < maisbarato:
            maisbarato = preco
            barato = produto


    resp = str(input('Deseja continuar? [S/N] ')).strip().upper()
    print('-'*54)

print(f'A valor total dos produtos foi de R$ {total:.2f}. ')
print(f'Foram encontrados {maismil} produto(s) acima de R$ 1000,00 . ')
print(f'O produto mais barato foi {barato} e custou {maisbarato:.2f}. ')
