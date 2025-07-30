myNumbers = []
for i in range (1,4):
    userInput = (input("Enter number:"))
    myNumbers.append(userInput)

print(myNumbers)
for numbers in myNumbers:
    print(numbers)


for i in (1,6):
    userInput = input("Enter a new value:")
    myNumbers.append(userInput)

sortedAscending = []
sortedAscending = sorted(myNumbers)

sortedDecending = []
sortedDecending = sorted(myNumbers, reverse=True)

print("Middle number of the original list:")
print(myNumbers[2])

print("Middle number of the sorted ascending list:")
print(sortedAscending[2])

print("Middle number of sorted decending list:")
print(sortedDecending[2])