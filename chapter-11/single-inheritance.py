class Employee:
    company="Google"

    def showDetails(Self):
        print("This is an Employee")

class Programmer(Employee):
    language="Python"

    def getlanguage(Self):
        print(f"the language is {self.language}")

    def showDetails(Self):                    #override
        print("This is an programmer")

e=Employee()
p=Programmer()
e.showDetails()
p.showDetails()
print(p.language)
print(p.company)