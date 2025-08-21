while True:
            follow = input('The killer is leading you down the alley ways, will you call for backup or go it alone? \n    1. call for backup\n    2. go it alone \n Enter a number: ')
            if follow == '1':
                clearscreen()
                print(Fore.RED, intro['breakspace'])
                print(Fore.YELLOW, 'The Arrest Ending')
                print(Fore.RED, intro['breakspace'])
                print()
                print(Fore.WHITE, "   By calling for backup when the killer tried to overpower you, you had a helping hand to take control of the situation and were able to make the arrest. You put the guy right back behind bars, you are a hero! Congradulations!")
                exit()
            elif follow == '2':
                print()
                print(Fore.WHITE, 'You continue following the killer for some time.')
                print('When the killer begins to slow and reach for something, you have two options:\n     1. Pull your gun first\n    2. Wait and see what he is doing')
                while True:
                    what = input('What will you do? Enter your answer number: ')
                    if what == '1':
                        clearscreen()
                        print(Fore.RED, intro['breakspace'])
                        print(Fore.YELLOW, 'The Murderers Ending')
                        print(Fore.RED, intro['breakspace'])
                        print()
                        print(Fore.WHITE, 'You pulled your gun and shot the killer first. \n While your boss was unhappy, it was self defence and rid the world of a dangerous man.')
                        exit()
                    elif what == '2':
                        clearscreen()
                        print(Fore.RED, intro['breakspace'])
                        print(Fore.YELLOW, 'The Cowards Ending')
                        print(Fore.RED, intro['breakspace'])
                        print()
                        print(Fore.WHITE, "You failed to pull your gun and got shot. \n Your boss had cause to fire you because you didn't call for backup. \n \n Enjoy being unemployed!")
                        exit()
                    else:
                        print('Try again')
                        
            else:
                print("Try again")



def whatifelse():
    while True:
        what = input('What will you do? Enter your answer number: ')
        if what == '1':
            clearscreen()
            print(Fore.RED, intro['breakspace'])
            print(Fore.YELLOW, 'The Murderers Ending')
            print(Fore.RED, intro['breakspace'])
            print()
            print(Fore.WHITE, 'You pulled your gun and shot the killer first. \n While your boss was unhappy, it was self defence and rid the world of a dangerous man.')
            exit()
        elif what == '2':
            clearscreen()
            print(Fore.RED, intro['breakspace'])
            print(Fore.YELLOW, 'The Cowards Ending')
            print(Fore.RED, intro['breakspace'])
            print()
            print(Fore.WHITE, "You failed to pull your gun and got shot. \n Your boss had cause to fire you because you didn't call for backup. \n \n Enjoy being unemployed!")
            exit()
        else:
            print('Try again')