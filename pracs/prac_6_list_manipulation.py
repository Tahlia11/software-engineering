no_drinks =[]
drinks = [
    "Water",
    "Orange Juice",
    "Apple Juice",
    "Lemonade",
    "Iced Tea",
    "Coffee",
    "Green Tea",
    "Hot Chocolate",
    "Milk",
    "Cola",
    "Ginger Ale",
    "Energy Drink",
    "Smoothie",
    "Milkshake",
    "Sparkling Water",
    "Herbal Tea",
    "Coconut Water",
    "Mango Lassi",
    "Tomato Juice",
    "Grape Juice"
]
drinks.remove("Milk")
drinks.remove("Cola")
drinks.append("Jungle Juice")
no_drinks = drinks[-4:]
print(no_drinks)
print(drinks)
print(len(drinks))
#remove Milk and Cola from the list
#update the list bu adding 'Jungle Juice' to the list
#make a new list by slicing the last 4 elements off this list and into a new list called 'no_drinks'.
#ouput the contents of 'drinks' and 'no_drinks' to the terminal window
#Calulate the length of 'drinks' at the end of this manipulation hint: print(len(somelist))