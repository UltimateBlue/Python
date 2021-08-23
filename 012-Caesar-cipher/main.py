alphabets = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

while True:
    codingType = input('for encoding type "e"\nfor decoding type "d"\nEnter your choise: ').lower()
    message = input('Write your message:').lower()
    shiftNum = int(input('Enter your desired shift number: '))
    coded = ''

    for c in message:
        i = alphabets.index(c)
        if codingType == 'e':
            newIndex = i+shiftNum if i+shiftNum<26 else i+shiftNum-26
        elif codingType == 'd':
            newIndex = i-shiftNum if i-shiftNum>=0 else 26 + i-shiftNum

        coded +=alphabets[newIndex]
    print(coded)
    contin = input('Do you want to continue? (Y/N) ').lower()
    if contin == 'n':
        break



