print('='*54)
print(' '*22, 'Inicio')
print('='*54)

sexo = 'F', 'M'
while sexo != 'F' and sexo != 'M':
    sexo = str(input('Digite o sexo: [M/F] ')).strip().upper()
    if sexo != 'F' and sexo != 'M':
        print('Opção inválida. ')
        print('-'*54)

if sexo == 'M' or sexo == 'F':
    print('Opção aceita. ')
print('-'*22, 'FINALIZADO', '-'*22)





