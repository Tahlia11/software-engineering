
print('Hello world')
import os
def clearScreen():
    os.system('cls')

clearScreen()

import time
def animateText(text):
    for letter in text:
        print(letter, end='')
        time.sleep(0.1)
        print()
animateText('Hello world')

from colorama import *
def colourText(text, colour):
    print(colour + text)

colourText("this is red", Fore.RED)
colourText('THis is green', Back.GREEN)