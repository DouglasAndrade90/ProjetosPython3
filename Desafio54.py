from datetime import date
print('='*53)
print(' '*13, 'CALCULADORA DE MAIORIDADE')
print('='*53)
maior = 0
menor = 0
for c in range (1, 8):
    nasc = int(input(f'Digite o ano do {c}° nascimento: '))
    idade = date.today().year - nasc
    if idade >= 21:
        maior += 1
    elif idade < 21:
        menor += 1
print('-'*53)
print(f'{maior} pessoas já atingiram a maioridade. ')
print(f'{menor} pessoas ainda não atingiram a maioridade. ')





