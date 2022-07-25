valores = list()
pares = list()
impares= list()

print('='*54)
print(' '*17, 'ANALISE DE LISTA')
print('='*54)

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
print('-'*54)
print(f'Os valores inseridos foram\n {sorted(valores)}. ')
print(f'Os valores pares inseridos foram\n {sorted(pares)}. ')
print(f'Os valores ímpares inseridos foram\n {sorted(impares)}. ')
print('-'*54)
print(' '*20, 'FINALIZADO')
