from random import randint
from random import choice
from string import ascii_letters
from string import punctuation


length = int(input('How long you want your password be? '))
digit_nums = int(input('How many digits you want your password has? '))
sym_nums = int(input('How many symbols you want your password has? '))

char_nums = length -digit_nums - sym_nums

password = [-1]*length;

l = length
while l>0:
    while digit_nums>0:
        dpos = randint(0,length-1)
        if password[dpos]==-1:
            password[dpos] = str(randint(0,9))
            digit_nums-=1
            l-=1
            break
    while sym_nums>0 and l>0:
        spos = randint(0,length-1)
        if password[spos]==-1:
            password[spos] = str(choice(punctuation))
            sym_nums-=1
            l-=1
            break
    while char_nums>0 and l>0:
        cpos = randint(0,length-1)
        if password[cpos]==-1:
            password[cpos] = choice(ascii_letters)
            char_nums-=1
            l-=1
            break
    
print(''.join(password))