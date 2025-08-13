office = {
    'name': '              The Precinct',
    'description': 'Buzzing with men in uniform, the precinct is the home of all detectives & police, their watching you.',
    'first':'Your boss has given you a new case. A young girl has been murdered in a back alley way coming out of a gym. The worst part, you recognise the way she has been killed. He is back. For your first clue complete the puzzle.',
    'exits': '<<Available exits>>',
    'exits1': ' > the church \n > the beach \n > the back alley'
}

print(Fore.RED, intro['breakspace'])
print(Fore.YELLOW, offname)
print(Fore.RED, intro['breakspace'])
print(Fore.WHITE, offdes)
print(Fore.LIGHTMAGENTA_EX, "<<Your new case>>")
print(Fore.WHITE, offfirst)
print(room())
print(Fore.CYAN, choice)
print(repr(choice))
if choice == "help me":
    clearscreen()
    print(helpme())
    print(endscene())
elif choice == "commands":
    clearscreen()
    print(commandss())
    print(endscene())
elif choice == "map":
    clearscreen()
    print(mapp())
    print(endscene())
elif choice == "mail":
    clearscreen()
else:
    print(Fore.WHITE, "Try again")
    print(Fore.CYAN, idduno())


print(helpme())
print(endscene())

