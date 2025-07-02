tempurature = 35
if tempurature > 30:
    print("Its warm")
    print("Drink water")
elif tempurature > 20:
    print("It's nice")
else:
    print("It's cold")
print("Done")


age = 22
message = "Eligible" if age >= 18 else "Not eligible"
print(message)



high_income = True
good_credit = True
student = True

if (high_income or good_credit) and not student:
    print("Eligible")
else:
    print("Not eligible")


high_income = False
good_credit = True
student = True

if high_income or good_credit or not student:
    print("Eligible")


#age should be between 18 and 65
age = 22
if age >= 18 and age < 65:
    print("eligible")

if 18<= age <65:
    print("eligiible")
#These are same thing

if 10 == "10":
    print("a")
elif "bag" > "apple" and "bag" > "cat":
    print("b")
else:
    print("c")