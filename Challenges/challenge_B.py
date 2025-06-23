name = input(str("What is your username?"))
woodBlocks = int(input("How many woodblocks do you have?"))
woodWeight = float(input("What is the weight of a single woodblock?"))
daytime = input("Is it daytime?").lower() == "yes"

while woodBlocks < 10:
    print("How many more woodblocks would you like to collect?")
    successfu = 10
    for woodBlocks in range (1,10):
        woodBlocks + 1
        print(woodBlocks)
        if successful:
            break