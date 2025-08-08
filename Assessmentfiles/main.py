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
print(Fore.YELLOW, office['name'])
print(Fore.RED, intro['breakspace'])
print(Fore.WHITE, office['description'])
print(Fore.LIGHTMAGENTA_EX, "<<Your new case>>")
print(Fore.WHITE, office['first'])
print(room())

if idduno() == "help me":
    clearscreen()
    print(helpme())