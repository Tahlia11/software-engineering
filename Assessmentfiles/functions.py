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
    print()


#Every room
def room ():
    print(Fore.LIGHTMAGENTA_EX, inventory['message'])
    print(Fore.WHITE, inventory['items'])
    print()
    print(f"Your current health is {health}")
    print()
    print(f"Your current progress is {progress}")
    print()
    print(Fore.LIGHTMAGENTA_EX, puzzle['message'])
    print(Fore.CYAN, puzzle['command'])
    print()
    print(Fore.LIGHTMAGENTA_EX, office['exits'])
    print(Fore.WHITE, office['exits1'])
    print()
    print(Fore.LIGHTMAGENTA_EX, commands['head'])
    print(Fore.WHITE, commands['all'])
    print(Fore.CYAN, idduno())

def helpme ():
    print(Fore.RED, intro['breakspace'])
    print(Fore.YELLOW, help['heading'])
    print(Fore.RED, intro['breakspace'])
    print(Fore.LIGHTMAGENTA_EX, help['ahead'])
    print(Fore.WHITE, help['aim'])
    print(Fore.LIGHTMAGENTA_EX, help['chead'])
    print(Fore.WHITE, help['commands'])
    print(Fore.LIGHTMAGENTA_EX, help['lhead'])
    print(Fore.WHITE, help['locations'])
    print(Fore.LIGHTMAGENTA_EX, help['thead'])
    print(Fore.WHITE, help['tips'])
    print(help['fail'])
    endscene()