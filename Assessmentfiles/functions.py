import colorama
colorama.init()
from colorama import Fore, init
import os
import time 
from data import *



def idduno ():
    str(input("What would you like to do? / Where would you like to go?"))


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


#Every room
def room ():
    print(Fore.LIGHTMAGENTA_EX, inventory['message'])
    print(Fore.WHITE, inventory['items'])
    print('')
    print(f"Your current health is {health}")
    print('')
    print(Fore.LIGHTMAGENTA_EX, offex)
    print(Fore.WHITE, offex1)
    print('')
    print(Fore.LIGHTMAGENTA_EX, commands['head'])
    print(Fore.WHITE, commands['all'])
 
def office1():
    print(Fore.RED, intro['breakspace'])
    print(Fore.YELLOW, offname)
    print(Fore.RED, intro['breakspace'])
    print(Fore.WHITE, offdes)
    print(Fore.LIGHTMAGENTA_EX, "<<Your new case>>")
    print(Fore.WHITE, offfirst)
    print(room())

def helpme ():
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

def commandsss():
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

def mapp():
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

def letters():
    print(Fore.RED, intro['breakspace'], Fore.YELLOW)
    animate('              Your mail')
    print(Fore.RED, intro['breakspace'])
    for key, value in mail.items():
        print(Fore.WHITE, value)

def puzzle1():
    print(Fore.RED, intro['breakspace'], Fore.YELLOW)
    animate('              Puzzle Room')
    print(Fore.RED, intro['breakspace'])
    print('')
    print(Fore.WHITE, mail['your first letter'])
    print('')
    print(puzzle2['where'])
    print('')
    print(puzzle2['locations'])
    answer_1 = input("Please enter the number of you answer: ")
    if answer_1 == '1':
        clearscreen()
        print(Fore.RED, "You are wrong. The exhaustion of figuring this out has taken a toll on you -5 health \n") 
        print(Fore.WHITE, 'Now that you know what it is not, re-attempt the question and find the next clue.')
        health = health - 5
        print(endscene())
    elif answer_1 == '2':
        print(clearscreen())
        print(Fore.LIGHTGREEN_EX, 'Correct! +5 progress \n')
        print(Fore.WHITE, 'The killer is leading you to the church! We have to get there quickly to find the next clue.')
        health = health + 5
        print(endscene())
    elif answer_1 == '3':
        print(Fore.RED, "You are wrong. The exhaustion of figuring this out has taken a toll on you -5 health \n") 
        print(Fore.WHITE, 'Now that you know what it is not, re-attempt the question and find the next clue.')
        health = health - 5
        print(endscene())
    else:
        print("Try again")
        answer_1 = input("Please enter the number of you answer: ")