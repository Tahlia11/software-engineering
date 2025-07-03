action = input(str("What did they do?"))
post = input("Did they like your lates post? ").lower()== "yes"
real_life = input("Are they your real like friend? ").lower == "yes"

if action in ["apologised", "praised"]:
    if post == True:
        if real_life == True:
            print("They are a true friend. Stay following them.")
        else:
            print("Maybe lets take a break. Mute them")
    else:
        if real_life == True:
            print("Maybe they missed the post. Stay following them.")
        else:
            print("I dont know if that is someone we want to associate with. Unfollow them.")
    

elif action in ["ignored", "insulted"]:
    if post == True:
        if real_life == True:
            print("Everyone has a bad day. Maybe lets give them a break. Mute!")
        else:
            print("I don't even know you! Unfollow!")
    else:
        if real_life == True:
            print("Thats rude! Unfollow!")
        else:
            print("No one talks to you like that. Block!")

else:
    print("Error! Try again!")

