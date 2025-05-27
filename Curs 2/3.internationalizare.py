
lang = input("choose your language(ro/en/it)")

while lang not in ("ro", "en", "it"):
    lang=input("please choose from (ro/en/it)")


traduceri= {
    "ro": ("introuduceti primul numar", "introduceti doar numere!!", "introuduceti al 2-lea numar", "alegeti operatia (+,-,*,/)", "rezultatul este:"),
    "en": ("insert first number","insert only numbers!!", "insert second number", "choose operation (+,-,*,/)", "the result is"),
    "it": ("Inserire primo numero", "inserisci solo numeri", "Inserire il secundo numero", "scegli l'operazione (+,-,*,/)", "il resultato e"),
}

no1=(input(traduceri[lang][0]))
while not no1.isnumeric():
    no1=(input(traduceri[lang][1]))

no1=int(no1)
print(no1)

no2=(input(traduceri[lang][2]))
while not no2.isnumeric():
    no2=(input(traduceri[lang][1]))
no2=int(no2)
print(no2)

op=input(traduceri[lang][3])

rezultat=no1+no2
print(traduceri[lang][4], rezultat)