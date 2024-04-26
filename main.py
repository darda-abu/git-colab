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
    
    def parity(self,num):
        if num % 2 : return "Odd"
        return "Even"
    
    def sign(self, num):
        if num >= 0 : return "Positive"
        return "negative"
    
    def display_text(self):
        num1_formatted = "({}; {};)".format(self.parity(self.num1), self.sign(self.num1))
        num2_formatted = "({}; {};)".format(self.parity(self.num2), self.sign(self.num2))
        result_formatted = "({}; {};)".format(self.parity(self.result), self.sign(self.result))
        return "{} {} {} = {}".format(num1_formatted, self.operator, num2_formatted, result_formatted)
    
    def display_digits(self):
        return "{} {} {} = {}".format(self.num1, self.operator, self.num2, self.result)
    
    def __str__(self) -> str:
        return "\n".join([self.display_digits(), self.display_text()])
        

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



