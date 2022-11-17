Using TaxiLagbe apps, users can share a single taxi with multiple people.
Implement the design of the TaxiLagbe class so that the following output is produced:
Hint:
1. Each taxi can carry maximum 4 passengers
2. addPassenger() method takes the last name of the passenger and ticket fare for that
person in an underscore (-) separated string.



from multipledispatch import dispatch
class TaxiLagbe:

    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.dic = {}
        self.fare = 0

    @dispatch(str, str)
    def addPassenger(self, x, y):
        pass_info = x.split("_") + y.split("_")
        if len(self.dic) <= 4:
            for i in range(0, 4, 2):
                self.dic[pass_info[i]] = int(pass_info[i+1])
                print(f"Dear {pass_info[i]}! Welcome to TaxiLagbe.")
        else:
            print("Taxi Full! NO more passengers can be added")

    @dispatch(str)
    def addPassenger(self, x):
        pass_info = x.split("_")
        if len(self.dic) < 4:
            self.dic[pass_info[0]] = int(pass_info[1])
            print(f"Dear {pass_info[0]}! Welcome to TaxiLagbe.")
        else:
            print("Taxi Full! NO more passengers can be added.")

    def printDetails(self):
        print(f"Trip info for Taxi number:{self.name}")
        print(f"This taxi can cover only {self.location} area.")
        print(f"Total passengers: {len(self.dic)}", "\nPassenger list:")
        for i in self.dic:
            print(i, end=",")
            self.fare += self.dic[i]
        print()
        print(f"Total collected fare: {self.fare} Taka")
        self.fare = 0


taxi1 = TaxiLagbe('1010-01', 'Dhaka')
print('-------------------------------')
taxi1.addPassenger('Walker_100', 'Wood_200')
taxi1.addPassenger('Matt_100')
taxi1.addPassenger('Wilson_105')
print('-------------------------------')
taxi1.printDetails()
print('-------------------------------')
taxi1.addPassenger('Karen_200')
print('-------------------------------')
taxi1.printDetails()
print('-------------------------------')
taxi2 = TaxiLagbe('1010-02', 'Khulna')
taxi2.addPassenger('Ronald_115')
taxi2.addPassenger('Parker_215')
print('-------------------------------')
taxi2.printDetails()
