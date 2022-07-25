valores = list()

while True:
    n = (int(input('Digite um valor: ')))
    if n not in valores:
        valores.append(n)
        print('Valor adicionado com sucesso. ')
    else:
        print('Valor inválido. Tente novamente. ')
    resp = str(input('Deseja continuar? [S/N]: ')).strip().upper()
    if resp == 'N':
        break
print('-'*54)
print(f' Os valores adicionados foram {sorted(valores)} ')
print(' '*8, 'PROGRAMA FINALIZADO PELO OPERADOR. ')

