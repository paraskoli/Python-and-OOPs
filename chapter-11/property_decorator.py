class Employee:
    company="Microsoft"
    salary=5500
    salarybonus=504
    # totalsalary=6000

    @property
    def totalSalary(self):
        return self.salary+self.salarybonus

    @totalSalary.setter
    def totalSalary(self,val):
        self.salarybonus=val - self.salary

e=Employee()
#print(e.totalsalary()) #if property is not included
print(e.totalSalary)
e.totalSalary=5800
print(e.salary)
print(e.salarybonus)