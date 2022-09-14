class Train:
    def __init__(self,name,fare,seats):
        self.name=name
        self.fare=fare
        self.seats=seats

    def getStatus(self):
        print("*********")
        print(f"The name of the Train is {self.name}")
        print(f"The sets availabe in the train are {self.seats}")
        print("*********")
        
    def fareInfo(self):
        
        print(f"The price of the ticket is : Rs {self.fare}")
    
    def bookTickets(self):
        if (self.seats>0):
            print(f"Your ticket has been booked! your seat number is {self.seats}")
            self.seats=self.seats-1
        else:
            print("sorry this train is full")    
intercity=Train("Intercity express: 1405",90,300)
intercity.getStatus()
intercity.bookTickets()
intercity.getStatus()