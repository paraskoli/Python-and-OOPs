class Employee:
    salary=1000
    Increment =2
    @property   
    def salaryAfterIncrement(self):
        return self.salary*self.Increment

    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self,sai):
        self.Increment=sai/self.salary

e=Employee()
print(e.salaryAfterIncrement)
