# class Calculator:

#     def __init__(self, operand1, operand2):
#         self.operand1=operand1
#         self.operand2=operand2
    
#     def add(self):
#         print() self.operand1+self.operand2

#     def sub(self):
#         print() self.operand1-self.operand2
#     def mul(self):
#         print() self.operand1*self.operand2
#     def div(self):
#         if self.operand2==0:
#             print()("divizarea la 0 nu este permisa")
#         else:
#             print() self.operand1/self.operand2

# adunare=Calculator(10,5)
# print(adunare)
# adunare.add()

# scadere=Calculator(40,20)
# print(scadere)
# scadere.sub()

# inmultire=Calculator()
# print(inmultire)
# inmultire.mul()

# impartire=Calculator()
# print(impartire)
# impartire.div()


class Calculator:

    def __init__(self, operand1, operand2):
        self.op1=operand1
        self.op2=operand2
    def __str__(self):
        return f"Calc cu {self.op1} si {self.op2}"
    
    def add(self):
        print(self.op1+self.op2) 
    def sub(self):
        print( self.op1-self.op2)
    def mul(self):
        print(self.op1*self.op2)
    def div(self):
        print(self.op1/self.op2)


calc=Calculator(10,5)
print(calc)

calc.add()
calc.sub()
calc.mul()
calc.div()