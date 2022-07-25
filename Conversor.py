n = float(input('Digite uma distância em metros: '))
km = n / 1000
hm = n / 100
dam = n / 10
dm  = n * 10
cm = n * 100
mm = n * 1000
print('A medida de {} m corresponde à:'.format(n))
print(' {}km \n {} hm \n {} dam \n {:.0f} dm \n {:.0f} cm \n {:.0f} mm'.format(km, hm, dam, dm, cm, mm))