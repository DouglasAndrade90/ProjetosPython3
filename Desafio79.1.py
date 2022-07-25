print('='*54)
print(' '*17, ' ANALISANDO VALORES')
print('='*54)

valores = list()
maior = menor = 0

while True:
    n = int(input('Digite um número: '))
    if n not in valores:
        valores.append(n)
        print('Número adicionado com sucesso. ')
    else:
        print('Número inválido! Tente novamente. ')
    for i, v in enumerate(valores):
        if i == 0:
            maior = menor = valores[i]
        else:
            if valores[i] > maior:
                maior = valores[i]
            if valores[i] < menor:
                menor = valores[i]
    resp = str(input('Deseja continuar? [S/N]: ')).strip().upper()
    if resp == 'N' or resp != 'S':
        break
    print('-'*54)

print('='*54)
print(f'Os números inseridos foram {sorted(valores)}. ')
print(f'O maior valor inserido foi {maior} e está na posição', end=' ')
for i, v in enumerate(valores):
    if v == maior:
        print(f'{i+1}...', end=' ')
print(f'\nO menor valor inserido foi {menor} e está na posição', end=' ')
for i, v in enumerate(valores):
    if v == menor:
        print(f'{i+1}...', end=' ')