print('='*54)
print(' '*17, 'ANALISE DE VALORES ')
print('='*54)

valores = [[], []]
dados = []
for c in range(1,8):
    dados = int(input(f'Digite o {c}º valor: '))
    if dados % 2 == 0:
        valores[0].append(dados)
    else:
        valores[1].append(dados)

print('-'*54)
print(f'Os valores ímpares inseridos foram {sorted(valores[1])}. ')
print(f'Os valores pares inseridos foram {sorted(valores[0])}. ')
print('-'*54)
print(' '*21, 'FINALIZADO')




