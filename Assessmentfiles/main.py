from data import *
from functions import *
print(Fore.RED, intro['breakspace'], Fore.YELLOW)
animate(f"{intro['welcome']}")
print(Fore.RED, intro['breakspace'])
print(Fore.WHITE, intro['description'], Fore.CYAN)
print(endscene())


print(Fore.GREEN, start['success'])
print(Fore.WHITE, start['basic'], Fore.CYAN)
print(endscene())

print(intro['breakspace'])
print(Fore.YELLOW, office['name'])
print(intro['breakspace'])
print(Fore.WHITE, office['description'])
print(Fore.LIGHTMAGENTA_EX, "Your new case:")
print(Fore.WHITE, office['first'])
print(Fore.LIGHTMAGENTA_EX, inventory)
print(f"Your current health is {health}")

