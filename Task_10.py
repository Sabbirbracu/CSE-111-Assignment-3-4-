#Implement the design of the Author class so that the following output is produced:

class Author:
    def __init__(self, name="Default", *books):
        self.name = name
        self.books = books

    def addBooks(self, *books):
        self.books += books

    def changeName(self, name):
        self.name = name

    def printDetails(self):
        print(f"Author Name:{self.name}", "\n--------", "\nList of Books:")
        for i in self.books:
            print(i)


auth1 = Author('Humayun Ahmed')
auth1.addBooks('Deyal', 'Megher Opor Bari')
auth1.printDetails()
print("===================")
auth2 = Author()
print(auth2.name)
auth2.changeName('Mario Puzo')
auth2.addBooks('The Godfather', 'Omerta', 'The Sicilian')
print("===================")
auth2.printDetails()
print("===================")
auth3 = Author('Paolo Coelho', 'The Alchemist', 'The Fifth Mountain')
auth3.printDetails()
