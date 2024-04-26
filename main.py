def division(x, y):
    pass


print("hello")
print("hello")

operation = input().split()

ans = 0

if operation[1] == '+': ans = add(operation[0], operation[2])
if operation[1] == '-': ans = substract(operation[0], operation[2])
if operation[1] == '*': ans = multiply(operation[0], operation[2])
if operation[1] == '/': ans = divide(operation[0], operation[2])

