class Calculator:
    def __init__(self, num1, num2) -> None:
        self.num1 = num1
        self.num2 = num2 
        self.result = 0
        self.operator = ''
    
    def substraction(self) -> int:
        self.result = self.num1 - self.num2 
        self.operator = '+'

    def addition(self):
        self.result = self.num1 + self.num2 
        self.operator = '-'

    def multiplication(self):
        self.result = self.num1 * self.num2
        self.operator = '*'

    def division(self):
        try:
            result = self.num1 / self.num2
            self.result = "{:.4f}".format(result)
        except ZeroDivisionError:
            print("Error: Division by zero is not allowed")
            return None
        self.operator = '/'
    

    def __str__(self) -> str:
        return "{} {} {} = {}".format(self.num1, self.operator, self.num2, self.result)
        

if __name__ == "__main__":
    print("Welcome to the Calculator App. ")
    while (True):
        
        num1 = int(input("Enter First Number: "))
        num2 = int(input("Enter Second Number: "))
        symbol = input("Specify Operation(+, -, /, *): ")
        calc_obj = Calculator(num1, num2)
        if symbol == '+':
            calc_obj.addition()
        elif symbol == '-':
            calc_obj.substraction()
        elif symbol == '*':
            calc_obj.multiplication()
        elif symbol == '/':
            calc_obj.division()
        else:
            print("Invalild input, please press correct symbol for calculation")
            calc_obj.result = ''

        print(calc_obj)

        option = input("Enter 'C' to continue or 'Q' to exit the program: ")
        if option =='Q':
            break 



