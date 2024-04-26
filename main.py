def divide(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed")
        return None
def Addition(num1,num2):
    return num1 + num2 


operation = input().split()

ans = 0

if operation[1] == '+': ans = add(operation[0], operation[2])
if operation[1] == '-': ans = substract(operation[0], operation[2])
if operation[1] == '*': ans = multiply(operation[0], operation[2])
if operation[1] == '/': ans = divide(operation[0], operation[2])

