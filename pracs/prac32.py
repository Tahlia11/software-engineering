fruits = ["apple", "banana", "cherry"]
print(fruits)
# Lists use square brackets [ ] and each item is separated by a comma.

#Step 2: Access Items in a List
#Each item has a position (called an index) starting from 0.

print(fruits[0])  # prints "apple"
print(fruits[2])  # prints "cherry"
print(fruits[-1])
# Use negative numbers to count from the end: fruits[-1] prints "cherry".

#Step 3: Change or Add Items
#You can change an item by using its index, or add new items using .append().

fruits[1] = "blueberry"
fruits.append("orange")
print(fruits)

 # Result: ['apple', 'blueberry', 'cherry', 'orange']

#Step 4: Remove Items
#se .remove() or del to remove items from a list.


fruits.remove("apple")  # removes by name
del fruits[0]           # removes by position
print(fruits)
# Make sure the item exists before removing, or it will cause an error.

#Step 5: Loop Through a List
#Use a for loop to go through each item in the list.

for fruit in fruits:
    print("I like", fruit)
# This is great for printing, checking, or using each item one by one.