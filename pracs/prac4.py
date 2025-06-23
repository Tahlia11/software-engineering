ground = 0
maxHeight = 100
rocketLocation = 0
while rocketLocation <= maxHeight:
    print(f"Rocket height is {rocketLocation}")
    break
    rocketLocation + 1

while rocketLocation == maxHeight:
    print(f"{maxHeight} has been reached!")
    break

while rocketLocation > ground:
    print(f"Rocket location is {rocketLocation}")
    break
    rocketLocation - 1

if rocketLocation == ground:
    print("Rocket has landed")
    