print('Small Pizza: $15\nMedium Pizza: $20\nLarge Pizza: $25')
print('\n#################################')

print('Pepperoni for small pizza: +$2')
print('Pepperoni for medium or large pizza: +$3')

print('Extra cheese for all sizes: +$1')
print('\n#################################')

siz = input('Choose your pizza size: (S/M/L) ')
pep = input('Do you want pepperoni in your pizza: (Y/N) ')
chiz = input('Do you want extra cheeze: (Y/N) ')
print('\n#################################')
total = 0
if siz == 'S' or siz == 's':
    if pep == 'Y' or pep== 'y':
        if chiz=='Y' or chiz == 'y':
            total = 15+2+1
        else:
            total = 15+2
    else:
        if chiz=='Y' or chiz == 'y':
            total = 15+1
        else:
            total = 15
else:
    if pep == 'Y' or pep== 'y':
        if chiz=='Y' or chiz == 'y':
            total = 3+1
        else:
            total = 3
    else:
        if chiz=='Y' or chiz == 'y':
            total = 1
        else:
            total = 0
    if siz == 'M' or 'm':
        total +=20
    else:
        total+=25

print('Your bill is $' + str(total))



