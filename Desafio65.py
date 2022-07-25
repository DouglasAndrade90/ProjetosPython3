print('='*54)
print(' '*8, 'CALCULADORA DE MEDIA, MAIOR E MENOR')
print('='*54)

menor = 0
maior = 0
cont = 0
s = 0
resposta = 'S'

while resposta == 'S':
    n = int(input('Digite um número: '))
    resposta = str(input('Deseja continuar a inserir dados? [S/N] ')).strip().upper()
    s += n
    cont += 1
    if cont == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
media = s / cont

print('-'*54)
print(f'Foram inseridos {cont} números. ')
print(f'A soma dos valores inseridos foi de {s}. ')
print(f'A média dos valores inseridos foi de {media}. ')
print(f'O maior número inserido foi {maior}. ')
print(f'O menor número inserido foi {menor}. ')
print('-'*54)