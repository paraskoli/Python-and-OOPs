class Person:
    country="India"

    def takrBreath(self):
        print("I am breathing...")

class Employee(Person):
    company="Honda"
    
    def getsalary(self):
        print(f"salary is {self.salary}")

    def takrBreath(self):
        print("I am an Employee so I am Luckily breathing..")

class Programmer(Employee):
    company="fiverr"

    def getsalary(self):
        print(f"No salary to programmers")

    def takrBreath(self):
        print("I am a Programmer so I am breathing++..")

p=Person()
p.takrBreath()
e=Employee()
e.takrBreath()
pr=Programmer() 
pr.takrBreath()
print(pr.company)
#print(p.company) #throws an error
print(e.country)