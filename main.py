def divide(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed")
        return None

def multiply(num1,num2):
    
    return num1*num2


operation = input().split()

ans = 0

if operation[1] == '+': ans = add(float((operation[0]), float(operation[2]))
if operation[1] == '-': ans = substract(float(operation[0)], float(operation[2]))
if operation[1] == '*': ans = multiply(float(operation[0]), float(operation[2]))
if operation[1] == '/': ans = divide(float(operation[0)], float(operation[2]))

