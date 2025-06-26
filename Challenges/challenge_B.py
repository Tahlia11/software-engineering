name = input(str("What is your username?"))
woodBlocks = int(input("How many woodblocks do you have?"))
woodWeight = float(input("What is the weight of a single woodblock (kg)?"))
daytime = input("Is it daytime? (yes/no) ").lower() == "yes"
successful = 10

while woodBlocks < 10:
    print(f"You have {woodBlocks} blocks.") 
    print(f"You need {10 - woodBlocks} more.")
    how_many = int(input("How may more woodblocks would you like?"))
    woodBlocks = how_many + woodBlocks

print("Woodblock collection complete!")
print(f"Username: {name}")
print(f"Total Blocks: {woodBlocks}")
print(f"Total weight: {woodWeight*woodBlocks} kg")
print(f"It is daytime: {daytime}")