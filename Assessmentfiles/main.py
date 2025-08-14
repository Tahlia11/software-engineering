from data import *
from functions import *

clearscreen()
#Welcome + game description
print(Fore.RED, intro['breakspace'], Fore.YELLOW)
animate(f"{intro['welcome']}")
print(Fore.RED, intro['breakspace'])
print(Fore.WHITE, intro['description'], Fore.CYAN)
print(endscene())

#Game tips and starting controlls
print(Fore.GREEN, start['success'])
print(Fore.WHITE, start['basic'], Fore.CYAN)
print(endscene())
while True:
#First room - Office
    office1()
    print('')
    print(Fore.LIGHTMAGENTA_EX, puzzle['message'])
    print(Fore.CYAN, puzzle['command'], Fore.WHITE)
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
        print(clearscreen())
        print(puzzle1())
    elif inter == "the beach":
        print(clearscreen())
    else:
        print(Fore.WHITE, "Try again")