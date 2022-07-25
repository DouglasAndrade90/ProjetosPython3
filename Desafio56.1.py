media = 0
maiormasculino = 0
maiorfeminino = 0
menorfeminino = 0
contmenorfeminino = 0
nomevelhomasculino = ''
nomevehofeminino = ''
soma = 0
media = 0
print('='*53)
print(' '*17, 'ANALISADOR PESSOAL')
print('='*53)

for c in range (1,5):
    print(f'Dados da {c}ª pessoa: ')
    nome = str(input('NOME: ')).strip()
    idade = int(input('IDADE: '))
    sexo = str(input('SEXO [M/F]: ')).strip()
    print('-'*53)
    soma = soma + idade

    if c == 1 and sexo in 'Mm':
        maiormasculino = idade
        nomevelhomasculino = nome
    if sexo in 'Mm' and idade > maiormasculino:
        maiormasculino = idade
        nomevelhomasculino = nome


    if c == 1 and sexo in 'Ff':
        maiorfeminino = idade
        nomevelhofeminino = nome
    if sexo in 'Ff' and idade > maiorfeminino:
        maiorfeminino = idade
        nomevelhofeminino = nome

media = soma / 4
print(f'A média de idade do grupo é de: {media} anos. ')
print(f'O homem mais velho do grupo tem {maiormasculino} anos e se chama {nomevelhomasculino}. ')
print(f'A mulher mais velha do grupo tem {maiorfeminino} anos e se chama {nomevelhofeminino}. ')
print(f'Existem {contmenorfeminino} mulher(s) menore(s) de 20 anos no grupo. ')
print('-' * 53)


