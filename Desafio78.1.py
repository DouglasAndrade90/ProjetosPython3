valores = list()
maior = menor = 0
for c in range(0,6):
    valores.append(int(input(f'Digite o valor para a posição {c}: ')))

    if c == 0:
        maior = menor = valores[c]
    else:
        if valores[c] < menor:
            menor = valores[c]
        if valores[c] > maior:
            maior = valores[c]

print('-'*54)
print(f'Você inseriu: {valores} ')
print(f'O maior valor inserido foi: {maior} nas posições', end= ' ')
for i, v in enumerate(valores):
    if v == maior:
        print(f'{i}...', end= ' ')
print(f'\nO menor valor inserido foi: {menor} nas posições. ', end= ' ')
for i, v in enumerate(valores):
    if v == menor:
        print(f'{i}...',end = ' ')
