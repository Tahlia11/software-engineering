# correct this code
swiftAlbums=["Taylor Swift","Fearless","Speak Now","Red","1989","Reputation","Lover"]

print("Taylor Swift Albums:")
for album in swiftAlbums:
    print(swiftAlbums)

albumToCheck = input("Enter an album to check: ")
if albumToCheck in swiftAlbums:
    print(f"{albumToCheck} is in the list")
else:
    print(f"{albumToCheck} is not in the list")

while True:
    print("\n"*5)
    albumToCheck = input("Enter an album to check or type 'exit to quit:")
    if albumToCheck == "exit":
        break
    if albumToCheck in swiftAlbums:
        print(f"{albumToCheck} is on the list")
    else:
        print(f"{albumToCheck} is not on the list")