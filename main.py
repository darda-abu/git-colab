class Calculator:
    def __init__(self, num1, num2, symbol) -> None:
        self.num1 = num1
        self.num2 = num2 
        self.symbol = symbol
    
    def substraction(self, num1, num2) -> int:
        return num1 - num2 



if __name__ == "__main__":
    num1 = int(input())
    num2 = int(input())
    symbol = input()
    calc_obj = Calculator(num1, num2, symbol)

    if symbol == '-':
        print("Substraction:", calc_obj.substraction(num1, num2)) 


        
