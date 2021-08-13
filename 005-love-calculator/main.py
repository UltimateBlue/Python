yourName = input('What\'s your name: ').lower()
theirName = input('What\'s his/her name: ').lower()


firstDig = 0
secDig = 0

name = yourName+theirName

for c in name:
    if c=='t' or c == 'r' or c == 'u' or c == 'e':
        firstDig+=1
    if c == 'l' or c == 'o' or c == 'v' or c == 'e':
        secDig+=1

print('your love index is '+str(firstDig)+str(secDig))