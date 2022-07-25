maior = menor = 0
valores = []

for c in range(0,5):
    valores.append(int(input(f'Digite o valor da posição {c}: ')))
    if c == 0:
        maior = menor = valores[c]
    else:
        if valores[c] > maior:
            maior = valores[c]
        if valores[c] < menor:
            menor = valores[c]
print('-'*54)
print(f'Você inseriu {valores}. ')
print(f'O maior número econtrado foi {maior} e está nas posições ', end= ' ')
for i, v, in enumerate(valores):
    if v == maior:
        print(f'{i} ... ', end= ' ')
print(f'\nO menor número encontrado foi {menor} e está nas posições ', end= ' ')
for i, v in enumerate(valores):
    if v == menor:
        print(f'{i} ... ')
