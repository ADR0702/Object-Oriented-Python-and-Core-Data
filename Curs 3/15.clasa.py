import math

class Cerc:
    def __init__(self, raza):
        self.raza=raza
    def __str__(self):
        return f" Perimetru:{self.perimetru()} \n Aria:{self.aria()} \n Diametru: {self.diametru()}"
        
    
    def perimetru(self):
        return 2* math.pi*self.raza
    def aria(self):
        return math.pi *self.raza**2
    def diametru(self):
        return self.raza*2
    def aratavalorile(self):
        print("perimetru", self.perimetru())
        print("Aria:", self.aria())
        print("diametru:", self.diametru())

cerc1=Cerc(1)

print(cerc1)

cerc2=Cerc(2)

print(cerc2)
