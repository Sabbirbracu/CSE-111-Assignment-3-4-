Analyze the given code below to write Cat class to get the output as shown.
Hints:
● Remember, the constructor is a special method. Here, you have to deal with
constructor overloading which is similar to method overloading.
● You may need to use the keyword None
● Your class should have 2 variables
[You are not allowed to change the code below]



class Cat:

    def __init__(self, c=None, a=None):
        if c is None:
            self.color = "White"
        else:
            self.color = c
        if a is None:
            self.action = "Sitting"
        else:
            self.action = a

    def printCat(self):
        print(f"{self.color} cat is {self.action}")

    def changeColor(self, c):
        self.color = c


c1 = Cat()
c2 = Cat("Black")
c3 = Cat("Brown", "jumping")
c4 = Cat("Red", "purring")
c1.printCat()
c2.printCat()
c3.printCat()
c4.printCat()
c1.changeColor("Blue")
c3.changeColor("Purple")
c1.printCat()
c3.printCat()
