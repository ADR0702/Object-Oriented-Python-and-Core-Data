class CalculatorBuzunar:
    def __init__(self):
        self.total=0

    def __str__(self):
        return f"{self.total}"
    

    def __iadd__(self,valoare):
        self.total+=valoare
        return self
    
    def add(self, valoare):
        self.total+=valoare
    def sub(self, valoare):
        self.total-=valoare
    def mul(self, valoare):
        self.total*=valoare
    def div(self, valoare):
        self.total/=valoare
        

calc+=2
print(calc)