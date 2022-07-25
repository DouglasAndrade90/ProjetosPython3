from datetime import date
print('='*54)
print(' '*14, 'FORÇAS ARMADAS BRASILEIRAS - FFAA ')
print(' '*18, 'Braço forte, mão amiga')
print('='*54)
nome = str(input('Digite seu nome completo: '))
data_nascimento = int(input('Digite o ano de seu nascimento: '))
idade = date.today().year - data_nascimento
alistamento = idade - 18
if idade < 18:
    alistamento = 18 - idade
if idade > 18:
    alistamento = idade - 18
nome = nome.split()
print(f'Prezado Sr. {(nome [0])}, ')
if idade == 18:
    print(f'\033[1:32mVocê tem {idade} ano e deve se alistar esse ano nas Forças Armadas.\033[m ')
elif idade < 18:
    print(f'\033[1;33mVocê tem {idade} anos e não está na faixa etária para alistamento.\033[m ')
    print(f'Ainda restam {alistamento} ano(s) para o alistamento. ')
elif idade > 18:
    print(f'\033[1:31mVocê tem {idade} anos e já se passou {alistamento} ano(s) para o alistamento.\033[m ')

