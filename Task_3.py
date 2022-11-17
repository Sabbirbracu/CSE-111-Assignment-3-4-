mplement the design of the Calculator class so that the following output is produced:
  
  class Calculator:

    def __init__(self):
        print("Calculator is ready!")

    def calculate(self, x, y, z):
        self.x = x
        self.y = y
        self.sign = z
        if self.sign == "+":
            self.d = self.x + self.y
        elif self.sign == "-":
            self.d = self.x - self.y
        elif self.sign == "*":
            self.d = self.x * self.y
        elif self.sign == "/":
            self.d = self.x/self.y
        return self.d

    def showCalculation(self):
        print(f"{self.x} {self.sign} {self.y} = {self.d}")


c1 = Calculator()
print("==================")
val = c1.calculate(10, 20, '+')
print("Returned value:", val)
c1.showCalculation()
print("==================")
val = c1.calculate(val, 10, '-')
print("Returned value:", val)
c1.showCalculation()
print("==================")
val = c1.calculate(val, 5, '*')
print("Returned value:", val)
c1.showCalculation()
print("==================")
val = c1.calculate(val, 16, '/')
print("Returned value:", val)
c1.showCalculation()
