

# class Account:
#     def __init__(self, bankaccount):
#         self.bankaccount=bankaccount
#     def __str__(self):
#         return f"mai aveti in cont {self.bankaccount} lei"
#     def balance(self):
#         self.bankaccount=200
#         print(self.bankaccount)
#     def withdraw(self):
#         self.bankaccount-=int(input("introduceti suma pe care doriti sa o retrageti\n"))
#     def addmoney(self):
#         self.bankaccount+=int(input("introduceti suma pe care doriti sa o adaugati\n"))
        
    

# withdraw=Account(200)
# withdraw.withdraw()
# print(withdraw.withdraw())

# addmoney=Account(1200)
# addmoney.addmoney()
# print(addmoney.addmoney())


class Account:
    def __init__(self, balance):
        self.balance = balance

    def __str__(self):
        return f"contul are {self.balance} lei"
    
    def withdraw(self, suma):
        if suma > self.balance:
            print("Fonduri Insuficiente")
        else:
            self.balance-=suma

    def addmoney(self, suma):
        if suma < 0:
            print("nu se poate asa ceva")
        else:    
            self.balance+=suma
    def showbalance(self):
        print(self)
        
cont1= Account(10) 
print(cont1)
cont1.withdraw(11)
print(cont1)
cont1.addmoney(20)
print(cont1)

cont1.showbalance()

    
        