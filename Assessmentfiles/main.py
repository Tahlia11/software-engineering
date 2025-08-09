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
print(Fore.CYAN, idduno())
if idduno() == "help me":
    clearscreen()
    print(helpme())
    print(endscene())
elif idduno() == "commands":
    clearscreen()
    print(commandss())
    print(endscene())
elif idduno() == "map":
    clearscreen()
    print(mapp())
    print(endscene())
elif idduno() == "mail":
    clearscreen()
else:
    print(Fore.WHITE, "Try again")
    print(Fore.CYAN, idduno())