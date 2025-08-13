from data import *
from functions import *
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

#First room - Office
print(Fore.RED, intro['breakspace'])
print(Fore.YELLOW, offname)
print(Fore.RED, intro['breakspace'])
print(Fore.WHITE, offdes)
print(Fore.LIGHTMAGENTA_EX, "<<Your new case>>")
print(Fore.WHITE, offfirst)
print(room())
inter = input(str("What would you like to do? / Where would you like to go?"))

while inter == "help me":
    print(clearscreen ())
    print(helpme())
    print(endscene())
    break
while inter == "commands":
    print(clearscreen ())
    print(commandsss())
    print(endscene())
    break
while inter == "map":
    print(clearscreen ())
    print(mapp())
    print(endscene())
    break
while inter == "mail":
    print(clearscreen())
    print(letters())
    print(endscene())
while inter == "puzzle":
    print(clearscreen())
    print(puzzle1())
    print(endscene())
else:
    print(Fore.WHITE, "Try again")