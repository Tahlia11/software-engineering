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
    print(Fore.LIGHTMAGENTA_EX, offex)
    print(Fore.WHITE, offex1)
    print()
    print(Fore.LIGHTMAGENTA_EX, commands['head'])
    print(Fore.WHITE, commands['all'])


def helpme ():
    print(Fore.RED, intro['breakspace'])
    print(Fore.YELLOW, help['heading'])
    print(Fore.RED, intro['breakspace'])
    print(Fore.LIGHTMAGENTA_EX, help['ahead'])
    print(Fore.WHITE, help['aim'])
    print()
    print(Fore.LIGHTMAGENTA_EX, help['chead'])
    print(Fore.WHITE, help['commands'])
    print()
    print(Fore.LIGHTMAGENTA_EX, help['lhead'])
    print(Fore.WHITE, help['locations'])
    print()
    print(Fore.LIGHTMAGENTA_EX, help['thead'])
    print(Fore.WHITE, help['tips'])
    print()
    print(help['fail'])

def commandss():
    print(Fore.RED, intro['breakspace'])
    print(Fore.YELLOW, commandss['heading'])
    print(Fore.RED, intro['breakspace'])
    print(Fore.LIGHTMAGENTA_EX, commandss['thead'])
    print(Fore.WHITE, commandss['travel'])
    print()
    print(Fore.LIGHTMAGENTA_EX, commandss['ghead'])
    print(Fore.WHITE, commandss['game'])
    print()
    print(Fore.LIGHTMAGENTA_EX, commandss['phead'])
    print(Fore.WHITE, commandss['puzzle'])
    print()
    print(Fore.LIGHTMAGENTA_EX, commandss['bhead'])
    print(Fore.WHITE, commandss['battle'])

def mapp():
    print(Fore.RED, intro['breakspace'])
    print(Fore.YELLOW, map['heading'])
    print(Fore.RED, intro['breakspace'])
    print(Fore.LIGHTMAGENTA_EX, offname)
    print(Fore.WHITE, offdes)
    print()
    print(Fore.LIGHTMAGENTA_EX, bena)
    print(Fore.WHITE, bedes)
    print()
    print(Fore.LIGHTMAGENTA_EX, chna)
    print(Fore.WHITE, chdes)
    print()
    print(Fore.LIGHTMAGENTA_EX, alna)
    print(Fore.WHITE, aldes)

