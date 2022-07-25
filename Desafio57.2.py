print('='*54)
print(' '*20, 'IDENTIFICADOR')
print('='*54)

sexo = 'M', 'F'
while sexo != 'M' and sexo != 'F':
    sexo = str(input('Digite o sexo [M/F]: ')).strip().upper()
    if sexo != 'M' and sexo != 'F':
        print('OPÇÃO INVÁLIDA! TENTE NOVAMENTE. ')
        print('-'*54)
if sexo == 'M' or sexo == 'F':
    print('OPÇÃO ACEITA! ')
print('-'*21, 'FINALIZADO', '-'*21)