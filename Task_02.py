
class Shape:

    def __init__(self, name, x=None, y=None):
        self.name = name
        if self.name == "Triangle":
            self.base = x
            self.height = y
        elif self.name == "Rhombus":
            self.diagonal_1 = x
            self.diagonal_2 = y
        elif self.name == "Square":
            self.side_1 = x
            self.side_2 = y
        elif self.name == "Rectangle":
            self.length = x
            self.width = y

    def area(self):
        if self.name == "Triangle":
            area = 0.5 * self.base * self.height
            #print("Area:", area)
        elif self.name == "Rhombus":
            area = 0.5 * self.diagonal_1 * self.diagonal_2
            #print("Area:", area)
        elif self.name == "Square":
            area = self.side_1*self.side_2
            #print("Area:", area)
        elif self.name == "Rectangle":
            area = self.length * self.width
            #print("Area", area)
        else:
            area = "Unknown Shape"
            #print("Area: Shape Unknown")
        print("Area :", area)


triangle = Shape("Triangle", 10, 25)
triangle.area()
print("==========================")
square = Shape("Square", 10, 10)
square.area()
print("==========================")
rhombus = Shape("Rhombus", 18, 25)
rhombus.area()
print("==========================")
rectangle = Shape("Rectangle", 15, 30)
rectangle.area()
print("==========================")
trapezium = Shape("Trapezium", 15, 30)
trapezium.area()
