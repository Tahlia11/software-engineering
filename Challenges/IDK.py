action = input(str("What did they do?"))
if action == "apologised" or action == "praised":
    post = input("Did they like your lates post? ").lower()== "yes"
    if post == True:
        

elif action == "insult" or action == "ignored":
    input(bool{post})

else:
    print("Error, please try again")



action = input(str("What did they do?"))
post = input("Did they like your lates post? ").lower()== "yes"
real_life = input("Are they your real like friend? ").lower == "yes"

if action == "ignored" or action == "insulted" and post =="no" and real_life == "no":
    print("How dare they! Block them!")

elif action == "praised" or action == "apologised" and post == "yes" and real_life == "yes":
    print("They are a true friend and have your back!")

elif action == "praised" or action == "apologised" and post == "yes" and real_life == "no":
    print("They have your back this time, but be careful. People are not always what they seem.")
else:
    print("Error, please try again")