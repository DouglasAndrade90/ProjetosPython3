nome = str(input('Digite seu nome completo: ').strip())
print('Seu nome em letras maiúsculas é: {}'.format(nome.upper()))
print('Seu nome em letras minúsculas é: {}'.format(nome.lower()))
print('Seu nome possui ao todo {} letras.'.format(len(nome) - nome.count(' ')))
separa = nome.split()
print('Seu primeiro nome é {} e possui {} letras.'.format(separa[0], len(separa[0])))







