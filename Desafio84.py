maispesado = maisleve = 0
pessoas = []
dados = []
cont = 0
while True:
    dados.append(str(input('Digite o nome: ')).strip().capitalize())
    dados.append(float(input('Digite o peso: ')))
    if len(pessoas) == 0:
        maispesado = maisleve  = dados[1]
    else:
        if dados[1] > maispesado:
            maispesado = dados[1]
        if dados[1] < maisleve:
            maisleve = dados[1]
    pessoas.append(dados[:])
    dados.clear()
    resp = str(input('Deseja continuar? [S/N]: ')).strip().upper()
    if resp == 'N' or resp != 'S':
        break
    print('-'*54)
print()
print(f'Foram cadastradas {len(pessoas)}. ')
print(f'O maior peso foi {maispesado} kg. Peso de ', end= ' ')
for p in pessoas:
    if p[1] == maispesado:
        print(f'[{p[0]}]')
print(f'O menor peso foi {maisleve}. ', end=' ')
for p in pessoas:
    if p[1] == maisleve:
        print(f'[{p[0]}]. ', end=' ')
print()

