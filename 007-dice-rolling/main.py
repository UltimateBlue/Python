import random


while True:
    i = round(float(input('Enter a random number: ')))

    random.seed(i)
    num = random.random()
    if num<0.5:
        print('Head')
    else:
        print('Tail')
    
    if input('Do you want to continue: (Y/N) ').lower == 'n':
        break



