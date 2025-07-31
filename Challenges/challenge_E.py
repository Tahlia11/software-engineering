def calculator(first_number, second_number, operation):
    if operation == "add":
        return first_number + second_number
    elif operation == "subtract":
        return first_number - second_number
    else:
        return "Error: operation not supported"
    
print(calculator(6, 4, "add"))
print(calculator(9, 7, "subtract"))
print(calculator(10, 5, "divide"))


def compare_numbers(num1, num2):
    if num1 > num2:
        return 
    elif num1 < num2:
        return
    else:
        return
    
print(compare_numbers(3,4))