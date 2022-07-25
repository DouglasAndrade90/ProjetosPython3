maisleve = maispesado = 0
dados = []
pessoas = []

print('='*54)
print(' '*17, 'ANALISE DE PESOS')
print('='*54)

while True:
    dados.append(str(input('NOME: ')).strip().capitalize())
    dados.append(float(input('PESO: ')))

    if len(pessoas) == 0:
        maispesado = maisleve = dados[1]
    else:
        if dados[1] > maispesado:
            maispesado = dados[1]
        if dados[1] < maisleve:
            maisleve = dados[1]

    pessoas.append(dados)
    dados.clear()
    resp = str(input('Deseja continuar? [S/N]: ')).strip().upper()
    if resp == 'N' or resp != 'S':
        break

print('-'*54)
print(f'Ao todo foram cadastrados {len(pessoas)} pessoas. ')
print(f'O maior peso encontrado foi {maispesado}. Peso de ', end=' ')

for p in pessoas:
    if p[1] == maispesado:
        print(f'[{p[0]}]', end=' ')

print(f'O menor peso encontrado foi {maisleve} . Peso de ', end=' ')
for p in pessoas:
    if p[1] == maisleve:
        print(f'[{p[0]}', end=' ')

print()