print('='*52)
print(' '*20, 'BHTRANS')
print(' '*12, ' AFERIDOR DE VELOCIDADE ')
print('='*52)
maior = 0
menor = 0
for c in range (1, 6):
    velocidade = int(input(f'Digite a velocidade do {c}° veículo: Km/h '))
    if c == 1:
        maior = velocidade
        menor = velocidade
    else:
        if velocidade > maior:
            maior = velocidade
        if velocidade < menor:
            menor = velocidade
print('-'*52)
print(f'A maior velocidade aferida foi de \033[1;31m{maior}\033[m Km/h. ')
print(f'A menor velocidade aferida foi de \033[1;36m{menor}\033[m Km/h. ')
