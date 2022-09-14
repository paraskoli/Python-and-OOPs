class Employee:
    company="Google"
    ecode=120

class freelancer:
    company="Visa"
    level=0
    
    def upgradeLevel(self):
        self.level=self.level+1

class Programmer(Employee,freelancer): 
    name="Rohit"

p=Programmer()
p.upgradeLevel()
print(p.company) #print Google because prefrence given to employee in arguments because its written first
print(p.name)
print(p.ecode)
print(p.level)