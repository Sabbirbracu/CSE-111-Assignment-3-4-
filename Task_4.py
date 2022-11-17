Design the Programmer class in such a way so that the following code provides the
expected output.
Hint:
o Write the constructor with appropriate printing and multiple arguments.
o Write the addExp() method with appropriate printing and argument.
o Write the printDetails() method
[You are not allowed to change the code below]

class Programmer:
    def __init__(self, name, lng, exp=None):
        self.name = name
        self.language = lng
        self.exp = exp
        print("Horray! A new programmer is born")

    def addExp(self, exp):
        self.exp += exp
        print("Updating experiences of", self.name)

    def printDetails(self):
        print("Name:", self.name, "\nLanguage:", self.language,
              "\nExperiences:", self.exp, "Years.")


p1 = Programmer("Ethen Hunt", "Java", 10)
p1.printDetails()
print('--------------------------')
p2 = Programmer("James Bond", "C++", 7)
p2.printDetails()
print('--------------------------')
p3 = Programmer("Jon Snow", "Python", 4)
p3.printDetails()
p3.addExp(5)
p3.printDetails()
