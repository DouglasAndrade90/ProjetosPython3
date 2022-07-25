nome = str(input('Digite seu nome: '))
if nome == 'Douglas':
    print('Que nome lindo!')
elif nome == 'João' or nome == 'Pedro' or nome == 'Leandro':
    print('Seu nome é um nome muito popular!')
elif nome in 'Juliana Bianca Margarida':
    print('Belo nome feminino!')
else:
    print('Seu nome é bem normal!')
print('Tenha um bom dia {}!' .format(nome))