Implement the design of the StudentDatabase class so that the following output is
produced:
GPA = Sum of (Grade Points * Credits)/ Credits attempted

class StudentDatabase:

    def __init__(self, name, id_no):
        self.name = name
        self.id_no = id_no
        self.grades = {}

    def calculateGPA(self, x, y):
        grd = 0
        dic1 = {}
        crs = []
        for element in x:
            list1 = element.split(":")
            crs.append(list1[0])
            grd += float(list1[1])
            total_grade = grd/len(crs)
            course = tuple(crs)
        dic1[course] = round(total_grade, 2)

        self.grades[y] = dic1

    def printDetails(self):
        print(f"Name:{self.name} \nId: {self.id_no}")
        for i in self.grades:
            print(f"Course taken in {i}:")
            for j in self.grades[i]:
                for k in j:
                    print(k)
            print("GPA:", self.grades[i][j])


s1 = StudentDatabase('Pietro', '10101222')
s1.calculateGPA(['CSE230: 4.0', 'CSE220: 4.0', 'MAT110: 4.0'],
                'Summer2020')
s1.calculateGPA(['CSE250: 3.7', 'CSE330: 4.0'], 'Summer2021')
print(f'Grades for {s1.name}\n{s1.grades}')
print('------------------------------------------------------')
s1.printDetails()
s2 = StudentDatabase('Wanda', '10103332')
s2.calculateGPA(['CSE111: 3.7', 'CSE260: 3.7', 'ENG101: 4.0'],
                'Summer2022')
print('------------------------------------------------------')
print(f'Grades for {s2.name}\n{s2.grades}')
print('------------------------------------------------------')
s2.printDetails()
