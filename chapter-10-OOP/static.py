class Employee:
    company="Google"
    def getsalary(self,signature):
        print(f"salary of a Employee working in {self.company} is {self.salary}\n{signature}")
    @staticmethod
    def greet():
        print("Good morning, sir")
    @staticmethod
    def time():
        print("The time is 9am in the morning")
harry=Employee() #object
harry.salary=100000
harry.getsalary("Thanks") #Employee.getsalary(harry)
harry.greet() #Employee.greet()
harry.time()