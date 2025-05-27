import math

class Paralelogram:
    def __init__(self, lungime, latime, unghi):
        self.lungime=lungime
        self.latime= latime
        self.unghi=unghi
    def __str__(self):
        return f"{self.forma()} are Lungime:{self.lungime} Latime{self.latime} Unghi:{self.unghi} are aria: {self.aria()}"
    def aria(self):
        return self.lungime*self.latime
    def este_dreptunghi(self):
        return self.unghi==90
    def este_romb(self):
        return self.latime==self.lungime
    def este_patrat(self):
        return self.este_dreptunghi() and self.este_romb()
    def forma(self):
        if self.este_patrat():
            return"Patrat"
        elif self.este_dreptunghi():
            return "dreptunghi"
        elif self.este_romb():
            return"romb"
        else:
            return "Paralelogram"  
              
paralelogram = Paralelogram(20,30, 100)
print(paralelogram)

dreptunghi= Paralelogram(10,20,90)
print(dreptunghi)

romb=Paralelogram(40,40,40)
print(romb)

patrat=Paralelogram(40,40,90)
print(patrat)