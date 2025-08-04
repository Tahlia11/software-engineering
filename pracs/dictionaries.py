characters = {
    "dc": {
        "name": "Diana Prince",
        "alias": "Wonder Woman",
        "team": "Justice League"
    },
    "marvel": {
        "name": "Carol Danvers",
        "alias": "Captain Marvel",
        "team": "Avengers"
    },
    "2000ad": {
        "name": "Cassandra Anderson",
        "alias": "Judge Anderson",
        "team": "Justice Department"
    }
}

ca = characters["marvel"]["name"]
ca1 =characters["marvel"]["alias"]
ca2 = characters["marvel"]["team"]
print(f"{ca} is {ca1} from the {ca2}")

ss = characters["2000ad"]["name"]
ss1= characters["2000ad"]["alias"]
ss2= characters["2000ad"]["team"]
print(f"{ss} is {ss1} from the {ss2}")

# Define a dictionary to demonstrate the use of KEY and SUBKEY
data = {
    "KEY": {
        "SUBKEY": "This is a value associated with the subkey."
    }
}

# Accessing the value using KEY and SUBKEY
value = data["KEY"]["SUBKEY"]
print(f"The value is: {value}")

for key in characters:

    print(key)
    for subkey in characters[key]:
        print(subkey, characters[key][subkey])

for subkey in characters["dc"]:
    print(f'The subkey is {subkey}, and the characters are {characters["dc"][subkey]}')

for subkey in characters["marvel"]:
    print(f"The subkey is {subkey}, and the  characters are {characters["marvel"][subkey]}")

for subkey in characters["2000ad"]:
    print(f"The subkey is {subkey}, and the characters are {characters["2000ad"][subkey]}")