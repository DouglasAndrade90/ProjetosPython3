import random
band1 = str(input('what is the name of the first band? '))
band2 = str(input('What is the name of the second band? '))
band3 = str(input('What is the name of the thirst band? '))
band4 = str(input('What is the name of the fourth band? '))
list = [band1, band2, band3, band4]
chosen = random.choice(list)
print('And the chosen band it was: {}'.format(chosen))