print('='*54)
print(' '*17, 'AVALIADOR DE LISTAS')
print('='*54)

maior = menor = 0
valores = list()

for c in range(0,6):
    valores.append(int(input(f'Digite o valor da posição {c}: ')))
    if c == 0:
        maior = menor = valores[c]
    else:
        if valores[c] > maior:
            maior = valores[c]
        if valores[c] < menor:
            menor = valores[c]

print('-'*54)

print(f'Você inseriu: {valores}')
print(f'O maior valor inserido foi: {maior} e está localizado na posição', end= ' ')
for i, v in enumerate(valores):
    if v == maior:
        print(f'{i}...', end= ' ')

print(f'\nO menor valor inserido foi: {menor} e está localizado na posição', end= ' ')
for i, v in enumerate(valores):
    if v == menor:
        print(f'{i}...', end= ' ')

print(' '*12, 'PROGRAMA FINALIZADO')