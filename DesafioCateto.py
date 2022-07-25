import math
cop = float(input('Qual o comprimento do cateto oposto? '))
caa = float(input('Qual o comprimento do cateto adjacente? '))
hi = math.hypot(cop, caa)
print('A hipotenusa mede: {:.2f}'.format(hi))

