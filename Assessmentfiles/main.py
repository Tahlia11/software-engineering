from data import *
from functions import *
health = 100

while health > 0:
    clearscreen()
    #Welcome + game description
    print(Fore.RED, intro['breakspace'], Fore.YELLOW)
    animate(f"{intro['welcome']}")
    print(Fore.RED, intro['breakspace'])
    print(Fore.WHITE, intro['description'], Fore.CYAN)
    endscene() 

    #Game tips and starting controlls
    print(Fore.GREEN, start['success'])
    print(Fore.WHITE, start['basic'], Fore.CYAN)
    endscene()

    while True:
    #First room - Office
        officev2(health)
        while True:
            inter = input(str("What would you like to do? / Where would you like to go?"))
            if inter == "help me":
                clearscreen()
                helpme()
                endscene()
            


            elif inter == "commands":
                clearscreen()
                commandsss()
                endscene()


            elif inter == "map":
                clearscreen()
                mapp()
                endscene()


            elif inter == "mail":
                clearscreen()
                letters()
                endscene()


            elif inter == "puzzle":
                clearscreen()
                mail.update({'your first letter': "Hello Detective, \n Its been a long time. I'm sure you remember me, just as I remember you. I spent a long time locked up because of you, my reputation is ruined. Now I'm back, I'll go back to doing what I love. And you'll go back to chasing me. Find your first clue at the place where water meets te forehead, the sun shines in colour and you can finally find your people."})
                puzzlerun1(health)
                print(health)


            elif inter == "the church":
                clearscreen()
                churchv1(health)
                chifelse1(health)

            elif inter == "the back alley":
                clearscreen()
                fight1(health, attack_health)
                alleyv1(health)
                allifelse1(health)

            elif inter == "the beach":
                clearscreen()
                beachv1(health)
                beaifelse1(health)

            elif inter == "quit":
                quit = input(str("Are you sure you want to quit? Enter yes/no: "))
                if quit == 'no':
                    print(clearscreen())
                elif quit == 'yes':
                    clearscreen()
                    print(Fore.RED, "The quitters ending")
                    print(Fore.WHITE, "You gave up. I'm disappointed.")
                    exit()

            else:
                clearscreen()
                print(Fore.WHITE, "Try again")
            

clearscreen()
print(Fore.GREEN, 'Game over. You have no health left. Should have looked at that more closely')