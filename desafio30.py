n = int(input('\033[1;30;47mDigite um número qualquer:\033[m '))
if n % 2 == 0:
    print('\033[1;34;40mO número {} é PAR.\033[m '.format(n))
else:
    print('\033[1;31;40m O número {} é IMPAR.\033[m '.format(n))
