from data import *
from functions import *
health = 100
if health > 100:
    health = 100

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
    officev2()
    inter = input(str("What would you like to do? / Where would you like to go?"))
    if inter == "help me":
        print(clearscreen())
        print(helpme())
        print(endscene())
    


    elif inter == "commands":
        print(clearscreen())
        print(commandsss())
        print(endscene())


    elif inter == "map":
        print(clearscreen())
        print(mapp())
        print(endscene())


    elif inter == "mail":
        print(clearscreen())
        print(letters())
        print(endscene())


    elif inter == "puzzle":
        print(clearscreen())
        mail.update({'your first letter': "Hello Detective, \n Its been a long time. I'm sure you remember me, just as I remember you. I spent a long time locked up because of you, my reputation is ruined. Now I'm back, I'll go back to doing what I love. And you'll go back to chasing me. Find your first clue at the place where water meets te forehead, the sun shines in colour and you can finally find your people."})
        print(puzzlerun1())


    elif inter == "the church":
        print(clearscreen())
        print(room())
        print(churchv1())
        inter = input(str("What would you like to do? / Where would you like to go?"))
        if inter == 'help me':
            print(clearscreen())
            print(helpme())
            print(endscene())
        elif inter == 'commands':
            print(clearscreen())
            print(commandsss())
            print(endscene())
        elif inter == 'map':
            print(clearscreen())
            print(mapp())
            print(endscene())
        elif inter == 'mail':
            print(clearscreen())
            print(letters())
            print(endscene())
        elif inter == 'puzzle':
            print(clearscreen())
            mail.update({'second': "Hello again Detective, \nI hope you have found the gift I have left for you. Do take good care of it, I'll be sending some people to collect it when i'm ready to put it to good use. Don't you just love my addition to the handle, I hope BOBBI is not a bore, I just hate a bad time. But I love a good chase, to get to BOBBI before me, the alley holds the answers. Find the item with pockets big enought to hold a knife but too small to hold a textbook."})
            print(puzzlerun2())
        elif inter == 'the precinct':
            print(clearscreen())
            print(office1())
            print(offifelse2())#?????????????????????????????????????????????????????????????????????????????????????????????
        elif inter == 'the beach':
            print(clearscreen())

        elif inter == 'the back alley':
            print(clearscreen())
        
        else: 
            print('Try again')

    elif inter == "the back alley":
        print(clearscreen())


    elif inter == "the beach":
        print(clearscreen())


    else:
        print(Fore.WHITE, "Try again")
