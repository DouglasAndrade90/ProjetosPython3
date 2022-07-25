print('='*54)
print(' '*17, 'ANALISE DE LISTAS')
print('='*54)

valores = list()

for c in range(0,5):
    n = int(input('Digite um número: '))
    for c , v in enumerate(valores):
        if n < v:
            valores.insert(c,n)
            break
    else:
        valores.append(n)
print('-'*54)
print(f'Os valores digitados foram {valores}. ')
