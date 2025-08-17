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