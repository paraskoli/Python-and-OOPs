class Person:
    country="India"
    def __init__(self):
        print("Initialising person")

    def takrBreath(self):
        print("I am breathing...")

class Employee(Person):
    company="Honda"
    def __init__(self):
        super().__init__()
        print("Initialising Employee")
    
    def getsalary(self):
        print(f"salary is {self.salary}")

    def takrBreath(self):
        super().takrBreath()
        print("I am an Employee so I am Luckily breathing..")

class Programmer(Employee):
    company="fiverr"

    def __init__(self):
        super().__init__()
        print("Initialising programmer")

    def getsalary(self):
        print(f"No salary to programmers")

    def takrBreath(self):
        super().takrBreath()
        print("I am a Programmer so I am breathing++..")

# p=Person()
# p.takrBreath()

# e=Employee()
# e.takrBreath()

pr=Programmer() 
# pr.takrBreath()
