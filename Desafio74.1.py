print('='*54)
print(' '*17, 'SORTEIO ALEATÓRIO')
print('='*54)

from datetime import datetime
from random import randint
time = str(datetime.now().time())[:8]

n = (randint(0, 9), randint(0, 9), randint(0, 9), randint(0, 9), randint(0 ,9))
print(f'Os números sorteados foram {n}. ')
print(f'O maior número sorteado foi: {max(n)}. ')
print(f'O menor número sorteado foi: {min(n)}. ')
print('-'*54)
print('       OBRIGADO POR UTILIZAR NOSSOS SERVIÇOS')
print(time)