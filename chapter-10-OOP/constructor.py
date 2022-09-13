class Employee:
    company="Google"
    def __init__(self,name,salary,company):
        self.name=name
        self.salary=salary
        self.company=company
        print("Employee is created")
    def getDetails(self):
        print(f"The name of the employee is {self.name}")
        print(f"The salary of the employee is {self.salary}")
        print(f"The company of the employee is {self.company}")
          
harry=Employee("harry",1000,"Youtube")
harry.getDetails()