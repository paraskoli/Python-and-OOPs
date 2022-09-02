class Railwayform:
    formType="RailwayForm"
    def printData(self):
        print(f"Name is {self.name}")
        print(f"Train is {self.train}")
harryapplication = Railwayform()
harryapplication.name="Harry"
harryapplication.train="Rajdhani Express"
harryapplication.printData()