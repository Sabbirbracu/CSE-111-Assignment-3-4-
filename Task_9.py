Implement the design of the Batsman class so that the following output is produced:
Hint: Batting strike rate (s/r) = runsScored / ballsFaced x 100.


from multipledispatch import dispatch
class Batsman:

    @dispatch(str, int, int)
    def __init__(self, name, run, ball):
        self.name = name
        self.run = run
        self.ball = ball

    @dispatch(int, int)
    def __init__(self, run, ball):
        self.run = run
        self.ball = ball
        self.name = "New Batsman"

    def setName(self, name):
        self.name = name

    def printCareerStatistics(self):
        print(
            f"Name: {self.name} \nRuns Scored: {self.run}, Balls Faced: {self.ball}")

    def battingStrikeRate(self):
        strk = (self.run/self.ball)*100
        return strk


b1 = Batsman(6101, 7380)
b1.printCareerStatistics()
print("============================")
b2 = Batsman("Liton Das", 678, 773)
b2.printCareerStatistics()
print("----------------------------")
print(b2.battingStrikeRate())
print("============================")
b1.setName("Shakib Al Hasan")
b1.printCareerStatistics()
print("----------------------------")
print(b1.battingStrikeRate())
