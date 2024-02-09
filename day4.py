#DAY 4 HACKERRANK 30 DAYS CHALLENGE.

#Declare Class Person...
class Person:
    def __init__(self, initialAge) -> int:
        if initialAge < 0:
            print("Age is not valid, setting Age to 0.")
            self.age = 0
        else: 
            self.age = initialAge
    def AmIOld(self):
        if self.age < 13: 
            print("You are young.")
        elif self.age < 18:
            print("You are a teenager.")
    def yearPasses(self):
        self.age += 1 
        print(self.age)

t = int(input())
for i in range(0, t):
    age = int(input())         
    p = Person(age)  
    p.AmIOld
    for j in range(0, 3):
        p.yearPasses()       
    p.AmIOld
    print("")
