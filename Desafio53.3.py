soma = 0
media = 0
maisvelhomasculino = 0
maisvelhofeminino = 0
nomevelhomasculino = ''
nomevelhofeminino = ''
menorfeminino = 0
contfem = 0
print('='*54)
print(' '*16, 'ANALISADOR DE IDADE')
print('='*54)
for c in range (1,5):
    print(f'------ DADOS DA {c}ª PESSOA ------ ')
    nome = str(input('NOME: ')).strip()
    idade = int(input('IDADE: '))
    sexo = str(input('SEXO [M/F]: ')).strip()
    soma = soma + idade

    if c == 1 and sexo in 'Mm':
        maisvelhomasculino = idade
        nomevelhomasculino = nome
    if sexo in 'Mm' and idade > maisvelhomasculino:
        maisvelhomasculino = idade
        nomevelhomasculino = nome
        print('-'*54)

    if c == 1 and sexo in 'Ff':
        maisvelhofeminino = idade
        nomevelhofeminino = nome
    if sexo in 'Ff' and idade > maisvelhofeminino:
        maisvelhofeminino = idade
        nomevelhofeminino = nome
        print('-'*54)

    if menorfeminino == 1 and sexo in 'Ff':
        menorfeminino < idade
        menorfeminino = idade
    if sexo in 'Ff' and menorfeminino < 20:
        menorfeminino = idade
        contfem = contfem + 1
        print('-'*54)

media = soma / 4

print(f'A idade média do grupo inserido é de {media} anos. ')
if maisvelhomasculino > 1:
    print(f'O homem mais velho do grupo inserido é {nomevelhomasculino} e ele tem {maisvelhomasculino} anos. ')
if maisvelhofeminino > 1:
    print(f'A mulher mais velha do grupo inserido é {nomevelhofeminino} e ela tem {maisvelhofeminino} anos. ')
if menorfeminino > 1:
    print(f'Existem {contfem} pessoas menor(es) de 20 ano(s) no grupo inserido. ')
print('-'*22, 'ENCERRADO', '-'*22)