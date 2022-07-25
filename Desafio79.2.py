print('='*54)
print(' '*17, 'ANALISE DE VALORES')
print('='*54)

maior = menor = 0
valores = list()

while True:
    n = int(input('Digite um número: '))
    if n not in valores:
        valores.append(n)
        print('Número adicionado com sucesso. ')
    else:
        print('Número inválido! Tente novamente. ')
    for c, v in enumerate(valores):
        if c == 0:
            maior = menor = valores[c]
        else:
            if valores[c] > maior:
                maior = valores[c]
            if valores[c] < menor:
                menor = valores[c]
    resp = str(input('Deseja continuar? [S/N]: ')).strip().upper()
    if resp == 'N':
        break
    print('FINALIZADO PELO OPERADOR. ')
    print('-' * 54)
print('-'*54)
print(f'Os números inseridos foram {sorted(valores)}. ')
print(f'O maior número inserido foi {maior}. Sua posição é a :', end=' ')
for c, v in enumerate(valores):
    if v == maior:
        print(f'{c+1}ª...', end=' ')
print(f'\nO menor número inserido foi {menor}. Sua posição é a:', end=' ')
for c, v in enumerate(valores):
    if v == menor:
        print(f'{c+1}ª...', end=' ')