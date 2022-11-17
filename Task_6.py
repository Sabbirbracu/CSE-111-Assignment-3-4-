Write a class called Customer with the required constructor and methods to get the
following output.
Subtasks:
1. Create a class called Customer.
2. Create the required constructor.
3. Create a method called greet that works if no arguments are passed or if one
argument is passed. (Hint: You may need to use the keyword NONE)
4. Create a method called purchase that can take as many arguments as the user
wants to give.


class Customer:

    def __init__(self, name):
        self.name = name

    def greet(self, name=None):
        if name is None:
            print("Hello!")
        else:
            print(f"Hello {self.name} !")

    def purchase(self, *items):
        self.item = items
        print(f"{self.name}, you purchased {len(self.item)} item(s):")
        for i in self.item:
            print(i)


customer_1 = Customer("Sam")
customer_1.greet()
customer_1.purchase("chips", "chocolate", "orange juice")
print("-----------------------------")
customer_2 = Customer("David")
customer_2.greet("David")
customer_2.purchase("orange juice")
