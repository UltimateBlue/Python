from random import randint



while True:
    choice = input('Rock / Paper / Sissor: ').lower()

    randChoice = randint(0,2)
    print(randChoice)

    if choice == 'rock' and randChoice ==0:
        print('You choose rock, I choose rock too! so no Winner!')
        con = input('Do you want to continue? (Y/N)').lower()
        if con == 'y':
            continue
        else:
            break
    elif choice == 'rock' and randChoice ==1:
        print('You choose rock, I choose paper too! so I\'m the winner!!')
        con = input('Do you want to continue? (Y/N)').lower()
        if con == 'y':
            continue
        else:
            break
    elif choice == 'rock' and randChoice ==2:
        print('You choose rock, I choose sissor too! so you are the winner!!')
        con = input('Do you want to continue? (Y/N)').lower()
        if con == 'y':
            continue
        else:
            break
    elif choice == 'paper' and randChoice ==0:
        print('You choose paper, I choose rock too! you are the Winner!')
        con = input('Do you want to continue? (Y/N)').lower()
        if con == 'y':
            continue
        else:
            break
    elif choice == 'paper' and randChoice ==1:
        print('You choose paper, I choose paper too! so no winner!!')
        con = input('Do you want to continue? (Y/N)').lower()
        if con == 'y':
            continue
        else:
            break
    elif choice == 'paper' and randChoice ==2:
        print('You choose paper, I choose sissor too! so I\'m the winner!!')
        con = input('Do you want to continue? (Y/N)').lower()
        if con == 'y':
            continue
        else:
            break
    elif choice == 'sissor' and randChoice ==0:
        print('You choose sissor, I choose rock too! so I\'m the Winner!')
        con = input('Do you want to continue? (Y/N)').lower()
        if con == 'y':
            continue
        else:
            break
    elif choice == 'sissor' and randChoice ==1:
        print('You choose sissor, I choose paper too! so you are winner!!')
        con = input('Do you want to continue? (Y/N)').lower()
        if con == 'y':
            continue
        else:
            break
    elif choice == 'sissor' and randChoice ==2:
        print('You choose sissor, I choose sissor too! so no winner!!')
        con = input('Do you want to continue? (Y/N)').lower()
        if con == 'y':
            continue
        else:
            break
    
    


