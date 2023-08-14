Design the Student class such a way so that the following code provides the expected
output.
Hint:
● Write the constructor with appropriate default value for arguments.
● Write the dailyEffort() method with appropriate arguments.
● Write the printDetails() method. For printing suggestions check the following
instructions.
⮚ If hour <= 2 print 'Suggestion: Should give more effort!'
⮚ If hour <= 4 print 'Suggestion: Keep up the good work!'
⮚ Else print 'Suggestion: Excellent! Now motivate others.'
[You are not allowed to change the code below]

class Student:

    def __init__(self, name, id, dept=None):
        self.name = name
        self.id = id
        if dept is None:
            self.dept = "CSE"
        else:
            self.dept = dept

    def dailyEffort(self, h):
        self.hour = h

    def printDetails(self):
        print(
            f"Name: {self.name} \nId: {self.id} \nDepertment: {self.dept} \nDaily Efforts: {self.hour} hour(s)")

        if self.hour <= 2:
            print("Suggestion: Should give more efforts!")
        elif self.hour <= 4:
            print("Suggestion: Keep up the good work!")
        else:
            print("Suggestion: Excellent! Now motivate others")


harry = Student('Harry Potter', 123)
harry.dailyEffort(3)
harry.printDetails()
print('========================')
john = Student("John Wick", 456, "BBA")
john.dailyEffort(2)
john.printDetails()
print('========================')
naruto = Student("Naruto Uzumaki", 777, "Ninja")
naruto.dailyEffort(6)
naruto.printDetails()
