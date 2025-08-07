import colorama
colorama.init()
from colorama import Fore, init
import os
import time 

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