print('='*54)
print(' '*17, 'ANALISE DE LISTAS')
print('='*54)

cont = 0
valores = list()
while True:
    n = int(input('Digite um número: '))
    valores.append(n)
    resp = str(input('Deseja continuar? [S/N]: ')).strip().upper()
    if resp == 'N':
        break
    print('-'*54)
print('-'*54)
print(f'Foram inseridos {len(valores)} números. ')
valores.sort(reverse=True)
print(f'Os valores inseridos em ordem decrescente foram {valores}. ')
for c, v in enumerate(valores):
    if 5 in valores:
        cont += 1
        print(f'Foram encontrados {cont} números 5 na posição {c}. ')
    else:
        print('Não foram encontrados números 5 na lista. ')





