#sequence
print("Hey")
print("How are you?")

#selection
score = 90
if score >= 50:
    print("congrats, you passed!")
else:
    print("too bad")


#iteration
lives=2
while lives > 6:
    print ("Keep playing")

for level in range(1,4):
    print("level", level)
#will print each level from 1-3 excluding 4 saying "level..."

#variables and data types
timeleft=5
#int = numbers
favouritefood="cinnabun"
#str = text
favouritefood = True
#bool = true or false

#list = collection of items


#functions
def greet(name):
    print(f'hi {name}')

greet('tahlia')
#when not recognising as function use def to define function
favouritefood = 'lasagne'
def bad(favouritefood):
    print(f'beautiful'{favouritefood})