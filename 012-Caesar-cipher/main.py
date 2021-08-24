alphabets = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

while True:
    codingType = input('for encoding type "e"\nfor decoding type "d"\nEnter your choise: ').lower()
    message = input('Write your message:').lower()
    shiftN = input('Enter your desired shift number: ')
    if not shiftN.isnumeric():
        print('Enter a valid number!')
        continue

    shiftNum = int(shiftN)
    coded = ''

    for c in message:
        if not c.isalpha():
            coded += c
            continue
        i = alphabets.index(c)
        if codingType == 'e':
            newIndex = i+(shiftNum%25) if i+(shiftNum%25)<26 else i+(shiftNum%25)-26
        elif codingType == 'd':
            newIndex = i-(shiftNum%25) if i-(shiftNum%25)>=0 else 26 + i-(shiftNum%25)
        else:
            print('you did not select any encryption!! ooops..')
            break
        coded +=alphabets[newIndex]
    print(coded)
    contin = input('Do you want to continue? (Y/N) ').lower()
    if contin == 'n':
        break



