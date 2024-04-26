class Calculator:
    def __init__(self, num1, num2) -> None:
        self.num1 = num1
        self.num2 = num2 
    
    def substraction(self) -> int:
        return self.num1 - self.num2 

    def addition(self):
        return self.num1 + self.num2 

    def multiplication(self):
        return self.num1 * self.num2

    def division(self):
        try:
            result = self.num1 / self.num2
            return "{:.4f}".format(result)
        except ZeroDivisionError:
            print("Error: Division by zero is not allowed")
            return None


if __name__ == "__main__":
    print("Welcome to the Calculator App. ")
    while (True):
        
        num1 = int(input("Enter First Number: "))
        num2 = int(input("Enter Second Number: "))
        symbol = input("Specify Operation(+, -, /, *): ")
        calc_obj = Calculator(num1, num2)
        if symbol == '+':
            print("Addition: ", calc_obj.addition()) 
        elif symbol == '-':
            print("Substraction: ", calc_obj.substraction()) 
        elif symbol == '*':
            print("Multiplication: ", calc_obj.multiplication())
        elif symbol == '/':
            print("Division: ", calc_obj.division())
        else:
            print("Invalild input, please press correct symbol for calculation")
        
        option = input("Enter 'C' to continue or 'Q' to exit the program: ")
        if option =='Q':
            break 



