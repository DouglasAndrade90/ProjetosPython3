valores = list()
maior = menor = 0
for c in range(0,5):
    valores.append(int(input(f'Digite um valor para a posição {c}: ')))
    if c == 0:
        maior = menor = valores[c]
    else:
        if valores[c] > maior:
            maior = valores[c]
        if valores[c] < menor:
            menor = valores[c]
print('-' * 54)
print(f'O valores inseridos foram {sorted(valores)}. ')
print(f'O menor valor encontrado foi {menor} e está localizado na posção ', end=' ')
for c, v in enumerate(valores):
    if v == menor:
        print(f'{c+1}...', end=' ')
print(f'\nO maior valor encontrado foi {maior} e está localizado na posição ', end= ' ')
for c, v in enumerate(valores):
    if v == maior:
        print(f'{c+1}...', end=' ')






