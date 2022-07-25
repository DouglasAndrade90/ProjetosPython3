import random
n1 = str(input('Digite a primeira banda:' ))
n2 = str(input('Digite a segunda banda: '))
n3 = str(input('Digite a terceira banda: '))
n4 = str(input('Digite a quarta banda: '))
lista = [n1, n2, n3, n4]
random.shuffle(lista)
print('A ordem escolhida foi: ')
print(lista)