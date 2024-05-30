class Calculator:

    def add(self, a, b):
        return int(a + b)
    
    def substract(self, a, b):
        return int(a - b)
    
    def multiply(self, a, b):
        return int(a * b)
    
    def divide(self, a, b):

        if b == 0:
            raise ValueError("You cannot divide by zero")
        return float(round(a/b, 2))
    

my_calc = Calculator()

print(my_calc.add(5, 10))

print(my_calc.substract(4,5))

print(my_calc.multiply(5, 4))

print(my_calc.divide(0, 2))

print(my_calc.divide(6,3))

print(my_calc.divide(3,2))

