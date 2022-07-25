maisvelhomasculino = 0
maisvelhofeminino = 0
nomevelhomasculino = ''
nomevelhofeminino = ''
menorfeminino = 0
contfem = 0
soma = 0
media = 0
print('='*54)
print(' '*19, 'DADOS PESSOAIS' )
print('='*54)
for c in range (1,5):
    print(f'Informações da {c}ª pessoa: ')
    nome = str(input('NOME: ')).strip()
    idade = int(input('IDADE: '))
    sexo = str(input('SEXO [M/F]: '))
    soma = soma + idade
    print('-'*54)

    if c == 1 and sexo in 'Mm':
        maisvelhomasculino = idade
        nomevelhomasculino = nome
    if sexo in 'Mm' and idade > maisvelhomasculino:
        maisvelhomasculino = idade
        nomevelhomasculino = nome

    if c == 1 and sexo in 'Ff':
        maisvelhofeminino = idade
        nomevelhofeminino = nome
    if sexo in 'Ff' and idade > maisvelhofeminino:
        maisvelhofeminino = idade
        nomevelhofeminino = nome

    if menorfeminino == 1  and sexo in 'Ff':
        menorfeminino < idade
        menorfeminino = idade
    if sexo in 'Ff' and idade < 20:
        menorfeminino = idade
        contfem = contfem + 1

media = soma / 4
print(f'A idade média do grupo informado é de {media} ano(s). ')
if maisvelhomasculino > 1:
    print(f'O homem mais velho do grupo é {nomevelhomasculino} e ele tem {maisvelhomasculino} ano(s). ')
print(f'A mulher mais velha do grupo é {nomevelhofeminino} e ela tem {maisvelhofeminino} ano(s). ')
print(f'Existem {contfem} mulheres menor(es) de 20 anos no grupo. ')

print('-'*22, 'ENCERRADO', '-'*22)





