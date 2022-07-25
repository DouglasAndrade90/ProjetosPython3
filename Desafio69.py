from datetime import date

resp = ''
homens = 0
mulheres = 0
maiores = 0
menores = 0
sexo = ''

while True:
    if resp == 'N':
        break
    idade = int(input('Digite a idade: '))
    while sexo != 'M' or sexo != 'F':
        sexo = str(input('Digite o sexo [M/F]: ')).strip().upper()
        if sexo == 'M' or sexo == 'F':
            break
    resp = str(input('Deseja continuar? [S/N] ')).strip().upper()
    print('-'*54)

    if idade >= 18:
        maiores += 1

    if sexo == 'M':
        homens += 1

    if sexo == 'F':
        mulheres += 1

    if idade < 20 and sexo == 'F':
        menores += 1

print(f'Foram cadastrados {maiores} pessoa(as) acima de 18 anos. ')
print(f'Foram encontrados {homens} homem(s) cadastrados. ')
print(f'Foram encontradas {menores} mulher(es) menores de 20 anos cadastradas. ')