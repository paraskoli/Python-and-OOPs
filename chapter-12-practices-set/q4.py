class claculator:
    @staticmethod
    def greet():
        print("*****hello welcome to the best calculator for finding cube,square and squareroot*****")
    def __init__(self,num):
        self.number=num
    
    def square(self):
        print(f"The square of {self.number} is {self.number **2}")

    def squareRoot(self):
        print(f"The squareRoot of {self.number} is {self.number **0.5}")

    def cube(self):
        print(f"The cube of {self.number} is {self.number **3}")

a=claculator(9)
a.greet()
a.square()
a.squareRoot()
a.cube()