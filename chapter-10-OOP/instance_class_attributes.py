class Employee:
    company="Google"
    salary=100
    

harry=Employee()
rajini=Employee()
#creating instance attribute salary for both the objects 
#harry.salary=300
#rajini.salary=400
print(harry.salary)
print(rajini.salary)
#below line throws an error as address is not present in the instance/class
#print(rajini.address)