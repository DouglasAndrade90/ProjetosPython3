print('='*53)
print(' '* 17, ' CONTADOR DE PESO ')
print('='*53)
maior = 0
menor = 0
for c in range (1, 8):
    peso = float(input(f'Digite o {c}° peso: '))
    if c == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('-'*54)
print(f'O maior peso encontrado foi: {maior} Kg. ')
print(f'O menor peso encontrado foi: {menor} Kg. ')