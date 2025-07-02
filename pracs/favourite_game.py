favourite_games= ["Monopoly", "Scrabble", "Cluedo"]
print(favourite_games)
favourite_games[1] = "Greedy Grandma"
print(favourite_games)
favourite_games.append("Guess Who")
print(favourite_games)
favourite_games.remove("Greedy Grandma")
print(favourite_games)
for game in favourite_games:
    print(f"I love playing {game}!")
print(len(favourite_games))

# Example list
animals = ["dog", "cat", "horse"]
print(animals)

fruits = ["apple", "banana", "cherry"]
print(fruits)

print(fruits[0])  # First item
print(fruits[2])  # Third item

fruits[1] = "mango"
print(fruits)  # ['apple', 'mango', 'cherry']

# Add to end of list
fruits.append("kiwi")

# Remove an item
fruits.remove("apple")

for fruit in fruits:
    print("I like", fruit)

print(len(fruits))  # Number of items in the list