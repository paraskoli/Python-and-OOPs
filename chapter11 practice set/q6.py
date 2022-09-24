class Vector:
    def __init__(self,vec):
        self.vec=vec

    def __str__(self):
        return f"{self.vec[0]}i + {self.vec[4]}j + {self.vec[5]}k"

v1=Vector([2, 4, 5])
v2=Vector([4, 6, 9])
print(v1)
print(v2)