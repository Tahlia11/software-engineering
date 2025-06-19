while True:

    question = input('enter an number:')
    print("you entered:", question)

    if question.isdigit():
        print("This is valid.")
        break
    else:
        print('Did you enter the right thing? I think not. Try again')

print('end')


#activity 4
num = 1 
num <= 10
while True:
    print("number:", num)
    num += 1
    if num > 10:
        break
    print("didn't break")
print("finally broke out the loop")
