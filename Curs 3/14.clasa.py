class Planeta:
    def __init__(self, nume, culoare, este_locuit=False):
        print("functia init a fost chemata")
        print("numele primit este:", nume)
        self.nume=nume
        self.culoare=culoare
        self.este_locuit=este_locuit

obiect1=Planeta("Pamant", "Albastra", True)
print(obiect1, "\n")
print(obiect1.nume, obiect1.culoare)


obiect2=Planeta("Jupiter", "portocalie")
print(obiect2)
print(obiect2.nume, obiect2.culoare)

obiect3=Planeta("Marte", "rosu")
print(obiect3)
print(obiect3.nume, obiect3.culoare)