import colorama
colorama.init()
from colorama import Fore, init
import os
import time 
from data import *

health = 100

attack_health = 100

def clearscreen():#MR GROOM HELPED WITH THIS ONE
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def endscene ():
    input('Hit "enter" to continue: ')
    clearscreen()

def animate (text):
    for letter in text:
        print(letter, end='', flush=True)
        time.sleep(0.1)
    print('')

#EVERY ROOM
def room(health):#non-specific info that goes into each room
    print(Fore.LIGHTMAGENTA_EX, inventory['message'])
    print(Fore.WHITE, inventory['items'])
    print('')
    print(f"Your current health is {health}")
    print(Fore.LIGHTMAGENTA_EX, commands['head'])
    print(Fore.WHITE, commands['all'])

def helpme ():#help function(gives hint and help)
    print(Fore.RED, intro['breakspace'], Fore.YELLOW)
    animate(f"{help['heading']}")
    print(Fore.RED, intro['breakspace'])
    print(Fore.LIGHTMAGENTA_EX, help['ahead'])
    print(Fore.WHITE, help['your aim'])
    print('')
    print(Fore.LIGHTMAGENTA_EX, help['chead'])
    print(Fore.WHITE, help['commands'])
    print('')
    print(Fore.LIGHTMAGENTA_EX, help['lhead'])
    print(Fore.WHITE, help['locations'])
    print('')
    print(Fore.LIGHTMAGENTA_EX, help['thead'])
    print(Fore.WHITE, help['tips'])
    print('')
    print(help['fail'])

def commandsss():#commands function(shows what commmands can be used)
    print(Fore.RED, intro['breakspace'],Fore.YELLOW)
    animate(f"{commandss['heading']}")
    print(Fore.RED, intro['breakspace'])
    print(Fore.LIGHTMAGENTA_EX, commandss['thead'])
    print(Fore.WHITE, commandss['travel'])
    print('')
    print(Fore.LIGHTMAGENTA_EX, commandss['ghead'])
    print(Fore.WHITE, commandss['game'])
    print('')
    print(Fore.LIGHTMAGENTA_EX, commandss['phead'])
    print(Fore.WHITE, commandss['puzzle'])
    print('')
    print(Fore.LIGHTMAGENTA_EX, commandss['bhead'])
    print(Fore.WHITE, commandss['battle'])

def mapp():#map function(displays locations and descriptions)
    print(Fore.RED, intro['breakspace'],Fore.YELLOW)
    animate(f"{map['heading']}")
    print(Fore.RED, intro['breakspace'])
    print(Fore.LIGHTMAGENTA_EX, offname)
    print(Fore.WHITE, offdes)
    print('')
    print(Fore.LIGHTMAGENTA_EX, bena)
    print(Fore.WHITE, bedes)
    print('')
    print(Fore.LIGHTMAGENTA_EX, chna)
    print(Fore.WHITE, chdes)
    print('')
    print(Fore.LIGHTMAGENTA_EX, alna)
    print(Fore.WHITE, aldes)

def letters():#displays all the letters the killer has written to the detective
    print(Fore.RED, intro['breakspace'], Fore.YELLOW)
    animate('              Your mail')
    print(Fore.RED, intro['breakspace'])
    for key, value in mail.items():
        print(Fore.WHITE, value)
    
#PRECINCT
def office1(health):#The precinct text without puzzle option
    inventory['items'].append({'case files'})
    print(Fore.RED, intro['breakspace'], Fore.YELLOW)
    animate(offname)
    print(Fore.RED, intro['breakspace'])
    print()
    print(Fore.WHITE, offdes)
    print()
    print(Fore.LIGHTMAGENTA_EX, "<<Your case>>")
    print(Fore.WHITE, offfirst)
    print()
    print(Fore.LIGHTMAGENTA_EX, offex)
    print(Fore.WHITE, offex1)
    print('')
    room(health)

def officev2(health):#precinct text with puzzle option
    inventory['items'].append({'case files'})
    print(Fore.RED, intro['breakspace'], Fore.YELLOW)
    animate(offname)
    print(Fore.RED, intro['breakspace'])
    print(Fore.WHITE, offdes)
    print(Fore.LIGHTMAGENTA_EX, "<<Your case>>")
    print(Fore.WHITE, offfirst)
    print()
    print(Fore.LIGHTMAGENTA_EX, offex)
    print(Fore.WHITE, offex1)
    room(health)
    print('')
    print(Fore.LIGHTMAGENTA_EX, puzzle['message'])
    print(Fore.CYAN, puzzle['command'])
    print(Fore.RED, puzzle['warning'], Fore.WHITE)

def puzzlerun1(health):#displays the precinct puzzle and makes it work for all options
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
        endscene()
        officev2(health)
        offifelse1(health)
        return health
    elif answer_1 == '2':
        clearscreen()
        print(Fore.LIGHTGREEN_EX, 'Correct! +5 health \n')
        print(Fore.WHITE, 'The killer is leading you to the church! We have to get there quickly to find the next clue.')
        health =health + 5
        print(f'Your health is now {health}')
        endscene()
        while True:
            office1(health)
            offifelse2(health)
            return health
    elif answer_1 == '3':
        clearscreen()
        print(Fore.RED, "You are wrong. The exhaustion of figuring this out has taken a toll on you -5 health \n") 
        print(Fore.WHITE, 'Now that you know what it is not, re-attempt the question and find the next clue.')
        health =health - 5
        print(f'Your health is now {health}')
        endscene()
        officev2(health)
        offifelse1(health)
        return health
    else:
        print("Try again")
        answer_1 = input("Please enter the number of you answer: ")

def offifelse1(health):#Options of where to go from the precinct if they havent already done the puzzle
    inter = input(str("What would you like to do? / Where would you like to go?"))
    if inter == "help me":
        clearscreen()
        helpme()
        endscene()

    elif inter == "commands":
        clearscreen()
        commandsss()

    elif inter == "map":
        clearscreen()
        mapp()
        endscene()

    elif inter == "mail":
        clearscreen()
        letters()
        endscene()

    elif inter == "puzzle":
        clearscreen()
        puzzlerun1(health)

    elif inter == "the beach":
        clearscreen()
    
    elif inter == "the church":
        clearscreen()
        room(health)
        churchv1(health)
        chifelse1()

    elif inter == "the back alley":
        clearscreen()
        fight1(health, attack_health)
        alleyv1(health)
        allifelse1(health)

    elif inter == "quit":
        quit = input(str("Are you sure you want to quit? Enter yes/no: "))
        if quit == 'no':
            clearscreen()
        elif quit == 'yes':
            clearscreen()
            print(Fore.RED, "The quitters ending")
            print(Fore.WHITE, "You gave up. I'm disappointed.")
            exit()

    else:
        print(Fore.WHITE, "Try again")
        offifelse1()


def offifelse2(health):#options of where to go if they have already done the puzzle
    inter = input(str("What would you like to do? / Where would you like to go?"))
    if inter == "help me":
        clearscreen()
        helpme()
        endscene()

    elif inter == "commands":
        clearscreen()
        commandsss()

    elif inter == "map":
        clearscreen()
        mapp()

    elif inter == "mail":
        clearscreen()
        letters()
        endscene()

    elif inter == "puzzle":
        print('You have already successfully completed the puzzle from this room, congrats! \n If you want to review the mail from the puzzle, please enter "mail"')

    elif inter == "the beach":
        clearscreen()
    
    elif inter == "the church":
        clearscreen()
        room(health)
        churchv1(health)
        chifelse1()

    elif inter == "the back alley":
        clearscreen()
        fight1(health, attack_health)
        alleyv1(health)
        allifelse1(health)

    elif inter == "quit":
        quit = input(str("Are you sure you want to quit? Enter yes/no: "))
        if quit == 'no':
            clearscreen()
        elif quit == 'yes':
            clearscreen()
            print(Fore.RED, "The quitters ending")
            print(Fore.WHITE, "You gave up. I'm disappointed.")
            exit()

    else:
        print(Fore.WHITE, "Try again")
        offifelse2()

#CHURCH
def churchv1(health):#church text with puzzle option
    inventory['items'].append({'engraved knife'})
    print(Fore.RED, intro['breakspace'], Fore.YELLOW)
    animate(chna)
    print(Fore.RED, intro['breakspace'])
    print()
    print(Fore.WHITE, chdes)
    print()
    room(health)
    ()
    print(Fore.LIGHTMAGENTA_EX, chex)
    print(Fore.WHITE, chex1)
    print()
    print(Fore.LIGHTMAGENTA_EX, puzzle['message'])
    print(Fore.CYAN, puzzle['command'])
    print(Fore.RED, puzzle['warning'], Fore.WHITE)

def churchv2(health):#church text without puzzle option
    print(Fore.RED, intro['breakspace'], Fore.YELLOW)
    animate(chna)
    print(Fore.RED, intro['breakspace'])
    print()
    print(Fore.WHITE, chdes)
    print()
    room(health)
    print()
    print(Fore.LIGHTMAGENTA_EX, chex)
    print(Fore.WHITE, chex1)

def puzzlerun2(health):#makes church puzzle run for all options
    print(Fore.RED, intro['breakspace'], Fore.YELLOW)
    animate('              Puzzle Room')
    print(Fore.RED, intro['breakspace'])
    print()
    print(puzzle2['opening'])
    print('')
    print(Fore.WHITE, mail['second'])
    print()
    print(puzzle2['where'])
    print(puzzle2['items'])
    answer2 = input("Please enter the number of your answer:")
    if answer2 == '1':
        clearscreen()
        print(Fore.LIGHTGREEN_EX, 'Correct! +5 health \n')
        print(Fore.WHITE, "The last victims jacket has the answers to who BOBBI is. Let's go to the alley.")
        health =health + 5
        print(f'Your health is now {health}')
        endscene()
        while True:
            clearscreen
            churchv2(health)
            chifelse2(health)
            return health
    elif answer2 =='2':
        clearscreen()
        print(Fore.RED, "You are wrong. The exhaustion of figuring this out has taken a toll on you -5 health \n") 
        print(Fore.WHITE, 'Now that you know what it is not, re-attempt the question and find the next clue.')
        health = health - 5
        print(f'Your health is now {health}')
        endscene()
        churchv1(health)
        chifelse1(health)
        return health
    elif answer2 == '3':
        clearscreen()
        print(Fore.RED, "You are wrong. The exhaustion of figuring this out has taken a toll on you -5 health \n") 
        print(Fore.WHITE, 'Now that you know what it is not, re-attempt the question and find the next clue.')
        health = health - 5
        print(f'Your health is now {health}')
        endscene()
        churchv1(health)
        chifelse1(health)
        return health
    else:
        print("Try again")
        answer_1 = input("Please enter the number of you answer: ")


def chifelse2(health): #if else statement for if the puzzle is correct and already been completed
    inter = input(str("What would you like to do? / Where would you like to go?"))
    if inter == 'help me':
        clearscreen()
        helpme()
        endscene()
    elif inter == 'commands':
        clearscreen()
        commandsss()
        endscene()
    elif inter == 'map':
        clearscreen()
        mapp()
        endscene()
    elif inter == 'mail':
        clearscreen()
        letters()
        endscene()
    elif inter == 'puzzle':
        print('You have already successfully completed the puzzle from this room, congrats! \n If you want to review the mail from the puzzle, please enter "mail"')
        endscene()

    elif inter == 'the precinct':
        clearscreen()
        office1(health)
        offifelse2(health)
        endscene()
    elif inter == "the beach":
        clearscreen()

    elif inter == "the back alley":
        clearscreen()
        fight1(health, attack_health)
        alleyv1(health)
        allifelse1(health)

    elif inter == "quit":
        quit = input(str("Are you sure you want to quit? Enter yes/no: "))
        if quit == 'no':
            clearscreen()
        elif quit == 'yes':
            clearscreen()
            print(Fore.RED, "The quitters ending")
            print(Fore.WHITE, "You gave up. I'm disappointed.")
            exit()

    else:
        print("Try again")
        chifelse2()

def chifelse1(health): #if else statement for if the puzzle has not been completed and needs to be redone
    inter = input(str("What would you like to do? / Where would you like to go?"))
    if inter == "help me":
        clearscreen()
        helpme()
        endscene()

    elif inter == "commands":
        clearscreen()
        commandsss()

    elif inter == "map":
        clearscreen()
        mapp()
        endscene()

    elif inter == "mail":
        clearscreen()
        letters()
        endscene()
    
    elif inter == 'puzzle':
        clearscreen()
        mail.update({'second': "Hello again Detective, \nI hope you have found the gift I have left for you. Do take good care of it, I'll be sending some people to collect it when i'm ready to put it to good use. Don't you just love my addition to the handle, I hope BOBBI is not a bore, I just hate a bad time. But I love a good chase, to get to BOBBI before me, the alley holds the answers. Find the item with pockets big enought to hold a knife but too small to hold a textbook."})
        puzzlerun2(health)
        endscene()

    elif inter == 'the precinct':
        clearscreen()
        office1(health)
        offifelse2(health)
        endscene()
    elif inter == 'the beach':
        clearscreen()

    elif inter == 'the back alley':
        clearscreen()
        fight1(health, attack_health)
        alleyv1(health)
        allifelse1(health)

    elif inter == "quit":
        quit = input(str("Are you sure you want to quit? Enter yes/no: "))
        if quit == 'no':
            clearscreen()
        elif quit == 'yes':
            clearscreen()
            print(Fore.RED, "The quitters ending")
            print(Fore.WHITE, "You gave up. I'm disappointed.")
            exit()

    else:
        print("Try again")
        chifelse1()

#BACK ALLEY
def alleyv1(health):#back alley text with puzzle option
    inventory['items'].append['Poster for workout group called BOBBI', 'Map of the beach with an x over part of it']
    mail.update({'third':"Hello Again Detective, \nI hope this letter and its friends find you well. I have left you a clue as to the wearabouts of my next beautiful, brown eyed victim succumbed to fate. Oh I do hope you will make it in time to see her blonde hair coated in blood. As always I love a challenge, I do hope these clues are enough for you to get your thick head around what is happening. \nI'll be seeing you again real soon."})
    print(Fore.RED, intro['breakspace'], Fore.YELLOW)
    animate(alna)
    print(Fore.RED, intro['breakspace'])
    print()
    print(Fore.WHITE, aldes)
    print()
    room(health)
    ()
    print(Fore.LIGHTMAGENTA_EX, alex)
    print(Fore.WHITE, alex1)
    print()
    print(Fore.LIGHTMAGENTA_EX, puzzle['message'])
    print(Fore.CYAN, puzzle['command'])
    print(Fore.RED, puzzle['warning'], Fore.WHITE)

def alleyv2(health):#back alley text without puzzle option
    inventory['items'].append['Poster for workout group called BOBBI', 'Map of the beach with an x over part of it']
    print(Fore.RED, intro['breakspace'], Fore.YELLOW)
    animate(alna)
    print(Fore.RED, intro['breakspace'])
    print()
    print(Fore.WHITE, aldes)
    print()
    room(health)
    print()
    print(Fore.LIGHTMAGENTA_EX, alex)
    print(Fore.WHITE, alex1)

def puzzlerun3(health):#makes church puzzle run for all options
    print(Fore.RED, intro['breakspace'], Fore.YELLOW)
    animate('              Puzzle Room')
    print(Fore.RED, intro['breakspace'])
    print()
    print(puzzle3['opening'])
    print('')
    print(Fore.WHITE, mail['third'])
    print()
    print(puzzle3['where'])
    print(puzzle3['options'])
    answer3 = input("Please enter the number of your answer:")
    if answer3 == '1':
        clearscreen()
        print(Fore.LIGHTGREEN_EX, "You are wrong. The exhaustion of figuring this out has taken a toll on you -5 health \n")
        print(Fore.WHITE, 'Now that you know what it is not, re-attempt the question and find the next clue.')
        health =health - 5
        print(f'Your health is now {health}')
        endscene()
        alleyv1(health)
        allifelse1(health)
    elif answer3 =='2':
        clearscreen()
        print(Fore.RED, "You are wrong. The exhaustion of figuring this out has taken a toll on you -5 health \n") 
        print(Fore.WHITE, 'Now that you know what it is not, re-attempt the question and find the next clue.')
        health = health - 5
        print(f'Your health is now {health}')
        endscene()
        alleyv1(health)
        allifelse1(health)
        return health
    elif answer3 == '3':
        clearscreen()
        print(Fore.RED, "You are wrong. The exhaustion of figuring this out has taken a toll on you -5 health \n") 
        print(Fore.WHITE, 'Now that you know what it is not, re-attempt the question and find the next clue.')
        health = health - 5
        print(f'Your health is now {health}')
        endscene()
        alleyv1(health)
        allifelse1(health)
        return health
    elif answer3 == '4':
        clearscreen()
        print(Fore.GREEN, "Correct! +5 health")
        print(Fore.WHITE, "You know who you are looking for! Now go find her before it is too late!")
        health = health +5
        print(f'Your health is now {health}')
        endscene()
        while True:
            clearscreen()
            alleyv2(health)
            allifelse2(health)
            return health
    else:
        print("Try again")
        answer_1 = input("Please enter the number of you answer: ")

def allifelse1(health): #if else statement for if the puzzle has not been completed and needs to be redone
    inter = input(str("What would you like to do? / Where would you like to go?"))
    if inter == "help me":
        clearscreen()
        helpme()
        endscene()

    elif inter == "commands":
        clearscreen()
        commandsss()
        endscene()

    elif inter == "map":
        clearscreen()
        mapp()
        endscene()

    elif inter == "mail":
        clearscreen()
        letters()
        endscene()
    
    elif inter == 'puzzle':
        clearscreen()
        puzzlerun3(health)
        endscene()

    elif inter == 'the precinct':
        clearscreen()
        office1(health)
        offifelse2(health)

    elif inter == 'the beach':
        clearscreen()

    elif inter == 'the church':
        clearscreen()
        room(health)
        churchv1(health)
        chifelse1()

    elif inter == "quit":
        quit = input(str("Are you sure you want to quit? Enter yes/no: "))
        if quit == 'no':
            clearscreen()
        elif quit == 'yes':
            clearscreen()
            print(Fore.RED, "The quitters ending")
            print(Fore.WHITE, "You gave up. I'm disappointed.")
            exit()

    else:
        print("Try again")
        allifelse1(health)


def allifelse2(health): #if else statement for if the puzzle is correct and already been completed
    inter = input(str("What would you like to do? / Where would you like to go?"))
    if inter == 'help me':
        clearscreen()
        helpme()
        endscene()
    elif inter == 'commands':
        clearscreen()
        commandsss()
        endscene()
    elif inter == 'map':
        clearscreen()
        mapp()
        endscene()
    elif inter == 'mail':
        clearscreen()
        letters()
        endscene()
    elif inter == 'puzzle':
        print('You have already successfully completed the puzzle from this room, congrats! \n If you want to review the mail from the puzzle, please enter "mail"')

    elif inter == 'the precinct':
        clearscreen()
        office1(health)
        offifelse2(health)
    elif inter == "the beach":
        clearscreen()

    elif inter == "the church":
        clearscreen()
        room(health)
        churchv1(health)
        chifelse1()

    elif inter == "quit":
        quit = input(str("Are you sure you want to quit? Enter yes/no: "))
        if quit == 'no':
            clearscreen()
        elif quit == 'yes':
            clearscreen()
            print(Fore.RED, "The quitters ending")
            print(Fore.WHITE, "You gave up. I'm disappointed.")
            exit()

    else:
        print("Try again")
        allifelse2(health)


def fight1(health, attack_health): #the fight before the back alley, has a chance to die
    clearscreen()
    damage = ''
    attdam = 7 #attackers damage
    print(Fore.RED, intro['breakspace'])
    print(Fore.YELLOW, "              Fight")
    print(Fore.RED, intro['breakspace'])
    print()
    print(Fore.WHITE, fight['description'])
    health = health - 4 #for the first hit to the head
    print()
    print(fight['options'])
    ask = input("What will you do?")
    if ask == '2':
        print("You got away!")
    elif ask == '1':
        clearscreen()
        print(Fore.RED, 'You have chosen to fight!')
        print()
        print(Fore.WHITE, 'You realise you have a weapon in your back pocket, reaching for it could risk another hit.')
        choice = input('What would you like to do?\n    1. reach for the weapon\n    2. fight with your fists \n Enter number 1 or 2: ')
        if choice == '1':
            damage = 10
        elif choice == '2':
            damage = 2
        else:
            print("This is serious! Enter a valid item.")
        print(Fore.GREEN, '')
        print(f'Your current health is {health}')
        print(Fore.RED, '')
        print(f'Your attackers health is {attack_health}')
        print(Fore.WHITE)
        while attack_health > 0 and health > 0:
            print(f'You struck the attacker', Fore.RED)
            attack_health = attack_health - damage
            print(f'Your attackers health is now {attack_health}', Fore.GREEN)
            print(f'Your health is now {health}')
            if attack_health < 0:
                attack_health = 0
            
            print(Fore.WHITE, '')
            print('Your assailant hit you!', Fore.GREEN)
            health = health - attdam
            print(f'Your health is now {health}', Fore.RED)
            print(f'Your attackers health is now {attack_health}')

            print(Fore.CYAN, fight['options'])
            ask = input("What will you do?")
            print(Fore.WHITE, '')
            if ask == '2':
                clearscreen()
                print("You got away!")
                endscene()
            elif ask == '1':
                print(Fore.WHITE, 'You struck the attacker', Fore.RED)
                print(f'Your attackers health is now {attack_health}', Fore.GREEN)
                print(f'Your health is now {health}')
                attack_health = attack_health - damage
                if attack_health < 0:
                    attack_health = 0
                
                print(Fore.WHITE, 'Your assailant hit you!', Fore.GREEN)
                health = health - attdam
                if health < 0:
                    health = 0
                print(f'Your health is now {health}', Fore.RED)
                print(f'Your attackers health is now {attack_health}')

                if health <= 0:
                    clearscreen()
                    print(Fore.RED, intro['breakspace'])
                    print(Fore.YELLOW, 'GAME OVER')
                    print(Fore.RED, intro['breakspace'])
                    print(Fore.WHITE, 'The last battle ending')
                    print()
                    print('Your attacker successfully killed you and the murderer got away')
                    exit()
                elif attack_health <= 0:
                    clearscreen()
                    print(Fore.GREEN, 'You have won the battle!')
                    print()
                    print(Fore.WHITE, 'Continue on to stop the killer!')
                    endscene()
                    break
            else:
                print('Try again')
                ask = input("What will you do?")


#Beach
def beachv1(health):
    print(Fore.RED, intro['breakspace'], Fore.YELLOW)
    animate(bena)
    print(Fore.RED, intro['breakspace'])
    print()
    print(Fore.WHITE, bedes)
    print()
    room(health)
    ()
    print(Fore.LIGHTMAGENTA_EX, beex)
    print(Fore.WHITE, beex1)
    print()
    print(Fore.LIGHTMAGENTA_EX, puzzle['message'])
    print(Fore.CYAN, puzzle['command'])
    print(Fore.LIGHTRED_EX, puzzle['warning'], Fore.WHITE)
    print()
    print(Fore.RED, 'You see killer. Type "killer" to follow him')
    print()
    print(Fore.GREEN, 'You also see the next victim. Type "vicitm" to warn her.', Fore.WHITE)

def beachv2(health):
    print(Fore.RED, intro['breakspace'], Fore.YELLOW)
    animate(bena)
    print(Fore.RED, intro['breakspace'])
    print()
    print(Fore.WHITE, bedes)
    print()
    room(health)
    print()
    print(Fore.LIGHTMAGENTA_EX, beex)
    print(Fore.WHITE, beex1)
    print()
    print(Fore.RED, 'You see killer. Type "killer" to follow him')
    print()
    print(Fore.GREEN, 'You also see the next victim. Type "vicitm" to warn her.', Fore.WHITE)

def puzzlerun4(health):
    print(Fore.RED, intro['breakspace'], Fore.YELLOW)
    animate('              Puzzle Room')
    print(Fore.RED, intro['breakspace'])
    print()
    print(Fore.WHITE, puzzle4['opening'])
    print()
    print(Fore.CYAN, puzzle4['what'])
    print(puzzle4['options'])
    answer4 = input("Please enter the number of your answer:")
    if answer4 == '1':
        clearscreen()
        print(Fore.LIGHTGREEN_EX, "You are wrong. The exhaustion of figuring this out has taken a toll on you -5 health \n")
        print(Fore.WHITE, 'Now that you know what it is not, re-attempt the question and find the next clue.')
        health =health - 5
        print(f'Your health is now {health}')
        endscene()
        beachv1(health)
        beaifelse1(health)
    elif answer4 =='2':
        clearscreen()
        print(Fore.RED, "You are wrong. The exhaustion of figuring this out has taken a toll on you -5 health \n") 
        print(Fore.WHITE, 'Now that you know what it is not, re-attempt the question and find the next clue.')
        health = health - 5
        print(f'Your health is now {health}')
        endscene()
        beachv1(health)
        beaifelse1(health)
        return health
    elif answer4 == '3':
        clearscreen()
        print(Fore.RED, "You are wrong. The exhaustion of figuring this out has taken a toll on you -5 health \n") 
        print(Fore.WHITE, 'Now that you know what it is not, re-attempt the question and find the next clue.')
        health = health - 5
        print(f'Your health is now {health}')
        endscene()
        beachv1(health)
        beaifelse1(health)
        return health
    elif answer4 == '4':
        clearscreen()
        print(Fore.RED, "You are wrong. The exhaustion of figuring this out has taken a toll on you -5 health \n") 
        print(Fore.WHITE, 'Now that you know what it is not, re-attempt the question and find the next clue.')
        health = health - 5
        print(f'Your health is now {health}')
        endscene()
        beachv1(health)
        beaifelse1(health)
        return health
    elif answer4 == '5':
        clearscreen()
        print(Fore.GREEN, "Correct! +5 health")
        print(Fore.WHITE, puzzle4['after'])
        health = health +5
        print(f'Your health is now {health}')
        endscene()
        while True:
            clearscreen()
            beachv2(health)
            beaifelse2(health)
            return health
    else:
        print("Try again")
        answer_1 = input("Please enter the number of you answer: ")

def beaifelse1(health):
    inter = input(str("What would you like to do? / Where would you like to go?"))
    if inter == "help me":
        clearscreen()
        helpme()
        endscene()

    elif inter == "commands":
        clearscreen()
        commandsss()
        endscene()

    elif inter == "map":
        clearscreen()
        mapp()
        endscene()

    elif inter == "mail":
        clearscreen()
        letters()
        endscene()
    
    elif inter == 'puzzle':
        clearscreen()
        puzzlerun4(health)
        endscene()

    elif inter == 'the precinct':
        clearscreen()
        office1(health)
        offifelse2(health)

    elif inter == 'the back alley':
        clearscreen()
        fight1(health, attack_health)
        alleyv1(health)
        allifelse1(health)

    elif inter == 'the church':
        clearscreen()
        room(health)
        churchv1(health)
        chifelse1()

    elif inter == "quit":
        quit = input(str("Are you sure you want to quit? Enter yes/no: "))
        if quit == 'no':
            clearscreen()
        elif quit == 'yes':
            clearscreen()
            print(Fore.RED, "The quitters ending")
            print(Fore.WHITE, "You gave up. I'm disappointed.")
            exit()
    
    elif inter == 'victim':
        clearscreen()
        print(Fore.RED, intro['breakspace'])
        print(Fore.BLUE, '              Saviours Ending')
        print(Fore.RED, intro['breakspace'])
        print()
        print(Fore.WHITE, 'You successfully warned the next victim of the threat to their life and got them to safety.')
        exit()

    elif inter == "killer":
        clearscreen()
        print(Fore.RED, intro['breakspace'])
        print(Fore.YELLOW, 'Killer Chase')
        print(Fore.RED, intro['breakspace'])
        print()
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
                what = input('What will you do? Enter your answer number: ')
        else:
            print("Try again")
            follow = input('The killer is leading you down the alley ways, will you call for backup or go it alone? \n    1. call for backup\n    2. go it alone \n Enter a number: ')



    else:
        print("Try again")
        beaifelse1(health)

def beaifelse2(health):
    inter = input(str("What would you like to do? / Where would you like to go?"))
    if inter == 'help me':
        clearscreen()
        helpme()
        endscene()
    elif inter == 'commands':
        clearscreen()
        commandsss()
        endscene()
    elif inter == 'map':
        clearscreen()
        mapp()
        endscene()
    elif inter == 'mail':
        clearscreen()
        letters()
        endscene()
    elif inter == 'puzzle':
        print('You have already successfully completed the puzzle from this room, congrats! \n If you want to review the mail from the puzzle, please enter "mail"')

    elif inter == 'the precinct':
        clearscreen()
        office1(health)
        offifelse2(health)

    elif inter == "the back alley":
        clearscreen()
        fight1(health, attack_health)
        alleyv1(health)
        allifelse1(health)

    elif inter == "the church":
        clearscreen()
        room(health)
        churchv1(health)
        chifelse1()

    elif inter == "quit":
        quit = input(str("Are you sure you want to quit? Enter yes/no: "))
        if quit == 'no':
            clearscreen()
        elif quit == 'yes':
            clearscreen()
            print(Fore.RED, "The quitters ending")
            print(Fore.WHITE, "You gave up. I'm disappointed.")
            exit()
    
    elif inter == 'victim':
        clearscreen()
        print(Fore.RED, intro['breakspace'])
        print(Fore.BLUE, '              Saviours Ending')
        print(Fore.RED, intro['breakspace'])
        print()
        print(Fore.WHITE, 'You successfully warned the next victim of the threat to their life and got them to safety.')
        exit()

    elif inter == "killer":
        clearscreen()
        print(Fore.RED, intro['breakspace'])
        print(Fore.YELLOW, 'Killer Chase')
        print(Fore.RED, intro['breakspace'])
        print()
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
                what = input('What will you do? Enter your answer number: ')
        else:
            print("Try again")

    else:
        print("Try again")
        beaifelse2(health)