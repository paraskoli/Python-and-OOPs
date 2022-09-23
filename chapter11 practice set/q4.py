#(a+bi)(c+di)=(ac-bd)+(ad+bc)
import bdb


class Complex:
    def __init__(self,r,i):
        self.real=r
        self.imaginary=i

    def __add__(self,c):
        return Complex(self.real+c.real,self.imaginary+c.imaginary)

    def __mul__(self,c):
        mlReal=(ac-bd)
        return Complex(self.real*c.real,self.imaginary+c.imaginary)

    def __str__(self):
        return f"{self.real}+{self.imaginary}i"

c1=complex(1,5)
c2=complex(8,5)
print(c1+c2)