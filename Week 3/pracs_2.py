name = input("what is your name?")

#staring values
health = 100
food = 50
in_cave = True

hours = int(input("How many hours did you wait in the cave?"))

#algorithm - appy effects
health -= hours * 5
food -= hours * 3

#show result
print(f"{name}, your health is now {health}")
print(f"your food is now {food}")

#condition check
if health <50 or food <20:
    print("You are weak!")

if hours > 5:
    print("You survived a night in the cave!")
else:
    print("You left too early and are dead")




