

class Concediu:
    def __init__(self, nr_zile):
        self.zile=nr_zile
    def __str__(self):
        return f"Concediu mai are {self.zile} zile"

    def incepe(self):
        print("YEEE")
    def bucurie(self):
        self.zile-=1

concediu=Concediu(3)
print(concediu)
print(Concediu)

concediu.incepe()


concediu_de_iarna=Concediu(20)
print(concediu_de_iarna)
concediu_de_iarna.incepe()


concediu_de_studii=Concediu(30)
print(concediu_de_studii)
concediu_de_studii.incepe()

concediu_de_studii.bucurie()
print(concediu_de_studii)

concediu_de_iarna.bucurie()
print(concediu_de_iarna)