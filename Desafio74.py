print('='*54)
print(' '*17, 'SORTEIO ALEATÓRIO')
print('='*54)

from random import randint
n = (randint(0,9), randint(0,9), randint(0,9), randint(0,9), randint(0,9))
print(f'Os números sorteados foram: {n}. ')
print(f'O maior número encontrado foi: {max(n)}. ')
print(f'O menor número sorteado foi : {min(n)}. ')




