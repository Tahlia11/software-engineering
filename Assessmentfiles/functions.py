import colorama
colorama.init()
from colorama import Fore, init
import os
import time 
from data import *

health = 100
if health > 100:
    health = 100


def clearscreen ():
    os.system('cls')

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
    print(Fore.RED, intro['breakspace'])
    print(Fore.YELLOW, offname)
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
    print(Fore.RED, intro['breakspace'])
    print(Fore.YELLOW, offname)
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
    print(Fore.CYAN, puzzle['command'], Fore.WHITE)


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
        print(endscene())
        print(officev2(health))
        offifelse1(health)
        return health
    elif answer_1 == '2':
        print(clearscreen())
        print(Fore.LIGHTGREEN_EX, 'Correct! +5 health \n')
        print(Fore.WHITE, 'The killer is leading you to the church! We have to get there quickly to find the next clue.')
        health =health + 5
        print(f'Your health is now {health}')
        print(endscene())
        while True:
            office1(health)
            offifelse2(health)
            return health
    elif answer_1 == '3':
        print(clearscreen())
        print(Fore.RED, "You are wrong. The exhaustion of figuring this out has taken a toll on you -5 health \n") 
        print(Fore.WHITE, 'Now that you know what it is not, re-attempt the question and find the next clue.')
        health =health - 5
        print(f'Your health is now {health}')
        print(endscene())
        officev2(health)
        offifelse1(health)
        return health
    else:
        print("Try again")
        answer_1 = input("Please enter the number of you answer: ")



def offifelse1(health):#Options of where to go from the precinct if they havent already done the puzzle
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
        puzzlerun1(health)

    elif inter == "the beach":
        print(clearscreen())
    
    elif inter == "the church":
        print(clearscreen())
        room(health)
        churchv1(health)
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
            puzzlerun2(health)
        elif inter == 'the precinct':
            print(clearscreen())
            office1(health)
            offifelse2()#?????????????????????????????????????????????????????????????????????????????????????????????
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


def offifelse2(health):#options of where to go if they have already done the puzzle
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
        print(room(health))
        print(churchv1(health))
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
            print(puzzlerun2(health))
        elif inter == 'the precinct':
            print(clearscreen())
            office1(health)
            offifelse2(health)#?????????????????????????????????????????????????????????????????????????????????????????????
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


#CHURCH
def churchv1(health):#precinct text with puzzle option
    inventory.update({'first':'engraved knife (has BOBBI written on it)'})
    print(Fore.RED, intro['breakspace'])
    print(Fore.YELLOW, chna)
    print(Fore.RED, intro['breakspace'])
    print()
    print(Fore.WHITE, chdes)
    print()
    print(room(health))
    ()
    print(Fore.LIGHTMAGENTA_EX, chex)
    print(Fore.WHITE, chex1)
    print()
    print(Fore.LIGHTMAGENTA_EX, puzzle['message'])
    print(Fore.CYAN, puzzle['command'])
    print(Fore.RED, puzzle['warning'], Fore.WHITE)


def churchv2(health):#precinct text without puzzle option
    print(Fore.RED, intro['breakspace'])
    print(Fore.YELLOW, chna)
    print(Fore.RED, intro['breakspace'])
    print()
    print(Fore.WHITE, chdes)
    print()
    print(room(health))
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
            print(churchv2(health))
            print(chifelse2(health))
            return health
    elif answer2 =='2':
        print(clearscreen())
        print(Fore.RED, "You are wrong. The exhaustion of figuring this out has taken a toll on you -5 health \n") 
        print(Fore.WHITE, 'Now that you know what it is not, re-attempt the question and find the next clue.')
        health = health - 5
        print(f'Your health is now {health}')
        print(endscene())
        print(churchv1(health))
        print(chifelse1(health))
        return health
    elif answer2 == '3':
        print(clearscreen())
        print(Fore.RED, "You are wrong. The exhaustion of figuring this out has taken a toll on you -5 health \n") 
        print(Fore.WHITE, 'Now that you know what it is not, re-attempt the question and find the next clue.')
        health = health - 5
        print(f'Your health is now {health}')
        print(endscene())
        print(churchv1(health))
        print(chifelse1(health))
        return health
    else:
        print("Try again")
        answer_1 = input("Please enter the number of you answer: ")



def chifelse2(health): #if else statement for if the puzzle is correct and already been completed
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
        print('You have already successfully completed the puzzle from this room, congrats! \n If you want to review the mail from the puzzle, please enter "mail"')
    elif inter == 'the precinct':
        print(clearscreen())
        print(office1(health))
        print(offifelse2(health))#???????????????????????????????????????????????????????????????????????????????????????????????
    elif inter == "the beach":
        print(clearscreen())
    
    elif inter == "the back alley":
        print(clearscreen())

def chifelse1(health): #if else statement for if the puzzle has not been completed and needs to be redone
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
    
    elif inter == 'puzzle':
        print(puzzlerun2(health))

    elif inter == 'the precinct':
        print(clearscreen())
        office1(health)
        print(offifelse2(health))#???????????????????????????????????????????????????????????????????????????????????????????????
    elif inter == 'the beach':
        print(clearscreen())

    elif inter == 'the back alley':
        print(clearscreen())

    else:
        print("Try again")
        answer_1 = input("Please enter the number of you answer: ")