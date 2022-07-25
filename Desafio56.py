maioridadehomem = 0
nomevelho = ''
soma = 0
media = 0
contfeminino = 0
print('='*53)
print(' '*18, 'IBGE SENSO 2022')
print('='*53)
for c in range (1,5):
    print(f'------- {c}ª PESSOA -------')
    nome = str(input('NOME: ')).strip()
    idade = int(input('IDADE: '))
    sexo = str(input('SEXO [M/F]: '))
    soma = soma + idade
    if c == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        contfeminino += 1
media = soma / 4
print('-'*53)
print(f'O homem mais velho do grupo tem {maioridadehomem} anos e se chama {nomevelho}. ')
print(f'Existem {contfeminino} pessoas do sexo feminino no grupo abaixo de 20 anos. ')

