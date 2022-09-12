class Employee:
    company="Google"
    def getSalry(self):
        print(f"salary for this employee working in{self.company}is{self.salary}")

harry=Employee()
harry.salary=100000
harry.getSalry()#Employee.getsalary(harry)