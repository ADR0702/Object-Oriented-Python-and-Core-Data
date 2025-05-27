
vocale= "aeiouAEIOU"
def elimina_vocale(string):
    rezultat=""
    for i in string:
        if i not in vocale:
            rezultat+=i
    return rezultat

valoare_returnata=elimina_vocale("la multi ani")
print(valoare_returnata)
