#Exercise 1
name = str(input("What is your childs name?"))
age = int(input("What is their age?"))
snack = str(input("What snack do they want to bring?"))
game_time = float(input("how long should they be in the game? Answer in minutes"))
water_play = bool(input("Do they like water play? Answer yes/no"))
print(f"Hi {name}! You're {age} years old and are ready to play in Bluey's backyard. You'll play for {game_time} minutes and bring your snack: {snack}. Water play? {water_play}!")

#Exercise 2
games_list = ["Keepy Uppy", "Magic Asparagus", "Shadowlands", "Obstactle course", "Muffin Cone"]
print(games_list)

print("First game:", games_list[0])
print("Last game:", games_list[-1])

games_list.append("Grannies")
print(games_list)

games_list[1] = "Magic Wand"
print(games_list)

for game in games_list:
    print("Let's play:", game)

def count_games():
    print("Total games:", len(games_list))

count_games()