Implement the design of the UberEats class so that the following output is produced:
[For simplicity, you can assume that a customer will always order exact 2 items]


class UberEats:

    def __init__(self, name, mobile, adds):
        self.name = name
        self.mobile = mobile
        self.adds = adds
        print(f"{self.name}, welcome to UberEats!")

    def add_items(self, *arg):
        self.food1 = arg[0]
        self.food2 = arg[1]
        self.price1 = arg[2]
        self.price2 = arg[3]

    def print_order_detail(self):
        dic = {}
        self.list = []
        dic[self.food1] = self.price1
        dic[self.food2] = self.price2

        self.list.append(
            f"user details: Name:{self.name}, Phone: \n{self.mobile}, Address:{self.adds}")
        self.list.append(
            f"Orders:{dic} \nTotal paid Amount:{self.price1+self.price2}")
        return "\n".join(self.list)


order1 = UberEats("Shakib", "01719658xxx", "Mohakhali")
print("=========================")
order1.add_items("Burger", "Coca Cola", 220, 50)
print("=========================")
print(order1.print_order_detail())
print("=========================")
order2 = UberEats("Siam", "01719659xxx", "Uttara")
print("=========================")
order2.add_items("Pineapple", "Dairy Milk", 80, 70)
print("=========================")
print(order2.print_order_detail())
