def cabecalho():
    print('='*54)
    print(' '*17,' ANALISE DE LISTAS')
    print('='*54)


maior = menor = 0
valores = []
cabecalho()


for c in range(0,5):
    n = int(input('Digite um número: '))
    for c, v in enumerate(valores):
        if n < v:
            valores.insert(c,n)
            break
    else:
        valores.append(n)
for c, v in enumerate(valores):
    if c == 0:
        maior = menor = valores[c]
    else:
        if valores[c] > maior:
            maior = valores[c]
        if valores[c] < menor:
            menor = valores[c]

print('-'*54)
print(f'A lista inserida em ordem crescente é {valores}')
print(f'O maior valor encontrado foi {maior}. ')
print(f'O menor valor encontrado foi {menor}. ')
print(' '*20, 'FINALIZADO')
