class Patient:
    def __init__(self, name, age, weight, height):
        self.name = name
        self.age = age
        self.weight = weight
        self.height = height
        self.BMI = self.weight/(self.height/100)**2

    def printDetails(self):
        print(
            f"Name: {self.name}\nAge: {self.age}\nWeight: {self.weight} Kg \nHeight: {self.height} Cm \nBMI: {self.BMI}")


p1 = Patient("A", 55, 63.0, 158.0)
p1.printDetails()
print("====================")
p2 = Patient("B", 53, 61.0, 149.0)
p2.printDetails()
