print('='*54)
print(' '*20, 'ANALISE DE LISTA ')
print('='*54)

valores = list()
pares = list()
impares = list()

while True:
    n = int(input('Digite um número: '))
    valores.append(n)
    for c, v in enumerate(valores):
        if n % 2 == 0:
            pares.append(n)
            break
        else:
            impares.append(n)
            break
    resp = str(input('Deseja continuar? [S/N]: ')).strip().upper()
    if resp == 'N' or resp != 'S':
        break
    print('-'*54)
print(f'Os valores inseridos foram {valores}. ')
print(f'Os valores pares inseridos são {pares}. ')
print(f'Os valores ímpares inseridos são {impares}. ')
print('-'*54)
print(' '*20, 'FINALIZADO')
