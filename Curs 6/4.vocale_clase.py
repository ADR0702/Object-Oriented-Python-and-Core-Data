class Procesatortext:
    def __init__(self, text):
        self.text=text
    def __str__(self):
        return self.text
    def elimina_vocale (self):
        vocale= "aeiouAEIOU"
        rezultat=""
        for i in self.text:
            if i not in vocale:
                rezultat+=i
        return rezultat

procesator=Procesatortext("la multi ani")
print(procesator)

print(procesator.elimina_vocale())