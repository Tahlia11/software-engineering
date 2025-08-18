print(Fore.RED, intro['breakspace'], Fore.YELLOW)
        animate('              Puzzle Room')
        print(Fore.RED, intro['breakspace'])
        print()
        print(puzzle2['opening'])
        print('')
        print(Fore.WHITE, mail['second'])
        print()
        print(puzzle1['where'])
        print(puzzle2['items'])
        answer2 = input("Please enter the number of your answer:")
        if answer2 == '1':
            print(clearscreen())
            print(Fore.LIGHTGREEN_EX, 'Correct! +5 health \n')
            print(Fore.WHITE, "The last victims jacket has the answers to who BOBBI is. Let's go to the alley.")
            health =health + 5
            print(f'Your health is now {health}')
            print(endscene())
            while True:
                print(clearscreen)
                print(churchv2())
                print(chifelse2())
        elif answer2 =='2':
            print(clearscreen())
            print(Fore.RED, "You are wrong. The exhaustion of figuring this out has taken a toll on you -5 health \n") 
            print(Fore.WHITE, 'Now that you know what it is not, re-attempt the question and find the next clue.')
            health = health - 5
            print(f'Your health is now {health}')
            print(endscene())
            print(churchv1())
            print(chifelse1)
        elif answer2 == '3':
            print(clearscreen())
            print(Fore.RED, "You are wrong. The exhaustion of figuring this out has taken a toll on you -5 health \n") 
            print(Fore.WHITE, 'Now that you know what it is not, re-attempt the question and find the next clue.')
            health = health - 5
            print(f'Your health is now {health}')
            print(endscene())
            print(churchv1())
            print(chifelse1)






print(clearscreen())
        print(Fore.RED, intro['breakspace'], Fore.YELLOW)
        animate('              Puzzle Room')
        print(Fore.RED, intro['breakspace'])
        print('')
        print(Fore.WHITE, mail['your first letter'])
        print('')
        print(puzzle1['where'])
        print('')
        print(puzzle1['locations'])
        answer_1 = input("Please enter the number of you answer: ")
        if answer_1 == '1':
            clearscreen()
            print(Fore.RED, "You are wrong. The exhaustion of figuring this out has taken a toll on you -5 health \n") 
            print(Fore.WHITE, 'Now that you know what it is not, re-attempt the question and find the next clue.')
            health = health - 5
            print(f'Your health is now {health}')
            print(endscene())
            print(officev2())
            inter = input(str("What would you like to do? / Where would you like to go?"))
            print(offifelse1())
        elif answer_1 == '2':
            print(clearscreen())
            print(Fore.LIGHTGREEN_EX, 'Correct! +5 health \n')
            print(Fore.WHITE, 'The killer is leading you to the church! We have to get there quickly to find the next clue.')
            health =health + 5
            print(f'Your health is now {health}')
            print(endscene())
            while True:
                office1()
                print(offifelse2)
        elif answer_1 == '3':
            health = 100
            print(Fore.RED, "You are wrong. The exhaustion of figuring this out has taken a toll on you -5 health \n") 
            print(Fore.WHITE, 'Now that you know what it is not, re-attempt the question and find the next clue.')
            health =health - 5
            print(f'Your health is now {health}')
            print(endscene())
            officev2()
            inter = input(str("What would you like to do? / Where would you like to go?")) 
            print(offifelse1())


inter = input(str("What would you like to do? / Where would you like to go?"))
    if inter == "help me":
        print(clearscreen())
        print(helpme())
        print(endscene())

    elif inter == "commands":
        print(clearscreen())
        print(commandsss())

    elif inter == "map":
        print(clearscreen())
        print(mapp())
        print(endscene())

    elif inter == "mail":
        print(clearscreen())
        print(letters())
        print(endscene())

    elif inter == "puzzle":
        print(puzzlerun1())

    elif inter == "the beach":
        print(clearscreen())
    
    elif inter == "the church":
        print(clearscreen())
        print(room())
        print(churchv1())
        inter = input(str("What would you like to do? / Where would you like to go?"))
        if inter == 'help me':
            print(clearscreen())
            print(helpme())
            print(endscene())
        elif inter == 'commands':
            print(clearscreen())
            print(commandsss())
            print(endscene())
        elif inter == 'map':
            print(clearscreen())
            print(mapp())
            print(endscene())
        elif inter == 'mail':
            print(clearscreen())
            print(letters())
            print(endscene())
        elif inter == 'puzzle':
            print(clearscreen())
            mail.update({'second': "Hello again Detective, \nI hope you have found the gift I have left for you. Do take good care of it, I'll be sending some people to collect it when i'm ready to put it to good use. Don't you just love my addition to the handle, I hope BOBBI is not a bore, I just hate a bad time. But I love a good chase, to get to BOBBI before me, the alley holds the answers. Find the item with pockets big enought to hold a knife but too small to hold a textbook."})
            print(puzzlerun2())
        elif inter == 'the precinct':
            print(clearscreen())
            print(office1())
            print(offifelse2())#?????????????????????????????????????????????????????????????????????????????????????????????
        elif inter == 'the beach':
            print(clearscreen())

        elif inter == 'the back alley':
            print(clearscreen())
        
        else: 
            print('Try again')
    elif inter == "the back alley":
        print(clearscreen())

    else:
        print(Fore.WHITE, "Try again")


def offifelse2():#options of where to go if they have already done the puzzle
    inter = input(str("What would you like to do? / Where would you like to go?"))
    if inter == "help me":
        print(clearscreen())
        print(helpme())
        print(endscene())

    elif inter == "commands":
        print(clearscreen())
        print(commandsss())

    elif inter == "map":
        print(clearscreen())
        print(mapp())

    elif inter == "mail":
        print(clearscreen())
        print(letters())

    elif inter == "puzzle":
        print('You have already successfully completed the puzzle from this room, congrats! \n If you want to review the mail from the puzzle, please enter "mail"')

    elif inter == "the beach":
        print(clearscreen())
    
    elif inter == "the church":
        print(clearscreen())
        print(room())
        print(churchv1())
        inter = input(str("What would you like to do? / Where would you like to go?"))
        if inter == 'help me':
            print(clearscreen())
            print(helpme())
            print(endscene())
        elif inter == 'commands':
            print(clearscreen())
            print(commandsss())
            print(endscene())
        elif inter == 'map':
            print(clearscreen())
            print(mapp())
            print(endscene())
        elif inter == 'mail':
            print(clearscreen())
            print(letters())
            print(endscene())
        elif inter == 'puzzle':
            print(clearscreen())
            mail.update({'second': "Hello again Detective, \nI hope you have found the gift I have left for you. Do take good care of it, I'll be sending some people to collect it when i'm ready to put it to good use. Don't you just love my addition to the handle, I hope BOBBI is not a bore, I just hate a bad time. But I love a good chase, to get to BOBBI before me, the alley holds the answers. Find the item with pockets big enought to hold a knife but too small to hold a textbook."})
            print(puzzlerun2())
        elif inter == 'the precinct':
            print(clearscreen())
            print(office1())
            print(offifelse2())#?????????????????????????????????????????????????????????????????????????????????????????????
        elif inter == 'the beach':
            print(clearscreen())

        elif inter == 'the back alley':
            print(clearscreen())
        
        else: 
            print('Try again')
    elif inter == "the back alley":
        print(clearscreen())

    else:
        print(Fore.WHITE, "Try again")