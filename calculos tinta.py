A = float(input('Digite a altura da parede (Mts): '))
H = float(input('Digite a largura da parede (Mts): '))
s = A * H
r = s / 2
print('A parede mede : {} m² e serão necessárias {} litros de tintas para pintá-las'.format(s, r))