print('='*54)
print(' '*20, ' LOJAS 250')
print('='*54)

resp = barato = ''
maismil = total = menorpreco = cont = 0


while True:
    if resp == 'N':
        break
    produto = str(input('Digite o nome do produto: ')).strip().upper()
    preco = float(input('Digite o preço do produto R$ '))
    cont += 1
    resp = str(input('Deseja continuar? [S/N]: ')).strip().upper()
    total += preco

    if preco > 1000:
        maismil += 1

    if cont == 1:
        menorpreco = preco
        barato = produto
    else:
        if preco < menorpreco:
            menorpreco = preco
            barato = produto

    print('-'*54)

print(f'O valor total dos produtos foi de R$ {total:.2f}. ')
print(f'Foram encontrados {maismil} produto(s) acima de R$ 1000,00. ')
print(f'O produto mais barato encontrado {barato} e custa R$ {menorpreco:.2f}. ')