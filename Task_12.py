Implement the design of the Account class so that the following output is produced:

class Account:
    def __init__(self, name="Default Account", b=0.0):
        self.name = name
        self.balance = b

    def details(self):
        return f"{self.name}\n{self.balance}"

    def withdraw(self, y):
        if y > self.balance or y >= 6930:
            print("Sorry, Withdraw unsuccessful! The account balance after deducting withdraw amount is equal to or less than minimum.")
        else:
            self.balance -= y
            print(f"Withdraw successful! New balance is: \n{self.balance}")


a1 = Account()
print(a1.details())
print("------------------------")
a1.name = "Oliver"
a1.balance = 10000.0
print(a1.details())
print("------------------------")
a2 = Account("Liam")
print(a2.details())
print("------------------------")
a3 = Account("Noah", 400)
print(a3.details())
print("------------------------")
a1.withdraw(6930)
print("------------------------")
a2.withdraw(600)
print("------------------------")
a1.withdraw(6929)
