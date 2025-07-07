weapons = ["sword", "axe", "bow and arrow"]
special_attacks = ["fireball", "snow strike", "tsunami"]
enemies = ["Bruce the burger", "Larry the meathead", "Tahlia the overtired teenager"]
player_health = 100
enemy_health = 100
damage = 15


print(f"Welcome to the inventory. You have these weapons available - {weapons}. You have these stikes available - {special_attacks}\n")

w_choice = ''
while w_choice not in weapons:
    w_choice = input("What weapon would you like to use?")
    if w_choice in weapons:
        print("Nice choice.")
    else:
        print("Try again.")

a_choice = ''
while a_choice not in special_attacks:
    a_choice = input("What attack would you like to use?")
    if a_choice in special_attacks:
        print("Thats a strong attack.")
    else:
        print("Try again.")

if w_choice in weapons and a_choice in special_attacks:
    print(f"Use your {w_choice} and strike with {a_choice} to defeat the enemy.")

qw_add = ''
while qw_add != "yes" and qw_add != "no":
    qw_add = input("Are there weapons you would like to add to your inventory? (yes/no)").lower()
    if qw_add == "yes":
        w_add = input(str("What weapon would you like to add? Enter only one: "))
        weapons.append(w_add)
        print(weapons)
    elif qw_add != "no" and qw_add != "yes":
        print("Please re-enter yes or no")

qw_remove = ''
while qw_remove!= "yes" and qw_remove != "no":
    qw_remove = input("Are there weapons you would like to remove to your inventory? (yes/no)").lower()
    if qw_remove == "yes":
        w_remove = ''
        while w_remove not in weapons: 
            w_remove = input(str("What weapon would you like to remove?"))
            if w_remove in weapons:
                weapons.remove(w_remove)
                print(weapons)
                break
            else:
                print("Enter a valid weapon to remove:")
    elif qw_remove != "no" and qw_remove != "yes":
        print("Please re-enter yes or no")

qa_add = ''
while qa_add != "yes" and qa_add != "no":
    qa_add = input("Are there attacks you would like to add to your inventory? (yes/no)").lower()
    if qa_add == "yes":
        a_add = input(str("What attacks would you like to add? Enter only one: "))
        special_attacks.append(a_add)
        print(special_attacks)
    elif qa_add != "no" and qa_add != "yes":
        print("Please re-enter yes or no")

qa_remove = ''
while qa_remove != "yes" and qa_remove != "no":
    qa_remove = input("Are there attacks you would like to remove to your inventory? (yes/no)").lower()
    if qa_remove == "yes":
        a_remove = ''
        while a_remove not in special_attacks: 
            a_remove = input(str("What attack would you like to remove?"))
            if a_remove in special_attacks:
                special_attacks.remove(a_remove)
                print(special_attacks)
                break
            else:
                print("Enter a valid attack to remove:")
    elif qa_remove != "no" and qa_remove != "yes":
        print("Please re-enter yes or no")

print(f"You have {weapons.__len__()} weapons in your inventory")
print(f"You have {special_attacks.__len__()} attacks in your inventory")
print(f"These are you enemy choices: {enemies}")
enemy_choice = ''
while enemy_choice not in enemies:
    enemy_choice = input(str("What enemy would you like to verse?"))
    if enemy_choice in enemies:
        print(f"{enemy_choice} is a strong enemy. Good luck!")
    else:
        print("Try again.")

print(f"Your health is: {player_health}")
 
print(f"Your enemies health is: {enemy_health}")
while enemy_health > 0 and player_health > 0:
    print("It's your turn to fight your enemy.")
    enemy_health = enemy_health - damage
    if enemy_health < 0:
        enemy_health = 0
    print(f"Enemy health is now {enemy_health}")

    print(f"{enemy_choice}'s turn.")
    player_health = player_health - 9
    print(f"Your health is {player_health}")

    if enemy_health <= 0 and player_health >0:
        print("You have won the battle!")
        
    elif enemy_health <= 0 and player_health <= 0:
        print("Yout tied!")
    
    elif enemy_health >0 and player_health <= 0:
        print("You lost :(")
        