nome = str(input('Digite seu nome completo: ')).upper().strip()
print('Seu nome possui {} letras A'.format(nome.count('A')))
print('A primeira letra A se encontra na posição {} '.format(nome.find('A') + 1))
separa = nome.split()
print('A última letra A aparece na posição {}'.format(nome.rfind('A')+1))


