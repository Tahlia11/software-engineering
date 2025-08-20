def fight1(health, attack_health):
    clearscreen()
    damage = ''
    attdam = 7 #attackers damage
    print(Fore.RED, intro['breakspace'])
    print(Fore.YELLOW, "              Fight")
    print(Fore.RED, intro['breakspace'])
    print()
    print(Fore.WHITE, fight['description'])
    health = health - 4 #for the first hit to the head
    print()
    print(fight['options'])
    ask = input("What will you do?")
    if ask == '2':
        print("You got away!")
    elif ask == '1':
        clearscreen()
        print(Fore.RED, 'You have chosen to fight!')
        print()
        print(Fore.GREEN, 'Here are you current inventory items!')
        print(Fore.WHITE, inventory['items'])
        w_choice = input(str('What item would you like to use to strike the attacker?'))
        while w_choice not in inventory['items']:
            w_choice = input(str('What item would you like to use to strike the attacker?'))
            if w_choice in inventory['items']:
                print('Its time to fight')
                if w_choice == 'case files':
                    damage = 2
                elif w_choice == 'engraved knife':
                    damage = 10
            else:
                print("This is serious! Enter a valid item.")
        print(Fore.GREEN, '')
        print(f'Your current health is {health}')
        print(f'Your attackers health is {attack_health}')
        while attack_health > 0 and health > 0:
            print(f'It is you struck the attacker with your {w_choice}')
            print(f'Your attackers health is now {attack_health}')
            print(f'Your health is now {health}')
            attack_health = attack_health - damage
            if attack_health < 0:
                attack_health = 0
            
            print('Your assailant hit you!')
            health = health - attdam
            print(f'Your health is now {health}')

            print(Fore.CYAN, fight['options'])
            ask = input("What will you do?")
            if ask == '2':
                print("You got away!")
            elif ask == '1':
                print(f'It is you struck the attacker with your {w_choice}')
                print(f'Your attackers health is now {attack_health}')
                print(f'Your health is now {health}')
                attack_health = attack_health - damage
                if attack_health < 0:
                    attack_health = 0
                
                print('Your assailant hit you!')
                health = health - attdam
                if health < 0:
                    health = 0
                print(f'Your health is now {health}')

                if health <= 0:
                    clearscreen
                    print(Fore.RED, intro['breakspace'])
                    print(Fore.RED, 'GAME OVER')
                    print(Fore.RED, intro['breakspace'])
                    print(Fore.WHITE, 'The last battle ending')
                    print()
                    print('Your attack successfully killed you and the murderer got away')
                    break
                elif attack_health <= 0:
                    print(Fore.GREEN, 'You have won the battle!')
                    print()
                    print(Fore.WHITE, 'Continue on to stop the killer!')
                    break