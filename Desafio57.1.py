print('='*54)
print(' '*22, 'IDENTIFICADOR')
print('='*54)

sexo = 'F', 'M'
while sexo != 'F' and sexo != 'M':
    sexo = str(input('Digite o sexo [M/F]: ')).strip().upper()
    if sexo != 'F' and sexo != 'M':
        print('OPÇÃO INVÁLIDA! TENTE NOVAMENTE. ')
        print('-'*54)

if sexo == 'F' or sexo == 'M':
    print('OPÇÃO ACEITA! ')
print('-'*21, 'FINALIZADO', '-'*21)