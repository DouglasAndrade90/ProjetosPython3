numeros = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez',
'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')

while True:
    escolha = int(input('Digite um número entre 0 e vinte: '))
    if escolha < 0 or escolha > 20:
        print('Opção inválida, tente novamente ')
    else:
        print(f'Você escolheu {numeros[escolha]}. ')
    resp = str(input('Deseja continuar? [S/N] ')).strip().upper()
    if resp == 'N':
        break
print('-'*54)
print(' '*11, 'FINALIZADO PELO OPERADOR')
