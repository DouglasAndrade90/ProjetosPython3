tabela = ('Palmeiras', 'Atlético MG', 'Corinthians', 'Internacional',
'Fluminense', 'Atlético PR', 'Flamengo', 'Bragantino', 'São Paulo',
'Santos', 'Bota-Fogo', 'Avaí', 'Goiás', 'Ceará SC', 'Cuiabá', 'Coritiba',
'América MG', 'Atlético GO', 'Fortaleza', 'Juventude')

'''print('='*54)
print(' '*17, 'TABELA BRASILEIRÃO')
print('='*54)

print(tabela)

print(f'Os cinco primeiros colocados são:{tabela[:5]}')
print('-'*54)

print(f'Os quatro últimos colocados são {tabela[-4:]}')
print('-'*54)

print(f'A organização dos times em ordem alfabética é: \n', sorted(tabela))
print('-'*54)

i = tabela.index('Bragantino')
print(f'O Bragantino se encontra na {i+1}ª posição')'''



tabela = ('Palmeiras', 'Atlético MG', 'Corinthians', 'Internacional',
'Fluminense', 'Atlético PR', 'Flamengo', 'Bragantino', 'São Paulo',
'Santos', 'Bota-Fogo', 'Avaí', 'Goiás', 'Ceará SC', 'Cuiabá', 'Coritiba',
'América MG', 'Atlético GO', 'Fortaleza', 'Juventude')

print('='*54)
print(' '*12, 'TABELA CAMPEONATO BRASILEIRO')
print('='*54)

print(tabela)
print('-'*54)

print(f'Os cinco primeiros colocados são\n {tabela[0:5]}. ')
print('-'*54)

print(f'Os quatro últimos colocados são\n {tabela[-4:]}. ')
print('-'*54)


print(sorted(tabela))
print('-'*54)

i = tabela.index('São Paulo')
print(f'O São Paulo se encontra na posição {i+1}ª posição. ')


