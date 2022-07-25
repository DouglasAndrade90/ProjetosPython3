import math
angulo = float(input('Digite o ângulo: '))
seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))
print('Para o ângulo de {} temos: \n SENO{:.2f}\n COSSENO {:.2f}\n TANGENTE {:.2f}'.format(angulo,seno, cosseno, tangente))
